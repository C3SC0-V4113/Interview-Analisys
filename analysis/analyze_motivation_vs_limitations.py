import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo combinado
df = pd.read_csv('combined_data.csv')

# Limitaciones y motivación
limitations_columns = ['Technical issues', 'Distractions', 'Lack of feedback', 'Not accessible for all']
motivation_column = 'Response'

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.countplot(data=df.melt(id_vars=[motivation_column], value_vars=limitations_columns), x='variable', hue=motivation_column)
plt.title('Comparación entre motivación y limitaciones')
plt.xlabel('Limitaciones')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.show()
