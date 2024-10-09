import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo combinado
df = pd.read_csv('combined_data.csv')

# Aspectos positivos y motivación
positive_aspects = ['Flexibility', 'Convenience', 'Accessibility', 'Interactivity']
motivation_column = 'Response'

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.countplot(data=df.melt(id_vars=[motivation_column], value_vars=positive_aspects), x='variable', hue=motivation_column)
plt.title('Relación entre la motivación y los aspectos positivos')
plt.xlabel('Aspectos Positivos')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.show()
