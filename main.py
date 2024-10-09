import subprocess
import sys

# Obtener el intérprete de Python actual
python_executable = sys.executable

# Lista de scripts a ejecutar
scripts = [
    'normalize_platforms.py',
    'normalize_positive_aspects.py',
    'normalize_limitations.py',
    'normalize_learning_help.py',
    'normalize_improvements.py',
    'normalize_english_confidence.py',
    #'normalize_personalized_learning.py'
    'normalize_yes_no_abstention.py',
    'normalize_sentiment_analysis.py'
]

# Ejecutar cada script en la lista usando el intérprete de Python correcto
for script in scripts:
    print(f"Ejecutando {script} con {python_executable}...")
    subprocess.run([python_executable, script], check=True)
    print(f"{script} ejecutado con éxito.\n")

print("Todos los scripts han sido ejecutados correctamente.")