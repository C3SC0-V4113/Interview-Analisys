import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo combinado
df = pd.read_csv('combined_data.csv')

# Autogestión y plataformas
platforms = ['Microsoft Teams', 'Zoom', 'Moodle', 'Google Classroom', 'Youtube']
self_management_column = 'Learn to be self-disciplined'

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.countplot(data=df.melt(id_vars=[self_management_column], value_vars=platforms), x='variable', hue=self_management_column)
plt.title('Relación entre autogestión y plataformas usadas')
plt.xlabel('Plataformas')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.show()
