from pytube import YouTube
from moviepy.editor import *

# Step 1: Get YouTube video
url = 'https://www.youtube.com/watch?v=6uUvcX85krw'  # Replace with your video URL
yt = YouTube(url)

# Step 2: Download the highest quality audio stream
audio_stream = yt.streams.filter(only_audio=True).first()
downloaded_file = audio_stream.download(filename="temp_audio.mp4")

# Step 3: Convert to MP3
output_file = "output_audio.mp3"
audio_clip = AudioFileClip(downloaded_file)
audio_clip.write_audiofile(output_file)

# Step 4: Clean up
audio_clip.close()
print(f"Download complete! Saved as {output_file}")
