import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos combinados
df = pd.read_csv('combined_data.csv')

# Crear una columna que cuente cuántas plataformas usa cada estudiante
df['Total_Platforms_Used'] = df[['Microsoft Teams', 'Moodle', 'Zoom', 'Google Classroom', 'Youtube', 'U-Virtual', 'Cambridge', 'E-Biblioteca']].sum(axis=1)

# Filtrar las columnas relevantes
df_filtered = df[['Total_Platforms_Used', 'Better or improved conversation skills']]

# Crear gráfico de dispersión
plt.figure(figsize=(8,6))
sns.scatterplot(data=df_filtered, x='Total_Platforms_Used', y='Better or improved conversation skills')
plt.title('Relación entre uso de múltiples plataformas y mejora de habilidades de conversación en inglés')
plt.xlabel('Número de plataformas usadas')
plt.ylabel('Mejora en habilidades de conversación')
plt.show()
