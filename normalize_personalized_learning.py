import pandas as pd
from textblob import TextBlob

# Cargar el archivo Excel
excel_file = 'INTERVIEW.xlsx'
xls = pd.ExcelFile(excel_file)

df_cleaned = pd.read_excel(xls, sheet_name='Sheet1', header=4)

df_cleaned.columns = ['Category', 'Unnamed: 1', 'Empty'] + [f'Student_{i}' for i in range(1, len(df_cleaned.columns)-2)]
df_cleaned = df_cleaned.drop(columns=['Empty'])

student_ids = {f'Student_{i}': f'STUD_{i}' for i in range(1, len(df_cleaned.columns[2:])+1)}

def classify_personalized_learning(response):
    sentiment = TextBlob(response).sentiment.polarity
    if sentiment > 0.5:
        return "It has helped a lot"
    elif 0 < sentiment <= 0.5:
        return "It has helped"
    elif -0.5 < sentiment <= 0:
        return "It hasn’t helped much"
    else:
        return "It hasn’t helped at all"

# Buscar la pregunta "To what extent do you feel that virtual platforms allow you to personalize your learning according to your pace, needs and time?"
personalized_learning_df = df_cleaned[df_cleaned['Unnamed: 1'] == 'To what extent do you feel that virtual platforms allow you to personalize your learning according to your pace, needs and time? '].copy()

# Verificar si hay datos para esta pregunta
if personalized_learning_df.empty:
    print("No se encontraron respuestas para la pregunta: 'To what extent do you feel that virtual platforms allow you to personalize your learning according to your pace, needs and time?'")
else:
    personalized_learning_result_df = pd.DataFrame({'Student_ID': [student_ids[col] for col in personalized_learning_df.columns[2:]]})

    for i, response in enumerate(personalized_learning_df.values[0][2:]):
        if pd.notna(response):
            result = classify_personalized_learning(response)
            personalized_learning_result_df.loc[i, 'Personalized Learning'] = result

    # Guardar el CSV si hay datos
    personalized_learning_result_df.to_csv('personalized_learning.csv', index=False)
    print("Archivo CSV de personalización del aprendizaje generado con éxito.")
