import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo combinado
df = pd.read_csv('combined_data.csv')

# Plataformas y motivación
platforms = ['Microsoft Teams', 'Zoom', 'Moodle', 'Google Classroom', 'Youtube']
motivation_column = 'Response'  # Columna de la motivación

# Filtrar datos
platforms_motivation_df = df.melt(id_vars=[motivation_column], value_vars=platforms)

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.countplot(data=platforms_motivation_df, x='variable', hue=motivation_column)
plt.title('Impacto de las plataformas usadas en la motivación')
plt.xlabel('Plataformas')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.show()
