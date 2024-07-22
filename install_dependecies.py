import subprocess  # Importa el módulo subprocess para ejecutar comandos del sistema
import sys         # Importa el módulo sys para interactuar con el intérprete de Python

def install_requirements():
    try:
        # Intenta ejecutar el comando para instalar los paquetes listados en requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except Exception as e:
        # Si ocurre un error durante la instalación, se captura y se imprime un mensaje de error
        print(f"An error occurred: {e}")

# Esta condición verifica si el script está siendo ejecutado directamente
if __name__ == "__main__":
    # Si es así, llama a la función install_requirements para instalar los paquetes
    install_requirements()