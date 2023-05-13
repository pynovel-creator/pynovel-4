# Import pygame and load it.
import pygame, subprocess
from pygame.locals import *
pygame.init()

# Image is stored here.
image = {}

# Import itself.
import script

# Display.
import script.display

# Audio
import script.audio.audio
import script.audio.music
import script.audio.sound

# This is the code of ui (script.display.ui shortcut).
import script.ui

# Configuration.
import script.config
import script.screen

def open_script(file):
    return subprocess.Popen("C:/Users/ntien/AppData/Local/Programs/Python/Python37/pythonw.exe C:/Users/ntien/AppData/Local/Programs/Python/Python37/Lib/idlelib/idle.pyw game/" + file, shell=True)
