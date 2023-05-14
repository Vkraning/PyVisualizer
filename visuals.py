import sys
from tkinter import filedialog

import pygame
import pyaudio
import numpy as np
import os.path
class visual:
    # Initialize Pygame
    pygame.init()
    
    # Set up the screen
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Music Visualizer")
    
    # Set up Pyaudio
    p = pyaudio.PyAudio()
    stream = None
    
    # Ask user to enter file path
    file_path = filedialog.askopenfilename(initialdir="audio/", title="please select a file")
    
    # Check if file exists
    while not os.path.exists(file_path):
        print("File not found.")
        file_path = input("Enter the path of the audio file: ")
    
    # Load audio file
    file_extension = os.path.splitext(file_path)[1]
    if file_extension == ".wav":
        audio_sample_rate, audio_sample_width, audio_channels = p.get_format_from_width(2), 2, 1
        stream = p.open(format=audio_sample_rate,
                        channels=audio_channels,
                        rate=44100,
                        input=True,
                        frames_per_buffer=1024)
    else:
        print("File format not supported.")
        pygame.quit()
        sys.exit()
    
    # Apply FFT to audio data
    fft_data = np.zeros(512, dtype=np.float32)
    def calculate_fft(data):
        global fft_data
        fft_data = np.fft.fft(data)
        fft_data = np.abs(fft_data[0:len(fft_data)//2])
        fft_data = fft_data / np.max(fft_data)
    
    # Main loop
    running = True
    while running:
    
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        # Read audio data from stream
        data = np.frombuffer(stream.read(1024), dtype=np.int16)
    
        # Apply FFT to audio data
        calculate_fft(data)
    
        # Draw bars
        bar_width = screen.get_width() / len(fft_data)
        for i in range(len(fft_data)):
            bar_height = fft_data[i] * screen.get_height() * 1
            bar_x = i * bar_width
            bar_y = screen.get_height() - bar_height
            pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, bar_width, bar_height))
    
        # Update the screen
        pygame.display.flip()
    
    # Clean up
    pygame.quit()
    if stream is not None:
        stream.stop_stream()
        stream.close()
    p.terminate()
