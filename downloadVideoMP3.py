import yt_dlp
from moviepy.editor import *

# Función para descargar el video de YouTube
def downloadVideo(url, output_path='video.mp4'):
    ydl_opts = {
        # 'format': 'best',
        'format': 'bestvideo+bestaudio',
        'outtmpl': output_path,
        'merge_output_format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        # Descargar solo si no existe el archivo
        # if not os.path.exists(output_path):
    
    print(f'Descargado: {output_path}')
    return output_path

# Función para convertir MP4 a MP3
def convertMP4toMP3(mp4_path, mp3_path='audio.mp3'):
    video = VideoFileClip(mp4_path)
    audio = video.audio
    audio.write_audiofile(mp3_path)
    
    print(f'Convertido: {mp3_path}')
    # return mp3_path

# URL del video de YouTube
url = 'https://youtu.be/mbAPCtZirD4?si=NZIoGDykRHGgud_K'

# Ruta de salida para el video descargado y el audio convertido
video_path = 'Video/video.mp4'
audio_path = 'Video/audio.mp3'

# Descargar el video de YouTube
downloaded_video_path = downloadVideo(url, video_path)

# Convertir el video descargado a MP3 solo si existe
if os.path.exists(downloaded_video_path):
    convertMP4toMP3(downloaded_video_path, audio_path)
else:
    print(f'El archivo {downloaded_video_path} no existe.')