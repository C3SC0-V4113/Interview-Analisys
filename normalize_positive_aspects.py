import pandas as pd

# Cargar el archivo Excel
excel_file = 'INTERVIEW.xlsx'
xls = pd.ExcelFile(excel_file)

# Leer la hoja de Excel
df_cleaned = pd.read_excel(xls, sheet_name='Sheet1', header=4)

df_cleaned.columns = ['Category', 'Unnamed: 1', 'Empty'] + [f'Student_{i}' for i in range(1, len(df_cleaned.columns)-2)]
df_cleaned = df_cleaned.drop(columns=['Empty'])

student_ids = {f'Student_{i}': f'STUD_{i}' for i in range(1, len(df_cleaned.columns[2:])+1)}

def classify_positive_aspects(response):
    response = response.lower()
    aspects = {
        "Flexibility": ["flexibility", "schedule", "anytime", "time", "home"],
        "Availability": ["available", "always", "anytime"],
        "Adaptability": ["adapt", "adaptability", "customize"],
        "Accessibility": ["accessibility", "easy access", "access"],
        "Convenience": ["convenient", "convenience", "easy to use", "simple"],
        "Interactivity": ["interactive", "interaction", "engagement"],
        "Other": []
    }
    
    result = {aspect: 0 for aspect in aspects}
    
    found = False
    for aspect, keywords in aspects.items():
        for keyword in keywords:
            if keyword in response:
                result[aspect] = 1
                found = True
    
    if not found:
        result["Other"] = 1
    
    return result

positive_aspects_df = df_cleaned[df_cleaned['Unnamed: 1'] == 'What positive aspects have you found in the use of virtual platforms?'].copy()

aspects_df = pd.DataFrame({'Student_ID': [student_ids[col] for col in positive_aspects_df.columns[2:]]})

for i, response in enumerate(positive_aspects_df.values[0][2:]):
    if pd.notna(response):
        classified_aspects = classify_positive_aspects(response)
        for aspect, mentioned in classified_aspects.items():
            aspects_df.loc[i, aspect] = mentioned

aspects_df.to_csv('positive_aspects.csv', index=False)
print("Archivo CSV de aspectos positivos generado con éxito.")
