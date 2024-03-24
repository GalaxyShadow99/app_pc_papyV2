import os
from tkinter import filedialog


path = filedialog.askdirectory()
music_path = []

for filename in os.listdir(path):
    if filename.endswith(".mp3" or ".wav" or ".ogg"):
        music_path.append(filename)
        
for elt in music_path:
    print(f'"{elt}"',end=',')
    print()
