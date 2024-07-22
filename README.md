# Proyecto de Descarga de Video y Audio

Este proyecto utiliza `yt_dlp` y `moviepy` para descargar y procesar videos y audios de YouTube.

## Requisitos

- Python 3.x
- Paquetes de Python listados en `requirements.txt`
- `ffmpeg` instalado y accesible desde la línea de comandos

## Instalación de ffmpeg

### Windows
1. Ve a la [página oficial de FFmpeg](https://ffmpeg.org/download.html).
2. Descarga la versión adecuada para Windows.
3. Extrae el contenido del archivo zip descargado.
4. Copia la ruta de la carpeta `bin` dentro del directorio extraído (por ejemplo, `C:\ffmpeg\bin`).
5. Agrega esta ruta a las variables de entorno del sistema:
   - Abre el Panel de control.
   - Ve a Sistema y seguridad > Sistema > Configuración avanzada del sistema.
   - Haz clic en "Variables de entorno".
   - En "Variables del sistema", busca y selecciona la variable `Path`, luego haz clic en "Editar".
   - Agrega una nueva entrada con la ruta copiada (`C:\ffmpeg\bin`).
   - Guarda y cierra todas las ventanas.

### macOS
1. Abre una terminal.
2. Si tienes Homebrew instalado, puedes instalar `ffmpeg` usando:
   ```sh
   brew install ffmpeg

### Linux
1. Abre una terminal.
2. En distribuciones basadas en Debian/Ubuntu, usa:
```
sudo apt update
sudo apt install ffmpeg
```
3. Para otras distribuciones, usa el administrador de paquetes correspondiente.

## Instalación de Dependencias de Python
Ejecuta el siguiente comando para instalar todas las dependencias de Python listadas en requirements.txt:

```
pip install -r requirements.txt
```

## Uso
```
python downloadVideoMP3.py
```
