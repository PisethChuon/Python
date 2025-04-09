from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def yt_to_mp3(yt_url, output_path='.'):
    try:
        yt = YouTube(yt_url)
        print(f"Downloading: {yt.title}")
        
        # Download the highest quality audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        downloaded_file = audio_stream.download(output_path=output_path)
        
        # Convert to .mp3 using moviepy
        base, ext = os.path.splitext(downloaded_file)
        mp3_file = f"{base}.mp3"
        
        audio_clip = AudioFileClip(downloaded_file)
        audio_clip.write_audiofile(mp3_file)
        audio_clip.close()

        # Optional: remove the original .mp4 audio
        os.remove(downloaded_file)

        print(f"Saved as MP3: {mp3_file}")
        return mp3_file
    except Exception as e:
        print(f"Error: {e}")

# Example usage
yt_url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
yt_to_mp3(yt_url, output_path='downloads')
