import pandas as pd

# Cargar el archivo Excel
excel_file = 'INTERVIEW.xlsx'
xls = pd.ExcelFile(excel_file)

df_cleaned = pd.read_excel(xls, sheet_name='Sheet1', header=4)

df_cleaned.columns = ['Category', 'Unnamed: 1', 'Empty'] + [f'Student_{i}' for i in range(1, len(df_cleaned.columns)-2)]
df_cleaned = df_cleaned.drop(columns=['Empty'])

student_ids = {f'Student_{i}': f'STUD_{i}' for i in range(1, len(df_cleaned.columns[2:])+1)}

def classify_improvements(response):
    response = response.lower()
    improvements = {
        "More interactivity": ["interaction", "participation", "engagement", "interactive"],
        "Better technical support": ["technical support", "help", "issues"],
        "Better inclusivity": ["inclusivity", "accessibility", "disability"],
        "Anti cheats": ["cheating", "anti-cheat", "proctoring"],
        "Grammar, Vocabulary, Pronunciation": ["grammar", "vocabulary", "pronunciation"]
    }
    
    result = {improvement: 0 for improvement in improvements}
    
    found = False
    for improvement, keywords in improvements.items():
        for keyword in keywords:
            if keyword in response:
                result[improvement] = 1
                found = True
    
    if not found:
        result["Other"] = 1
    
    return result

# Buscar la pregunta "What are the aspects that could be improved in these virtual platforms?"
improvements_df = df_cleaned[df_cleaned['Unnamed: 1'] == 'What are the aspects that could be improved in these virtual platforms? '].copy()

# Verificar si hay datos para esta pregunta
if improvements_df.empty:
    print("No se encontraron respuestas para la pregunta: 'What are the aspects that could be improved in these virtual platforms?'")
else:
    improvements_result_df = pd.DataFrame({'Student_ID': [student_ids[col] for col in improvements_df.columns[2:]]})

    for i, response in enumerate(improvements_df.values[0][2:]):
        if pd.notna(response):
            classified_improvements = classify_improvements(response)
            for improvement, mentioned in classified_improvements.items():
                improvements_result_df.loc[i, improvement] = mentioned

    # Guardar el CSV si hay datos
    improvements_result_df.to_csv('improvements.csv', index=False)
    print("Archivo CSV de aspectos a mejorar generado con éxito.")
