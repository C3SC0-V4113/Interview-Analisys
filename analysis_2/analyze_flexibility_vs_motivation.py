import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos combinados
df = pd.read_csv('combined_data.csv')

# Filtrar las columnas relevantes
df_filtered = df[['Flexibility', 'Response']]

# Crear gráfico de barras
plt.figure(figsize=(8,6))
sns.countplot(data=df_filtered, x='Flexibility', hue='Response')
plt.title('Impacto de la flexibilidad en la motivación')
plt.xlabel('Flexibilidad')
plt.ylabel('Cantidad')
plt.show()
