# Import pygame and load it.
import pygame, subprocess, sys, os
from pygame.locals import *
pygame.init()

# Image is stored here.
images = {}

# Movie is stored here.
movies = {}
playmovie = None

# Import itself.
import script

# Display.
import script.display

# Audio
import script.audio.audio
import script.audio.music
import script.audio.sound

# This is the code of ui (script.display.ui shortcut, important).
from script.ui import *

# Configuration.
import script.config
from script.render import *

# Movie
import script.movie

pygame.mouse.set_cursor(*pygame.cursors.arrow)

def music_start(file, loops=-1):
    # Ensure that's in game/ directory
    return audio.audio.play(file, -1)

def music_stop():
    return audio.audio.stop()

class Character:

    def __init__(self, name, color):
        if len(color) < 4:
            raise Exception("Color must be in RGBA value.")

        self.name = name + ":"
        self.color = color

    def get_name(self):
        return self.name

    def rgba_return(self):
        return self.color

def movie_start(filename):
    global playmovie
    if filename in movies:
        playmovie = script.movie.Movie(movies[filename])
    else:
        playmovie = script.movie.Movie(filename)
    return playmovie.play()

def movie_stop():
    global playmovie
    playmovie.stop()

def exists(filename):
    for file in os.listdir('game'):
        if file == filename:
            return True
        else:
            return False

def file(filename, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    return open(filename, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

def pathjoin(a, *p):
    path = a

    for b in p:
        path += '/' + b

    return path

def init():
    pygame.init()

def quit():
    pygame.quit()
    sys.exit()
        
        
