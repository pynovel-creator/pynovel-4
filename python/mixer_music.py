# Testing to make sure everything okay!
# Don't modified itself while you're not know what are you doing.
import pygame.mixer
pygame.mixer.init()

def load(filename, namehint=""):
    try:
        return pygame.mixer.music.load('game/audio/' + filename, namehint)
    except:
        return pygame.mixer.music.load('game/' + filename, namehint)
def play(loops=-1, start=0.0, fade_ms=0):
    return pygame.mixer.music.play(loops, start, fade_ms)

def unload():
    print('Stop loading the music file(s)...')
    return pygame.mixer.music.unload()

def stop():
    print('Stop the current music...')
    pygame.mixer.music.stop()

def queue(filename, namehint="", loops=0):
    print('Playing the next sound...')
    pygame.mixer.music.queue(filename, namehint, loops)
    
