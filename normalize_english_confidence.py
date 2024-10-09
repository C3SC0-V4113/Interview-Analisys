import pandas as pd
from textblob import TextBlob

# Cargar el archivo Excel
excel_file = 'INTERVIEW.xlsx'
xls = pd.ExcelFile(excel_file)

df_cleaned = pd.read_excel(xls, sheet_name='Sheet1', header=4)

df_cleaned.columns = ['Category', 'Unnamed: 1', 'Empty'] + [f'Student_{i}' for i in range(1, len(df_cleaned.columns)-2)]
df_cleaned = df_cleaned.drop(columns=['Empty'])

student_ids = {f'Student_{i}': f'STUD_{i}' for i in range(1, len(df_cleaned.columns[2:])+1)}

def classify_english_confidence(response):
    response = response.lower()
    sentiment = TextBlob(response).sentiment.polarity
    if sentiment < 0:
        return {"It hasn’t improved": 1, "Better or improved conversation skills": 0, "Better or improved writing skills": 0, "Better learning skills": 0}
    
    confidence_categories = {
        "Better or improved conversation skills": ["conversation", "speaking", "talking"],
        "Better or improved writing skills": ["writing", "composing"],
        "Better learning skills": ["learning", "skills"]
    }
    
    result = {category: 0 for category in confidence_categories}
    
    found = False
    for category, keywords in confidence_categories.items():
        for keyword in keywords:
            if keyword in response:
                result[category] = 1
                found = True
    
    if not found:
        result["It hasn’t improved"] = 1
    
    return result

# Buscar la pregunta "How has the use of virtual platforms influenced your confidence when communicating in English?"
english_confidence_df = df_cleaned[df_cleaned['Unnamed: 1'] == 'How has the use of virtual platforms influenced your confidence when communicating in English? '].copy()

# Verificar si hay datos para esta pregunta
if english_confidence_df.empty:
    print("No se encontraron respuestas para la pregunta: 'How has the use of virtual platforms influenced your confidence when communicating in English?'")
else:
    english_confidence_result_df = pd.DataFrame({'Student_ID': [student_ids[col] for col in english_confidence_df.columns[2:]]})

    for i, response in enumerate(english_confidence_df.values[0][2:]):
        if pd.notna(response):
            classified_confidence = classify_english_confidence(response)
            for category, mentioned in classified_confidence.items():
                english_confidence_result_df.loc[i, category] = mentioned

    # Guardar el CSV si hay datos
    english_confidence_result_df.to_csv('english_confidence.csv', index=False)
    print("Archivo CSV de confianza en inglés generado con éxito.")
