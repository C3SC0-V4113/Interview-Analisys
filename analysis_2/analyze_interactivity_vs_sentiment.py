import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos combinados
df = pd.read_csv('combined_data.csv')

# Filtrar las columnas relevantes
df_filtered = df[['Interactivity', 'Sentiment']]

# Crear gráfico de barras
plt.figure(figsize=(8,6))
sns.countplot(data=df_filtered, x='Interactivity', hue='Sentiment')
plt.title('Relación entre la interactividad de las plataformas y el sentimiento general')
plt.xlabel('Interactividad')
plt.ylabel('Cantidad')
plt.show()
