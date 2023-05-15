import pygame, time
from script import image as _image
from script.config import *
from script.screen import choice_key
pygame.init()

next_scene = None
font = pygame.font.SysFont('bitstreamverasans', 22)
fontb = pygame.font.SysFont('bitstreamverasans', 22, True)

left_button = pygame.mouse.get_pressed()[0]
right_button = pygame.mouse.get_pressed()[2]

def error_text(text, surface):
    global font, _image
    button_text = font.render(text, True, (255, 0, 0))
    button_text_rect = button_text.get_rect()
    button_text_rect.topleft = (0, 0)
    button_text_shadow = font.render(text, True, (0, 0, 0))
    button_text_shadow_rect = button_text.get_rect()
    button_text_shadow_rect.topleft = [2, 2]
    surface.blit(button_text_shadow, button_text_shadow_rect)
    surface.blit(button_text, button_text_rect)
    
def image(name):
    try:
        surface = pygame.image.load('game/' + name)
    except:
        surface = "Error"
    return surface
    
# Let's add some user interaction.
def text(text, pos, surface):
    global font, _image
    button_text = font.render(text, True, (255, 255, 255))
    button_text_rect = button_text.get_rect()
    button_text_rect.topleft = pos
    button_text_shadow = font.render(text, True, (0, 0, 0))
    button_text_shadow_rect = button_text.get_rect()
    button_text_shadow_rect.topleft = [pos[0]+2, pos[1]+2]
    surface.blit(button_text_shadow, button_text_shadow_rect)
    surface.blit(button_text, button_text_rect)
def box_appear(surface):
    _image["box image"] = image("frame.png")
    show('box image', surface, 'box_image')

def say(object, surface, pos, antialias=True):
    global fontb

    try:
    	button_text = fontb.render(object.name, antialias, object.color)
    	button_text_rect = button_text.get_rect()
    	button_text_rect.topleft = pos
    except:
    	button_text = fontb.render(object+":", antialias, (255, 255, 255))
    	button_text_rect = button_text.get_rect()
    	button_text_rect.topleft = pos

    surface.blit(button_text, button_text_rect)

def scene(name, surface):
    if name != "black":
        surface.blit(_image[name], (0, 0))
    else:
        surface.fill((0, 0, 0))

def show(name, surface, pos='center'):
    position()
    try:
        name_rect = _image[name].get_rect()
        name_rect.center = eval("position.%s" % pos)
        surface.blit(_image[name], name_rect)
    except:
        error_text("Image '%s' isn't found while loading." % name, surface)

def position():
    position.left = [200, 300]
    position.center = [400, 300]
    position.right = [600, 300]
    position.box_image = [400, 515]

            
