import yt_dlp
import os
import subprocess
import platform
import shutil

def open_folder(path):
    system = platform.system()
    if system == "Windows":
        subprocess.run(["explorer", os.path.realpath(path)])
    elif system == "Darwin":
        subprocess.run(["open", path])
    else:
        subprocess.run(["xdg-open", path])

def find_browser():
    browsers = ['firefox', 'chrome', 'edge', 'brave', 'opera']
    for browser in browsers:
        if shutil.which(browser):
            print(f"Найден браузер: {browser}")
            return browser
    print("Браузер не найден, используем Firefox по умолчанию")
    return 'firefox'
#рабоает криво ? вроде как?


def download_wav_from_youtube(url):
    download_dir = "downloads"
    os.makedirs(download_dir, exist_ok=True)

    ffmpeg_dir = os.path.join(os.getcwd(), 'bin')
    browser = find_browser()

    ydl_opts = {
        'format': 'bestaudio/best',
        'cookiesfrombrowser': (browser,),
        'ffmpeg_location': ffmpeg_dir,
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
    }

    print("Скачиваю и сохраняю в .wav...")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Готово. Открываю папку...")
        open_folder(download_dir)
    except Exception as e:
        print(f"Ошибка: {e}")

youtube_link = input("Вставь ссылку на YouTube: ")
download_wav_from_youtube(youtube_link)
