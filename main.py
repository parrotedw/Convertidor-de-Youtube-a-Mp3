import yt_dlp
import os
print("__________________________________________________________________")
print("Convertidor mp3 de Parrot")
print("__________________________________________________________________")
    

def hook(d):
    if d['status'] == 'finished':
        print(f"\nDescarga completada: {d['filename']}")

def descargar_video(url, ruta_salida='descargas'):
    # Crear el directorio si no existe
    if not os.path.exists(ruta_salida):
        os.makedirs(ruta_salida)
    
    print(f"Ruta de salida: {ruta_salida}")
    
    # Opciones para yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(ruta_salida, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [hook],  # Para ver la descarga en progreso
    }

    print("Iniciando descarga...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        archivo_descargado = os.path.join(ruta_salida, f"{info_dict['title']}.mp3")
        print(f"Archivo descargado: {archivo_descargado}")

    return archivo_descargado

def main():
    while True:
        
        url = input("Introduce la URL del video de YouTube: ")
        print("Descargando video...")
        archivo_mp3 = descargar_video(url)
        print(f"Archivo MP3 guardado en: {archivo_mp3}")

if __name__ == "__main__":
    main()
