import os
import tkinter as tk
from tkinter import filedialog
import pygame


# Initialize pygame mixer
pygame.mixer.init()

# Load music file
def load_music():
    global music_file
    music_file = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if music_file:
        pygame.mixer.music.load(music_file)
        song_label.config(text=os.path.basename(music_file))

# Play the music
def play_music():
    if music_file:
        pygame.mixer.music.play()

# Pause the music
def pause_music():
    pygame.mixer.music.pause()

# Resume music
def resume_music():
    pygame.mixer.music.unpause()

# Stop music
def stop_music():
    pygame.mixer.music.stop()

# GUI setup
root = tk.Tk()
root.title("Python Music Player 🎵")
root.geometry("400x300")
root.config(bg="#1DB954")  # Spotify green

song_label = tk.Label(root, text="Load a song to play", bg="#1DB954", fg="white", font=("Helvetica", 14))
song_label.pack(pady=20)

btn_frame = tk.Frame(root, bg="#1DB954")
btn_frame.pack(pady=10)

load_btn = tk.Button(btn_frame, text="Load", command=load_music)
load_btn.grid(row=0, column=0, padx=10)

play_btn = tk.Button(btn_frame, text="Play ▶️", command=play_music)
play_btn.grid(row=0, column=1, padx=10)

pause_btn = tk.Button(btn_frame, text="Pause ⏸️", command=pause_music)
pause_btn.grid(row=0, column=2, padx=10)

resume_btn = tk.Button(btn_frame, text="Resume 🔁", command=resume_music)
resume_btn.grid(row=1, column=0, padx=10, pady=10)

stop_btn = tk.Button(btn_frame, text="Stop ⏹️", command=stop_music)
stop_btn.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
