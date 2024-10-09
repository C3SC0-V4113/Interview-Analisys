import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo combinado
df = pd.read_csv('combined_data.csv')

# Relacionar plataformas con problemas técnicos
platforms = ['Microsoft Teams', 'Zoom', 'Moodle', 'Google Classroom', 'Youtube']
technical_issues = 'Technical issues'

# Filtrar datos
platforms_tech_issues_df = df.melt(id_vars=[technical_issues], value_vars=platforms)

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.countplot(data=platforms_tech_issues_df, x='variable', hue=technical_issues)
plt.title('Relación entre plataformas usadas y problemas técnicos reportados')
plt.xlabel('Plataformas')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.show()
