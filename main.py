import yt_dlp
import os
import subprocess
import platform

def open_folder(path):
    system = platform.system()
    if system == "Windows":
        subprocess.run(["explorer", os.path.realpath(path)])
    elif system == "Darwin":
        subprocess.run(["open", path])
    else:
        subprocess.run(["xdg-open", path])

def download_wav_from_youtube(url, browser, format):
    download_dir = "downloads"
    os.makedirs(download_dir, exist_ok=True)

    ffmpeg_dir = os.path.join(os.getcwd(), 'bin')

    ydl_opts = {
        'format': 'bestaudio/best',
        'cookiesfrombrowser': (browser,),
        'ffmpeg_location': ffmpeg_dir,
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': format,
        }],
    }

    print("Скачиваю и сохраняю...")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Готово. Открываю папку...")
        open_folder(download_dir)
    except Exception as e:
        print(f"Ошибка: {e}")

youtube_link = input("Вставь ссылку на YouTube: ")
browser_name = input("Введи свой браузер (например: firefox, chrome, edge, opera, brave): ").strip().lower()
formatvideo = str(input("введите формат (mp3, wav): "))
download_wav_from_youtube(youtube_link, browser_name, formatvideo)
