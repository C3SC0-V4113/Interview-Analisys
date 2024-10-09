import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo combinado
df = pd.read_csv('combined_data.csv')

# Limitaciones y sentimiento general
limitations_columns = ['Technical issues', 'Distractions', 'Lack of feedback', 'Not accessible for all']
general_sentiment_column = 'Sentiment'

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.countplot(data=df.melt(id_vars=[general_sentiment_column], value_vars=limitations_columns), x='variable', hue=general_sentiment_column)
plt.title('Impacto de las limitaciones en la experiencia general')
plt.xlabel('Limitaciones')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.show()

