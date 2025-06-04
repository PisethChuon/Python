from pytube import YouTube

url = input("Enter the YouTube video URL: ")
yt = YouTube(url)

audio_stream = yt.streams.filter(only_audio=True).first()
audio_stream.download()