from sound_engine import *
from display_engine import *

import pygame

pygame.init()

music_eng = MusicEngine()


display = DisplayWindow("Music Player", 300, 200)
#music_eng.PlayMusic()

display.window.mainloop()

