from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_as_mp3(url, output_path='.'):
    # Download the YouTube video in the highest quality
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()

    # Download the audio stream (in the best possible format available)
    print(f"Downloading: {yt.title}")
    download_path = video.download(output_path=output_path)

    # Convert downloaded audio to MP3 format
    print(f"Converting to MP3...")
    audio = AudioSegment.from_file(download_path)
    mp3_path = os.path.splitext(download_path)[0] + '.mp3'
    audio.export(mp3_path, format='mp3')

    # Remove the original file (optional, if you want to keep only the MP3)
    os.remove(download_path)

    print(f"Download and conversion complete: {mp3_path}")

# Example Usage:
url = 'https://youtu.be/jcEKpP_B9qM?si=fhAwjVZFp8_gWR37'
download_youtube_as_mp3(url)
