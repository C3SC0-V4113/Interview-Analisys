import subprocess
import sys

# Obtener el intérprete de Python actual
python_executable = sys.executable

# Lista de scripts a ejecutar
scripts = [
    'analysis/analyze_platforms_vs_technical_issues.py',
    'analysis/analyze_platforms_vs_motivation.py',
    'analysis/analyze_platforms_vs_positive_aspects.py',
    'analysis/analyze_motivation_vs_positive_aspects.py',
    'analysis/analyze_platforms_vs_english_confidence.py',
    'analysis/analyze_platforms_vs_learning_personalization.py',
    'analysis/analyze_limitations_vs_general_sentiment.py',
    'analysis/analyze_motivation_vs_limitations.py',
    'analysis/analyze_self_management_vs_platforms.py',
    'analysis/analyze_platforms_vs_general_sentiment.py'
]

# Ejecutar cada script en la lista usando el intérprete de Python correcto
for script in scripts:
    print(f"Ejecutando {script} con {python_executable}...")
    subprocess.run([python_executable, script], check=True)
    print(f"{script} ejecutado con éxito.\n")

print("Todos los scripts han sido ejecutados correctamente.")