from script.display.ui import *
import script.config as config

_text = text
_say = say
_image = image
_show = show
_scene = scene
input = Input
_input = Input

def makescreen():
    newscreen = pygame.display.set_mode((config.screen_width, config.screen_height))    
    return newscreen

def makenewscreen():
    newscreen = pygame.display.set_mode((config.screen_width, config.screen_height))
    return newscreen

newscreen = makenewscreen()

def render():
    newscreen.blit(screen, (0, 0))
    pygame.display.flip()