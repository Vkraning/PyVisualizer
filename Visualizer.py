import tkinter as tk
import wave
import numpy as np
import pyaudio
from tkinter import filedialog

# Parameters
CHUNK_SIZE = 2048
SAMPLE_RATE = 44100
UPDATE_DELAY = 10
color = "white"
Count = 1


class MusicVisualizer:
    def __init__(self,  master=None, canvas_width=500, canvas_height=300):
        # Initialize PyAudio
        self.pa = pyaudio.PyAudio()

        def New_Window():
            global Count

            def blue():
                for bar in self.bars:
                    self.canvas.itemconfig(bar, fill="blue")

            def red():
                for bar in self.bars:
                    self.canvas.itemconfig(bar, fill="red")

            if Count < 2:
                global newWindow
                newWindow = tk.Toplevel()
                newWindow.title("New Window")
                newWindow.geometry("200x200")
                tk.Button(newWindow, text="Blue", font=("Calibri", 12), width=10, command=blue).grid(row=1, sticky="E")
                tk.Button(newWindow, text="red", font=("Calibri", 12), width=10, command=red).grid(row=2, sticky="E")
                Count += 1

            else:
                newWindow.destroy()
                Count -= 1

        # Initialize Tkinter
        self.master = master if master else tk.Tk()

        self.button = tk.Button(self.master, text="Choose a song", command=self.select_file)
        self.button.grid(row=2, column=0, padx=10, pady=10)
        self.button= tk.Button(self.master, text="Customize", font=("Calibri", 12), width=18, command=New_Window).grid(row=0,
                                                                                                          sticky="E")



        # Create canvas and make it a 10x10 grid
        self.canvas = tk.Canvas(self.master, width=canvas_width, height=canvas_height, bg="black")
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        for i in range(10):
            self.canvas.columnconfigure(i, weight=0)
            self.canvas.rowconfigure(i, weight=1)

        # Initialize frequencies and bars
        self.frequencies = np.fft.fftfreq(CHUNK_SIZE, 1/SAMPLE_RATE)[:int(CHUNK_SIZE/2)]
        self.bars = [self.canvas.create_rectangle(5 + i*20, canvas_height-10, 25 + i*20, canvas_height, fill=color) for i in range(len(self.frequencies))]



    def select_file(self):
        # Open file dialog to select music file
        file_path = filedialog.askopenfilename(title="Select Music File", filetypes=[("Audio Files", "*.wav;*.mp3")])
        if not file_path:
            # User clicked cancel, exit program
            self.stop()
            exit()

        # Open audio stream
        self.stream = self.pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=SAMPLE_RATE,
            input=False,
            output=True
        )

        # Open music file
        self.audio_file = wave.open(file_path, 'rb')

    def update(self):
        # Read a chunk of audio data from the file
        audio_data = self.audio_file.readframes(CHUNK_SIZE)

        if not audio_data:
            # End of file, stop visualization
            self.stop()
            exit()

        # Apply Fast Fourier Transform
        audio_data = np.frombuffer(audio_data, dtype=np.int16)
        audio_fft = np.fft.fft(audio_data)
        audio_fft = np.abs(audio_fft)[:int(CHUNK_SIZE / 2)]

        # Update bars
        for i in range(len(self.bars)):
            bar_height = int(audio_fft[i] / 500 * 0.00009 * self.canvas.winfo_height())
            self.canvas.coords(self.bars[i], 10 + i * 20, self.canvas.winfo_height() - bar_height - 10, 25 + i * 20,
                               self.canvas.winfo_height() - 10)

        # Write audio data to stream
        self.stream.write(audio_data.tobytes())

        # Schedule next update
        self.master.after(UPDATE_DELAY, self.update)

    def start(self):
        self.select_file()
        self.master.after(0, self.update)
        self.master.mainloop()


if __name__ == '__main__':
    visualizer = MusicVisualizer(canvas_width=500, canvas_height=300)
    visualizer.start()
