from tkinter import *
from tkinter import filedialog
from pygame import mixer
import pygame
import time
from Visualizer import MusicVisualizer
from Visualizer import color
from PIL import ImageTk, Image

current_volume = float(0.5)
Count = 1




#Functions
def play_song():
    global filename
    filename = filedialog.askopenfilename(initialdir="audio/", title="please select a file")
    current_song = filename
  #  song_title = filename.split("/")
   # song_title = song_title[-1]

    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        Song_Box.insert(END, filename)
        #song_title_label.config(fg="blue",text="Now playing:"+ str(song_title))
        volume_label.config(fg="blue", text="Volume:"+str(current_volume))
    except Exception as e:
        print(e)
        error_label.config(fg="red", text="Error playing track")


def decrease_volume():
    try:
        global current_volume
        if current_volume <= 0:
            volume_label.config(fg="red", text="Volume: Muted")
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="blue", text="Volume:"+str(current_volume))
    except Exception as e:
        print(e)
        error_label.config(fg="red", text="Track hasn't been selected")
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
        error_label.config(fg="red", text="Track hasn't been selected")

def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        error_label.config(fg="red", text ="Track hasn't been selected")

def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        error_label.config(fg="red", text ="Track hasn't been selected")
def New_Window():
    global Count
    global Song_Box

    def blue():
        Song_Box.configure(fg='blue')

    def magenta():
        Song_Box.configure(fg='magenta')

    def green():
        Song_Box.configure(fg='green')

    def orange():
        Song_Box.configure(fg='orange')
    def tan_bg():
        Song_Box.configure(bg='tan')

    def brown_bg():
        Song_Box.configure(bg='brown')

    def white_bg():
        Song_Box.configure(bg='white')

    def black_bg():
        Song_Box.configure(bg='black')

    if Count < 2:
        global newWindow
        newWindow = Toplevel()
        Label(newWindow, text="Songlist color                                     ", font=("Calibri", 11), fg="black").grid(sticky='W', row=1)
        Label(newWindow, text=" background color", font=("Calibri", 11), fg="black").grid(sticky='E', row=1)
        newWindow.title("New Window")
        newWindow.geometry("200x200")
        Button(newWindow, text="Blue", font=("Calibri", 12), width=10, command=blue).grid(row=2,sticky="W")
        Button(newWindow, text="Magenta", font=("Calibri", 12), width=10, command=magenta).grid(row=3,sticky="W")
        Button(newWindow, text="Green", font=("Calibri", 12), width=10, command=green).grid(row=4, sticky="W")
        Button(newWindow, text="Orange", font=("Calibri", 12), width=10, command=orange).grid(row=5, sticky="W")
        Button(newWindow, text="Tan", font=("Calibri", 12), width=10, command=tan_bg).grid(row=2, sticky="E")
        Button(newWindow, text="Brown", font=("Calibri", 12), width=10, command=brown_bg).grid(row=3, sticky="E")
        Button(newWindow, text="White", font=("Calibri", 12), width=10, command=white_bg).grid(row=4, sticky="E")
        Button(newWindow, text="Black", font=("Calibri", 12), width=10, command=black_bg).grid(row=5, sticky="E")
        Count += 1

    else:
        newWindow.destroy()
        Count -= 1
def play():
    try:
        filename = Song_Box.get(ACTIVE)
        #BROKEN UNLESS My COMPUTER
        #filename = f'C:/{filename}'
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(loops=0)
    except Exception as e:
        print(e)
        error_label.config(fg="red", text ="Track hasn't been selected")
def stop():
    try:
        pygame.mixer.music.stop()
        Song_Box.selection_clear(ACTIVE)
    except Exception as e:
        print(e)
        error_label.config(fg="red", text="Track hasn't been selected")
def open_visualizer():
    # Create a MusicVisualizer window
    visualizer_window = Toplevel(master)
    visualizer_window.title("Music Visualizer")
    visualizer = MusicVisualizer(canvas_width=500, canvas_height=300, master=visualizer_window)
    visualizer.start()



# Main Screen
master = Tk()
master.title("Music Player")
now = time.time()

# The pictures

#Stop button
stop_bnt = Image.open(f"E:\VIDEO\pause.png")
resized = stop_bnt.resize((51, 51), Image.LANCZOS)
new_stop = ImageTk.PhotoImage(resized)
stop_bnt= "This is the stop button"
#Play button
play_bnt = Image.open(f"E:\VIDEO\play-button.png")
resized = play_bnt.resize((51, 51), Image.LANCZOS)
new_play = ImageTk.PhotoImage(resized)
# The label

Label(master, text="PyVizualizer", font=("Calibri", 15), fg="blue").grid(sticky='N', row=0, padx=120)
Label(master, text="Please select one of your tracks", font=("Calibri", 15), fg="green").grid(sticky='N', row=1, )
Label(master, text="Volume", font=("Calibri", 15), fg="green").grid(sticky='N', row=4, )
error_label = Label(master, font=("Calibri", 12))
error_label.grid(stick="N", row=3)
volume_label = Label(master, font=("Calibri", 12))
volume_label.grid(stick="N,", row=5)
volume_label.config(fg="blue", text="Volume:")

#Song Box
Song_Box = Listbox(master, bg="black", fg='green', width=60)
Song_Box.grid(sticky='N', row=10,)

# buttons
Button(master, text="Select Song", font=("Calibri", 12),width=12,command=play_song).grid(row=2, sticky="N")
Button(master, text="pause", font=("Calibri", 12), width=6,command=pause).grid(row=3, sticky="E")
Button(master, text="Resume", font=("Calibri", 12), width=6,command=resume).grid(row=3, sticky="W")
Button(master, text="-", font=("Calibri", 12), width=6,command=decrease_volume).grid(row=5, sticky="W")
Button(master, text="+", font=("Calibri", 12), width=6,command=increase_volume).grid(row=5, sticky="E")
Button(master, text="Customize", font=("Calibri", 12), width=12,command=New_Window).grid(row=0, sticky="E")
Button(master, image=new_play,command=play).grid(row=8, sticky="W")
Button(master, image=new_stop,command=stop).grid(row=8, sticky="E")
Button(master, text="Visualizer(Unfinished)", font=("Calibri", 12), width=20,command=open_visualizer).grid(row=8, sticky="N")


# #Canvas for visuals
# Canvas(master,bg="black", width=500, height=300).grid(row=20, sticky="W")
# count = 1
# size = 50
# def animate():
#     global count, size
#     #pygame.init()
#     size += 2
#     #sound = AudioSegment.from_file(filename)
#     #loudness = sound.dBFS
#     #with open(filename, "rb") as wav_file:
#         #audio_segment = AudioSegment.from_file(wav_file)
#     Label(master, text =size,font=("Calibri", 12), width=10).grid(row=21, sticky="E")
#     if count < 75:
#         size += 2
#         Canvas(master, bg="purple", width=size,height = size).grid(row=20, sticky="N")
#         count += 1
#         master.after(10, animate)
#
# Button(master, text="animate", font=("Calibri", 12), width=10, command=animate).grid(row=10, sticky="E")
master.mainloop()
