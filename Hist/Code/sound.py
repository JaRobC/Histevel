from pygame import mixer
import pygame

class Musique():
    def __init__(self):
        pygame.mixer.init()
        self.musique = mixer.music.load('./songs/mainsound.mp3')
    
    def jouer(self, flag):
        self.musique = mixer.music.play(-1)
        if flag == "pause":
            self.musique = mixer.music.pause()
            pass
        elif flag == "unpause":
            self.musique = mixer.music.unpause()
            pass
        else:
            pass
    
        