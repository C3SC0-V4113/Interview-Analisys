import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo combinado
df = pd.read_csv('combined_data.csv')

# Plataformas y sentimiento general
platforms = ['Microsoft Teams', 'Zoom', 'Moodle', 'Google Classroom', 'Youtube']
sentiment_column = 'Sentiment'

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.countplot(data=df.melt(id_vars=[sentiment_column], value_vars=platforms), x='variable', hue=sentiment_column)
plt.title('Relación entre plataformas usadas y sentimiento general')
plt.xlabel('Plataformas')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.show()
