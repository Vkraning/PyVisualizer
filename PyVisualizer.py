from tkinter import *
from tkinter import filedialog
from pygame import mixer
import pygame
import os


current_volume = float(0.5)
Count = 1

#Functions
def play_song():
    global filename
    filename = filedialog.askopenfilename(initialdir="audio/",title="please select a file")
    current_song = filename
    song_title = filename.split("/")
    song_title = song_title[-1]

    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        Song_Box.insert(END, song_title)
        #song_title_label.config(fg="blue",text="Now playing:"+ str(song_title))
        volume_label.config(fg="blue",text="Volume:"+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Error playing track")
def decrease_volume():
    try:
        global current_volume
        if current_volume <=0:
            volume_label.config(fg="red", text="Volume: Muted")
            return
        current_volume=current_volume - float(0.1)
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="blue", text="Volume:"+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn't been selected")
def increase_volume():
    try:
        global current_volume
        if current_volume >=1:
            volume_label.config(fg="blue", text="Volume: Max")
            return
        current_volume=current_volume + float(0.1)
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="blue", text="Volume:"+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn't been selected")

def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text ="Track hasn't been selected")

def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text ="Track hasn't been selected")
def New_Window():
    global Count
    if Count < 2:
        global newWindow
        newWindow = Toplevel()
        newWindow.title("New Window")
        newWindow.geometry("200x200")
        Label(newWindow,
              text="This is a new window").pack()
        Count += 1

    else:
        newWindow.destroy()
        Count -= 1
def play():
    filename = Song_Box.get(ACTIVE)
    filename = f'C:/Users/Vincent/Downloads/{filename}'
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(loops=0)
def stop():
    pygame.mixer.music.stop()
    Song_Box.selection_clear(ACTIVE)



# Main screen
master = Tk()
master.title("Music Player")


# The label
Label(master, text="PyVizualizer", font=("Calibri", 15), fg="blue").grid(sticky='N', row=0, padx=120)
Label(master, text="Please select one of your tracks", font=("Calibri", 15), fg="green").grid(sticky='N', row=1, )
Label(master, text="Volume", font=("Calibri", 15), fg="green").grid(sticky='N', row=4, )
song_title_label = Label(master, font=("Calibri", 12))
song_title_label.grid(stick="N", row=3)
volume_label = Label(master, font=("Calibri", 12))
volume_label.grid(stick="N,", row=5)
volume_label.config(fg="blue", text="Volume:")

Song_Box =Listbox(master, bg="black", fg='green', width=60)
Song_Box.grid(sticky='N', row=10,)
# buttons
Button(master, text="Select Song", font=("Calibri", 12),command=play_song).grid(row=2, sticky="N")
Button(master, text="Pause", font=("Calibri", 12),command=pause).grid(row=3, sticky="E")
Button(master, text="Resume", font=("Calibri", 12),command=resume).grid(row=3, sticky="W")
Button(master, text="-", font=("Calibri", 12), width=5,command=decrease_volume).grid(row=5, sticky="W")
Button(master, text="+", font=("Calibri", 12), width=5,command=increase_volume).grid(row=5, sticky="E")
Button(master, text="Settings", font=("Calibri", 12), width=10,command=New_Window).grid(row=0, sticky="E")
Button(master, text="Play", font=("Calibri", 12), width=5,command=play).grid(row=8, sticky="W")
Button(master, text="Stop", font=("Calibri", 12), width=10,command=stop).grid(row=8, sticky="E")
master.mainloop()
