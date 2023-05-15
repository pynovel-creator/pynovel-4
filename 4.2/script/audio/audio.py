import pygame.mixer
pygame.mixer.init()

def play(filename, loops=0):
    pygame.mixer.music.load('game/' + filename)
    pygame.mixer.music.play(loops)

def stop():
    pygame.mixer.music.stop()
