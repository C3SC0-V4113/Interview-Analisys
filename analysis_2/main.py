import subprocess
import sys

# Obtener el intérprete de Python actual
python_executable = sys.executable

# Lista de scripts a ejecutar
scripts = [
    'analysis_2/analyze_technical_issues_vs_technology_adaptation.py',
    'analysis_2/analyze_flexibility_vs_motivation.py',
    'analysis_2/analyze_platforms_vs_english_conversation_skills.py',
    'analysis_2/analyze_interactivity_vs_sentiment.py',
    'analysis_2/analyze_google_classroom_vs_time_management.py',
    'analysis_2/analyze_time_management_vs_microsoft_teams.py',
    'analysis_2/analyze_time_management_vs_u_virtual.py'
]

# Ejecutar cada script en la lista usando el intérprete de Python correcto
for script in scripts:
    print(f"Ejecutando {script} con {python_executable}...")
    subprocess.run([python_executable, script], check=True)
    print(f"{script} ejecutado con éxito.\n")

print("Todos los scripts han sido ejecutados correctamente.")