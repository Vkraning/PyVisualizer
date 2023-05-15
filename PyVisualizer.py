from tkinter import *
from tkinter import filedialog, messagebox
from pygame import mixer
import pygame
import time
from Visualizer import MusicVisualizer
from PIL import ImageTk, Image

current_volume = float(0.5)
Count = 1


# Functions
def play_song():
    # Lets you choose a song from your files, and it puts that song in the Song_Box
    filename = filedialog.askopenfilename(initialdir="audio/", title="please select a file")
    current_song = filename

    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        Song_Box.insert(END, filename)
        volume_label.config(fg="blue", text="Volume:" + str(current_volume))
    except Exception as e:
        print(e)
        error_label.config(fg="red", text="Error playing track")


def decrease_volume():
    try:
        # Used to decrease volume when you press the - button and if no song selected it print Track hasn't been
        # selected
        global current_volume
        if current_volume <= 0:
            volume_label.config(fg="red", text="Volume: Muted")
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="blue", text="Volume:" + str(current_volume))
    except Exception as e:
        print(e)
        error_label.config(fg="red", text="Track hasn't been selected")


def increase_volume():
    # Used to increase volume when you press the + button and if no song selected it print Track hasn't been selected
    try:
        global current_volume
        if current_volume >= 1:
            volume_label.config(fg="blue", text="Volume: Max")
            return
        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="blue", text="Volume:" + str(current_volume))
    except Exception as e:
        print(e)
        error_label.config(fg="red", text="Track hasn't been selected")


def pause():
    try:
        mixer.music.pause()
    except Exception as ex:
        print(ex)
        error_label.config(fg="red", text="Track hasn't been selected")


def resume():
    try:
        mixer.music.unpause()
    except Exception as exc:
        print(exc)
        error_label.config(fg="red", text="Track hasn't been selected")


def New_Window():
    global Count
    global Song_Box

    # Creates a new window that allows you to choose the color of either the songboxs' background or song name color
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
        Label(newWindow, text="Songlist color                                     ", font=("Calibri", 11),
              fg="black").grid(sticky='W', row=1)
        Label(newWindow, text=" background color", font=("Calibri", 11), fg="black").grid(sticky='E', row=1)
        newWindow.title("New Window")
        newWindow.geometry("200x200")
        Button(newWindow, text="Blue", font=("Calibri", 12), width=10, command=blue).grid(row=2, sticky="W")
        Button(newWindow, text="Magenta", font=("Calibri", 12), width=10, command=magenta).grid(row=3, sticky="W")
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
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(loops=0)
    except Exception as e:
        print(e)
        error_label.config(fg="red", text="Track hasn't been selected")


def stop():
    try:
        pygame.mixer.music.stop()
        Song_Box.selection_clear(ACTIVE)
    except Exception as e:
        print(e)
        error_label.config(fg="red", text="Track hasn't been selected")


def open_visualizer():
    # Creates a MusicVisualizer window
    visualizer_window = Toplevel(master)
    visualizer_window.title("Music Visualizer")
    visualizer = MusicVisualizer(canvas_width=500, canvas_height=300, master=visualizer_window)
    visualizer.start()


def on_enter(event):
    # increases button width
    event.widget.config(width=event.widget["width"] + 2)


def on_leave(event):
    # decreases button width
    event.widget.config(width=event.widget["width"] - 2)


def on_enter_picture(event):
    h.config(width=h.winfo_width() + 5)


def on_leave_picture(event):
    h.config(width=h.winfo_width() / 1.32)


def on_enter_picture2(event):
    g.config(width=g.winfo_width() + 5)


def on_leave_picture2(event):
    g.config(width=g.winfo_width() / 1.32)
def exit_application():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        master.destroy()

# Main Screen
master = Tk()
master.title("Music Player")
now = time.time()

# The pictures

# Stop button picture
stop_bnt = Image.open(f"E:\VIDEO\pause.png")
resized = stop_bnt.resize((51, 51), Image.LANCZOS)
new_stop = ImageTk.PhotoImage(resized)
stop_bnt = "This is the stop button"
# Play button picture
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

# Song Box
Song_Box = Listbox(master, bg="black", fg='green', width=60)
Song_Box.grid(sticky='N', row=10, )

# buttons
a = Button(master, text="Select Song", font=("Calibri", 12), width=12, command=play_song)
a.grid(row=2, sticky="N")
a.bind("<Enter>", on_enter)
a.bind("<Leave>", on_leave)
b = Button(master, text="pause", font=("Calibri", 12), width=6, command=pause)
b.grid(row=3, sticky="E")
b.bind("<Enter>", on_enter)
b.bind("<Leave>", on_leave)
c = Button(master, text="Resume", font=("Calibri", 12), width=6, command=resume)
c.grid(row=3, sticky="W")
c.bind("<Enter>", on_enter)
c.bind("<Leave>", on_leave)
d = Button(master, text="-", font=("Calibri", 12), width=6, command=decrease_volume)
d.grid(row=5, sticky="W")
d.bind("<Enter>", on_enter)
d.bind("<Leave>", on_leave)
e = Button(master, text="+", font=("Calibri", 12), width=6, command=increase_volume)
e.grid(row=5, sticky="E")
e.bind("<Enter>", on_enter)
e.bind("<Leave>", on_leave)
f = Button(master, text="Customize", font=("Calibri", 12), width=12, command=New_Window)
f.grid(row=0, sticky="E")
f.bind("<Enter>", on_enter)
f.bind("<Leave>", on_leave)
g = Button(master, image=new_play, command=play)
g.grid(row=8, sticky="W")
g.bind("<Enter>", on_enter_picture2)
g.bind("<Leave>", on_leave_picture2)
h = Button(master, image=new_stop, command=stop)
h.grid(row=8, sticky="E")
h.bind("<Enter>", on_enter_picture)
h.bind("<Leave>", on_leave_picture)
i = Button(master, text="Visualizer(Unfinished)", font=("Calibri", 12), width=20, command=open_visualizer)
i.grid(row=8, sticky="N")
i.bind("<Enter>", on_enter)
i.bind("<Leave>", on_leave)
Button(master, text="Quit", font=("Calibri", 12), width=12, command=exit_application).grid(row=0, sticky="W")
# Old animation test
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
