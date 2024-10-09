import pandas as pd

# Cargar los archivos CSV
platforms_df = pd.read_csv('platforms_used.csv')
positive_aspects_df = pd.read_csv('positive_aspects.csv')
limitations_df = pd.read_csv('limitations_found.csv')
general_experience_df = pd.read_csv('sentiment_analysis_How_do_you_consider_your_general_experience_with_the_use_of_virtual_platforms.csv')
motivation_df = pd.read_csv('yes_no_abstention_Do_you_feel_motivated_in_this_type_of_modality.csv')

# Combinar los datos en un DataFrame
merged_df = platforms_df.merge(positive_aspects_df, on='Student_ID', how='outer')
merged_df = merged_df.merge(limitations_df, on='Student_ID', how='outer')
merged_df = merged_df.merge(general_experience_df, on='Student_ID', how='outer')
merged_df = merged_df.merge(motivation_df, on='Student_ID', how='outer')

import seaborn as sns
import matplotlib.pyplot as plt

# Definir las plataformas y los aspectos positivos
platforms = ['Microsoft Teams', 'Zoom', 'Moodle', 'Google Classroom', 'Youtube']
positive_aspects = ['Flexibility', 'Convenience', 'Accessibility', 'Interactivity']

# Relación entre plataformas usadas y aspectos positivos
platforms_positive_aspects = merged_df[platforms + positive_aspects].melt(id_vars=platforms, value_vars=positive_aspects)

# Gráfico de correlación
plt.figure(figsize=(12, 8))
sns.heatmap(merged_df[platforms + positive_aspects].corr(), annot=True, cmap='coolwarm')
plt.title('Correlación entre plataformas usadas y aspectos positivos')
plt.show()



# Relación entre plataformas y el sentimiento general sobre las plataformas virtuales
plt.figure(figsize=(10, 6))

# Transformar el DataFrame para la visualización
sentiment_analysis_df = merged_df.melt(id_vars=['Student_ID', 'Sentiment'], value_vars=platforms)

# Crear gráfico
sns.countplot(data=sentiment_analysis_df, x='variable', hue='Sentiment')
plt.title('Relación entre plataformas usadas y sentimiento general sobre la experiencia virtual')
plt.xlabel('Plataforma')
plt.ylabel('Cantidad')
plt.show()



# Relación entre la motivación y las limitaciones encontradas
plt.figure(figsize=(10, 6))

# Filtrar estudiantes con limitaciones y sus respuestas de motivación
limitations_columns = limitations_df.columns[1:]  # Obtener las columnas de limitaciones
motivation_limitations_df = merged_df.melt(id_vars=['Student_ID', 'Response'], value_vars=limitations_columns)

# Crear gráfico
sns.countplot(data=motivation_limitations_df, x='variable', hue='Response')
plt.title('Relación entre la motivación y las limitaciones encontradas')
plt.xlabel('Limitaciones')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.show()
