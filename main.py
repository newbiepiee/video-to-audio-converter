import moviepy.editor
from tkinter.filedialog import *

video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)
audio = video.audio

audio.write_audiofile("parinam.mp3")
print("Khatam,Tata,Bye Bye,Good bye, Gya!")