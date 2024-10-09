import pandas as pd

# Cargar el archivo Excel
excel_file = 'INTERVIEW.xlsx'
xls = pd.ExcelFile(excel_file)

# Leer la hoja de Excel, a partir de la fila 4 (ajusta esto si es necesario)
df_cleaned = pd.read_excel(xls, sheet_name='Sheet1', header=4)

# Renombrar las columnas para reflejar mejor los datos
df_cleaned.columns = ['Category', 'Unnamed: 1', 'Empty'] + [f'Student_{i}' for i in range(1, len(df_cleaned.columns)-2)]
df_cleaned = df_cleaned.drop(columns=['Empty'])

# Generar un ID único para cada estudiante
student_ids = {f'Student_{i}': f'STUD_{i}' for i in range(1, len(df_cleaned.columns[2:])+1)}

# Función para clasificar plataformas
def classify_platforms(response):
    # Asegurarnos de que no falle si hay valores vacíos
    response = response.lower() if pd.notna(response) else ""
    
    platforms = {
        "Microsoft Teams": ["teams", "microsoft teams"],
        "Moodle": ["moodle"],
        "Zoom": ["zoom"],
        "Google Classroom": ["classroom", "google classroom"],
        "Youtube": ["youtube"],
        "U-Virtual": ["u-virtual", "virtual"],
        "Cambridge": ["cambridge"],
        "E-Biblioteca": ["biblioteca", "e-biblioteca"],
        "Other": []
    }
    
    # Inicializar las plataformas como 0 (no usadas)
    result = {platform: 0 for platform in platforms}
    
    # Revisar si alguna de las plataformas aparece en la respuesta
    for platform, keywords in platforms.items():
        for keyword in keywords:
            if keyword in response:
                result[platform] = 1
    
    return result

# Obtener las respuestas a la pregunta "What platforms have you used for learning?"
platform_question_df = df_cleaned[df_cleaned['Unnamed: 1'] == 'What platforms have you used for learning? ']

# Verificar si hay datos para esta pregunta
if platform_question_df.empty:
    print("No se encontraron respuestas para la pregunta: 'What platforms have you used for learning?'")
else:
    # Crear un DataFrame para almacenar los resultados
    platforms_df = pd.DataFrame({'Student_ID': [student_ids[col] for col in platform_question_df.columns[2:]]})
    
    # Aplicar la función de clasificación a cada respuesta de los estudiantes
    for i, response in enumerate(platform_question_df.iloc[0, 2:]):
        classified_platforms = classify_platforms(response)
        for platform, used in classified_platforms.items():
            platforms_df.loc[i, platform] = used

    # Guardar el CSV con los resultados, incluso si hay respuestas vacías
    platforms_df.to_csv('platforms_used.csv', index=False)
    print("Archivo CSV de plataformas generado con éxito.")
