import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos combinados
df = pd.read_csv('combined_data.csv')

# Filtrar las columnas relevantes
df_filtered = df[['Google Classroom', 'Have a better time management']]

# Crear gráfico de barras
plt.figure(figsize=(8,6))
sns.countplot(data=df_filtered, x='Google Classroom', hue='Have a better time management')
plt.title('Relación entre el uso de Google Classroom y la mejora en la gestión del tiempo')
plt.xlabel('Google Classroom (Usado)')
plt.ylabel('Cantidad')
plt.show()
