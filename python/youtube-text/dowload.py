from properties import LINK_URL, ARQUIVO, EXTENCAO
import yt_dlp as yt

"""Download do Audio/Video"""
def download_audio(url: str) -> None:
    youtube_info = {
        'format': 'bestaudio/best',
        'outtmpl': f'{ARQUIVO}',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': f'{EXTENCAO}',
            'preferredquality': '192'
        }]
    }

    with yt.YoutubeDL(youtube_info) as ydl:
        ydl.download([url])

download_audio(LINK_URL)
