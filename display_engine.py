from sound_engine import MusicEngine
import tkinter as tk
from tkinter.filedialog import askopenfilename

class DisplayWindow():

    def __init__(self, window_title, dim_x, dim_y):
        self.window_title = window_title
        self.dim_x = dim_x
        self.dim_y = dim_y

        self.window = tk.Tk()
        self.window.title(window_title)
        self.window.geometry(str(self.dim_x) + "x" + str(self.dim_y))


        btn_choosefile = tk.Button(
            master = self.window,
            text = "Open the file",
            command = self.choose_file
        )

        btn_playmusic = tk.Button(
            master = self.window, 
            text = "Play music!",
            command = lambda : MusicEngine.LoadMusic(self, self.filepath) #I have no clue why making this lambda works, but it works.
            )
        
        btn_choosefile.grid(row = 0, column = 0, sticky="nw")
        btn_playmusic.grid(row = 1, column = 0)

    def choose_file(self):
        self.filepath = askopenfilename(
            filetypes = [("MP3 files", "*.mp3"), ("OGG files", "*.ogg"), ("All files", "*.*")]
        )
        if not self.filepath:
            return
        


