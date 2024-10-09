import pandas as pd
from textblob import TextBlob

# Cargar el archivo Excel
excel_file = 'INTERVIEW.xlsx'
xls = pd.ExcelFile(excel_file)

df_cleaned = pd.read_excel(xls, sheet_name='Sheet1', header=4)

df_cleaned.columns = ['Category', 'Unnamed: 1', 'Empty'] + [f'Student_{i}' for i in range(1, len(df_cleaned.columns)-2)]
df_cleaned = df_cleaned.drop(columns=['Empty'])

student_ids = {f'Student_{i}': f'STUD_{i}' for i in range(1, len(df_cleaned.columns[2:])+1)}

def classify_learning_help(response):
    response = response.lower()
    sentiment = TextBlob(response).sentiment.polarity
    if sentiment < 0:
        return {"It hasn’t helped me": 1, "Learn to be self-disciplined": 0, "Have a better time management": 0, "Adapt to my own learning process": 0, "Learn to adapt and use technology": 0, "Learn more resources and courses": 0}
    
    help_categories = {
        "Learn to be self-disciplined": ["self-discipline", "discipline"],
        "Have a better time management": ["time management", "schedule", "manage time"],
        "Adapt to my own learning process": ["adapt", "own pace", "personalize"],
        "Learn to adapt and use technology": ["technology", "tools", "platforms"],
        "Learn more resources and courses": ["resources", "courses"]
    }
    
    result = {category: 0 for category in help_categories}
    
    found = False
    for category, keywords in help_categories.items():
        for keyword in keywords:
            if keyword in response:
                result[category] = 1
                found = True
    
    if not found:
        result["It hasn’t helped me"] = 1
    
    return result

# Buscar la pregunta "How has the virtual modality helped you in learning in your career?"
learning_help_df = df_cleaned[df_cleaned['Unnamed: 1'] == 'How has the virtual modality helped you in learning in your career? '].copy()

# Verificar si hay datos para esta pregunta
if learning_help_df.empty:
    print("No se encontraron respuestas para la pregunta: 'How has the virtual modality helped you in learning in your career?'")
else:
    learning_help_result_df = pd.DataFrame({'Student_ID': [student_ids[col] for col in learning_help_df.columns[2:]]})

    for i, response in enumerate(learning_help_df.values[0][2:]):
        if pd.notna(response):
            classified_help = classify_learning_help(response)
            for category, mentioned in classified_help.items():
                learning_help_result_df.loc[i, category] = mentioned

    # Guardar el CSV si hay datos
    learning_help_result_df.to_csv('learning_help.csv', index=False)
    print("Archivo CSV de cómo la modalidad virtual ayudó generado con éxito.")
