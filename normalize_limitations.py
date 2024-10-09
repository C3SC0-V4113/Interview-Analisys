import pandas as pd

# Cargar el archivo Excel
excel_file = 'INTERVIEW.xlsx'
xls = pd.ExcelFile(excel_file)

# Leer la hoja de Excel
df_cleaned = pd.read_excel(xls, sheet_name='Sheet1', header=4)

df_cleaned.columns = ['Category', 'Unnamed: 1', 'Empty'] + [f'Student_{i}' for i in range(1, len(df_cleaned.columns)-2)]
df_cleaned = df_cleaned.drop(columns=['Empty'])

student_ids = {f'Student_{i}': f'STUD_{i}' for i in range(1, len(df_cleaned.columns[2:])+1)}

def classify_limitations(response):
    response = response.lower()
    limitations = {
        "Distractions": ["distraction", "distracted", "focus", "concentration"],
        "No human interaction": ["face to face", "interaction", "social", "no human"],
        "Lack of feedback": ["feedback", "doubts", "clarify"],
        "Technical issues": ["internet", "connection", "audio", "technical", "software"],
        "Not accessible for all": ["devices", "smartphone", "tablet", "not accessible"],
        "Hard to learn real use cases": ["real", "cases", "hands-on"],
        "None": ["none", "no limitations", "nothing"]
    }
    
    result = {limitation: 0 for limitation in limitations}
    
    found = False
    for limitation, keywords in limitations.items():
        for keyword in keywords:
            if keyword in response:
                result[limitation] = 1
                found = True
    
    if not found:
        result["None"] = 1
    
    return result

# Buscar la pregunta "What limitations do you find in this modality?"
limitations_df = df_cleaned[df_cleaned['Unnamed: 1'] == 'What limitations do you find in this modality? '].copy()

# Verificar si hay datos para esta pregunta
if limitations_df.empty:
    print("No se encontraron respuestas para la pregunta: 'What limitations do you find in this modality?'")
else:
    limitations_result_df = pd.DataFrame({'Student_ID': [student_ids[col] for col in limitations_df.columns[2:]]})

    for i, response in enumerate(limitations_df.values[0][2:]):
        if pd.notna(response):
            classified_limitations = classify_limitations(response)
            for limitation, mentioned in classified_limitations.items():
                limitations_result_df.loc[i, limitation] = mentioned

    # Guardar el CSV si hay datos
    limitations_result_df.to_csv('limitations_found.csv', index=False)
    print("Archivo CSV de limitaciones generado con éxito.")
