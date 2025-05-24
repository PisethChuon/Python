from pytube import YouTube

url = input('Enter a video to download audio:')
yt = YouTube(url)

# Filter audiion stream and download the first one
audio_stream = yt.streams.filter(only_audio=True).first()
audio_stream.download()