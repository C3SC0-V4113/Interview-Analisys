import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos combinados
df = pd.read_csv('combined_data.csv')

# Filtrar las columnas relevantes
df_filtered = df[['U-Virtual', 'Have a better time management']]

# Crear gráfico de barras
plt.figure(figsize=(8,6))
sns.countplot(data=df_filtered, x='U-Virtual', hue='Have a better time management')
plt.title('Relación entre el uso de U-Virtual y la mejora en la gestión del tiempo')
plt.xlabel('U-Virtual (Usado)')
plt.ylabel('Cantidad')
plt.show()
