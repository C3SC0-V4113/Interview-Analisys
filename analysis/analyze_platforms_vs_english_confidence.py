import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo combinado
df = pd.read_csv('combined_data.csv')

# Plataformas y confianza en el inglés
platforms = ['Microsoft Teams', 'Zoom', 'Moodle', 'Google Classroom', 'Youtube']
confidence_columns = ['Better or improved conversation skills', 'Better or improved writing skills', 'Better learning skills']

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.heatmap(df[platforms + confidence_columns].corr(), annot=True, cmap='coolwarm')
plt.title('Correlación entre plataformas usadas y confianza en el uso del inglés')
plt.show()
