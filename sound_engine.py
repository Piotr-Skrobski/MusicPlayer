import pygame
import os.path


class MusicEngine():

    def __init__(self):
        #Initalise music engine
        pygame.mixer.init()
        self.is_music_playing = False
    
    def LoadMusic(self, filename, loops = None):
        if os.path.exists(filename):
            pygame.mixer.music.load(filename)
            if loops != None:
                pygame.mixer.music.play(loops)
            else:
                pygame.mixer.music.play()

        else:
            return -1 #File does not exist, error

    def PlayMusic(self, loops = None):
        if loops != None:
            pygame.mixer.music.play(loops)
        else:
            pygame.mixer.music.play()


