import yt_dlp as yt
import tkinter as tk
from tkinter import *
from playsound import playsound
from tkVideoPlayer import TkinterVideo
from PIL import Image, ImageTk
import vlc


window = tk.Tk()

frame = tk.Frame(window, width=700, height=600)
frame.pack()

display = tk.Frame(frame, bd=5)
display.place(relwidth=1, relheight=1)

Instance = vlc.Instance()
player = Instance.media_player_new()
player.set_xwindow(display.winfo_id())


def playVideo():
    Media = Instance.media_new('test-video.mp4')
    player.set_media(Media)
    player.play()

back = PhotoImage(master=window, file="img/skip-prev.png", width=25, height=25)
Button(window, image=back, command=playVideo).pack(side = BOTTOM, pady = 0)
play = PhotoImage(master=window, file="img/play.png", width=25, height=25)
Button(window, image=play, command=playVideo).pack(side = BOTTOM, pady = 0)


window.mainloop()
