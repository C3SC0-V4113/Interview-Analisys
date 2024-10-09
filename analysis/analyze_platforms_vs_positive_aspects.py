import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo combinado
df = pd.read_csv('combined_data.csv')

# Plataformas y aspectos positivos
platforms = ['Microsoft Teams', 'Zoom', 'Moodle', 'Google Classroom', 'Youtube']
positive_aspects = ['Flexibility', 'Convenience', 'Accessibility', 'Interactivity']

# Correlación entre plataformas y aspectos positivos
plt.figure(figsize=(12, 8))
sns.heatmap(df[platforms + positive_aspects].corr(), annot=True, cmap='coolwarm')
plt.title('Correlación entre plataformas usadas y aspectos positivos')
plt.show()
