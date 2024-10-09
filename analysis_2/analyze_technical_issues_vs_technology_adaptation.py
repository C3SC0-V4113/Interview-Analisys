import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos combinados
df = pd.read_csv('combined_data.csv')

# Filtrar las columnas relevantes
df_filtered = df[['Technical issues', 'Learn to adapt and use technology']]

# Crear gráfico de barras
plt.figure(figsize=(8,6))
sns.countplot(data=df_filtered, x='Technical issues', hue='Learn to adapt and use technology')
plt.title('Relación entre problemas técnicos y la adaptación a la tecnología')
plt.xlabel('Problemas técnicos')
plt.ylabel('Cantidad')
plt.show()
