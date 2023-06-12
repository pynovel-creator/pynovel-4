import pygame.mixer
pygame.mixer.init()

sound = None

def play(filename, loops=0):
    global sound
    sound = pygame.mixer.Sound('game/' + filename)
    sound.play(loops)

def stop():
    global sound
    sound.stop()
