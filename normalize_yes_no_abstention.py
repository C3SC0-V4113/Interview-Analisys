import pandas as pd

# Cargar el archivo Excel
excel_file = 'INTERVIEW.xlsx'
xls = pd.ExcelFile(excel_file)

# Leer la hoja de Excel
df_cleaned = pd.read_excel(xls, sheet_name='Sheet1', header=4)

# Imprimir las columnas para verificar
print("Columnas disponibles en el archivo Excel:")
print(df_cleaned.columns)

# Crear un diccionario con los IDs de los estudiantes
student_ids = {col: f'STUD_{i+1}' for i, col in enumerate(df_cleaned.columns[3:])}

def classify_yes_no_abstention(response):
    response = response.lower() if pd.notna(response) else "abstention"
    
    if "yes" in response:
        return "Yes"
    elif "no" in response:
        return "No"
    else:
        return "Abstention"

# Preguntas Yes/No/Abstention que queremos procesar
yes_no_questions = [
    'Have you previously taken virtual subjects before this semester? ',
    'Do you consider that technical problems can influence the development of your learning? ',
    'Do you feel motivated in this type of modality?'
]

# Procesar cada pregunta
for question in yes_no_questions:
    # Aquí utilizamos `iloc` para acceder a la columna 1
    question_df = df_cleaned[df_cleaned.iloc[:, 1] == question].copy()

    # Verificar si hay datos
    if question_df.empty:
        print(f"No se encontraron respuestas para la pregunta: '{question}'")
    else:
        # Crear DataFrame para almacenar resultados
        yes_no_df = pd.DataFrame({'Student_ID': [student_ids[col] for col in question_df.columns[3:]]})

        # Clasificar respuestas
        for i, response in enumerate(question_df.iloc[0, 3:]):  # Ajustamos el índice para respuestas
            yes_no_df.loc[i, 'Response'] = classify_yes_no_abstention(response)

        # Guardar el archivo CSV con el nombre de la pregunta
        csv_filename = f"yes_no_abstention_{question.strip().replace(' ', '_').replace('?', '')}.csv"
        yes_no_df.to_csv(csv_filename, index=False)
        print(f"Archivo CSV generado para la pregunta: '{question}'")
