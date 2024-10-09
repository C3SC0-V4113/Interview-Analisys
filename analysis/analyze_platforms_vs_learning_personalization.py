import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo combinado
df = pd.read_csv('combined_data.csv')

# Plataformas y personalización del aprendizaje
platforms = ['Microsoft Teams', 'Zoom', 'Moodle', 'Google Classroom', 'Youtube']
personalization_column = 'Sentiment'

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.countplot(data=df.melt(id_vars=[personalization_column], value_vars=platforms), x='variable', hue=personalization_column)
plt.title('Relación entre plataformas usadas y personalización del aprendizaje')
plt.xlabel('Plataformas')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.show()
