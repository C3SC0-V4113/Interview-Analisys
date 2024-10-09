import pandas as pd

# Cargar el archivo Excel
excel_file = 'INTERVIEW.xlsx'
xls = pd.ExcelFile(excel_file)

# Leer la hoja de Excel, a partir de la fila 4 (ajusta esto si es necesario)
df_cleaned = pd.read_excel(xls, sheet_name='Sheet1', header=4)

# Mostrar las primeras filas para ver la estructura del archivo
print("Primeras filas del archivo Excel:\n")
print(df_cleaned.head())

# Mostrar las columnas disponibles en el archivo
print("\nColumnas en el archivo Excel:\n")
print(df_cleaned.columns)

# Mostrar las preguntas (columna 'Unnamed: 1') y verificar si están correctamente formateadas
print("\nPreguntas en la columna 'Unnamed: 1':\n")
print(df_cleaned['Unnamed: 1'].unique())
