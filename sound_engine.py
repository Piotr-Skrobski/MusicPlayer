import pygame
import os.path



class MusicEngine():

    is_music_playing = False
    is_music_paused = False

    def __init__(self):
        #Initalise music engine
        pygame.mixer.init()
        
    
    def LoadMusic(self, filename, loops = None):
        if os.path.exists(filename):
            pygame.mixer.music.load(filename)
            MusicEngine.is_music_playing = True
            if loops != None:
                pygame.mixer.music.play(loops)
            else:
                pygame.mixer.music.play()

        else:
            return -1 #File does not exist, error

    def PauseMusic(self):
            if MusicEngine.is_music_paused == False:
                pygame.mixer.music.pause()
                MusicEngine.is_music_paused = True
            else:
                pygame.mixer.music.unpause()


    def PlayMusic(self, loops = None):
        if loops != None:
            pygame.mixer.music.play(loops)
        else:
            pygame.mixer.music.play()

    def GetTimeOfSong(self):
        return pygame.mixer.music.get_pos()


