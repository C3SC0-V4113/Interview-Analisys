import pandas as pd
from textblob import TextBlob

# Cargar el archivo Excel
excel_file = 'INTERVIEW.xlsx'
xls = pd.ExcelFile(excel_file)

# Leer la hoja de Excel
df_cleaned = pd.read_excel(xls, sheet_name='Sheet1', header=4)

# Imprimir las columnas para verificar
print("Columnas disponibles en el archivo Excel:")
print(df_cleaned.columns)

# Generar un ID único para cada estudiante
student_ids = {col: f'STUD_{i+1}' for i, col in enumerate(df_cleaned.columns[3:])}

def classify_sentiment(response):
    response = response.lower() if pd.notna(response) else ""
    sentiment = TextBlob(response).sentiment.polarity

    if sentiment > 0.5:
        return "Positive"
    elif sentiment < -0.5:
        return "Negative"
    else:
        return "Neutral"

# Preguntas de análisis de sentimientos
sentiment_analysis_questions = [
    'How do you consider your general experience with the use of virtual platforms?',
    'How has the virtual modality helped you in learning in your career? ',
    'How has the use of virtual platforms influenced your confidence when communicating in English? ',
    'To what extent do you feel that virtual platforms allow you to personalize your learning according to your pace, needs and time? '
]

# Procesar cada pregunta
for question in sentiment_analysis_questions:
    # Aquí utilizamos `iloc` para acceder a la columna 1 donde están las preguntas
    question_df = df_cleaned[df_cleaned.iloc[:, 1] == question].copy()

    # Verificar si hay datos
    if question_df.empty:
        print(f"No se encontraron respuestas para la pregunta: '{question}'")
    else:
        # Crear DataFrame para almacenar resultados
        sentiment_df = pd.DataFrame({'Student_ID': [student_ids[col] for col in question_df.columns[3:]]})

        # Clasificar las respuestas
        for i, response in enumerate(question_df.iloc[0, 3:]):
            sentiment_df.loc[i, 'Sentiment'] = classify_sentiment(response)

        # Guardar el archivo CSV con el nombre de la pregunta
        csv_filename = f"sentiment_analysis_{question.strip().replace(' ', '_').replace('?', '')}.csv"
        sentiment_df.to_csv(csv_filename, index=False)
        print(f"Archivo CSV generado para la pregunta: '{question}'")
