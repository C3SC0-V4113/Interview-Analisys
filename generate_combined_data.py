import pandas as pd

# Cargar todos los archivos CSV generados por los scripts de normalización
platforms_df = pd.read_csv('platforms_used.csv')
positive_aspects_df = pd.read_csv('positive_aspects.csv')
limitations_df = pd.read_csv('limitations_found.csv')
learning_help_df = pd.read_csv('learning_help.csv')
improvements_df = pd.read_csv('improvements.csv')
english_confidence_df = pd.read_csv('english_confidence.csv')
motivation_df = pd.read_csv('yes_no_abstention_Do_you_feel_motivated_in_this_type_of_modality.csv')
general_experience_df = pd.read_csv('sentiment_analysis_How_do_you_consider_your_general_experience_with_the_use_of_virtual_platforms.csv')

# Combinar los DataFrames utilizando `Student_ID` como clave
merged_df = platforms_df.merge(positive_aspects_df, on='Student_ID', how='outer')
merged_df = merged_df.merge(limitations_df, on='Student_ID', how='outer')
merged_df = merged_df.merge(learning_help_df, on='Student_ID', how='outer')
merged_df = merged_df.merge(improvements_df, on='Student_ID', how='outer')
merged_df = merged_df.merge(english_confidence_df, on='Student_ID', how='outer')
merged_df = merged_df.merge(motivation_df, on='Student_ID', how='outer')
merged_df = merged_df.merge(general_experience_df, on='Student_ID', how='outer')

# Verificar si los datos se combinaron correctamente
print("Datos combinados:")
print(merged_df.head())

# Guardar el DataFrame combinado en un archivo CSV
merged_df.to_csv('combined_data.csv', index=False)

print("Archivo 'combined_data.csv' generado con éxito.")
