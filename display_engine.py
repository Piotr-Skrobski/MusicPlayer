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


        self.btn_choosefile = tk.Button(
            master = self.window,
            text = "Open the file",
            command = self.choose_file
        )

        self.btn_pausemusic = tk.Button(
            master = self.window, 
            text = "Pause music!",
            command = lambda : MusicEngine.PauseMusic(MusicEngine)
        )

        self.btn_playmusic = tk.Button(
            master = self.window, 
            text = "Play music!",
            command = lambda : MusicEngine.LoadMusic(self, self.filepath) #I have no clue why making this lambda works, but it works.
            )

        self.lbl_time = tk.Label(
            master = self.window,
            text = '0:00'
        )
        
        self.clock()
        self.btn_choosefile.grid(row = 0, column = 0, sticky = "nw")
        self.btn_playmusic.grid(row = 1, column = 0, sticky = "nw")
        self.btn_pausemusic.grid(row = 1, column = 1)
        self.lbl_time.grid(row = 2, column = 0, sticky="ns")

    def choose_file(self):
        self.filepath = askopenfilename(
            filetypes = [("MP3 files", "*.mp3"), ("OGG files", "*.ogg"), ("All files", "*.*")]
        )
        if not self.filepath:
            return
    
    def get_time_of_song(self):
        return MusicEngine.GetTimeOfSong(MusicEngine)

    def clock(self):
        if MusicEngine.is_music_playing == True:
            seconds = self.get_time_of_song() / 1000
            minutes = 0
            if seconds > 59:
                while seconds > 59:
                    seconds -= 60
                    minutes += 1

            seconds = round(seconds)
            if seconds < 10:
                seconds = "0" + str(seconds)
            self.lbl_time["text"] = str(minutes) + ":" + str(seconds)
        self.window.after(1000, self.clock)

        


