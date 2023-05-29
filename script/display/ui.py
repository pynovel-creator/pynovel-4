import pygame, time
from script import images
from script.config import *
from script.screen import choice_key
pygame.init()

font = pygame.font.SysFont('bitstreamverasans', 22)
fontb = pygame.font.SysFont('bitstreamverasans', 22, True)

images["box image"] = "frame.png"

def get_image_list():
    global _image
    image_files = list(images.values())
    return print('Stored: ' + str(image_files))
    
def error_text(text, surface):
    global font
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
        surface = pygame.image.load('game/' + name).convert_alpha()
    except:
        surface = "Error"
    return surface

# Let's add some user interaction.
def text(text, pos, surface):
    global font
    button_text = font.render(text, True, (255, 255, 255))
    button_text_rect = button_text.get_rect()
    button_text_rect.topleft = pos
    button_text_shadow = font.render(text, True, (0, 0, 0))
    button_text_shadow_rect = button_text.get_rect()
    button_text_shadow_rect.topleft = [pos[0]+2, pos[1]+2]
    surface.blit(button_text_shadow, button_text_shadow_rect)
    surface.blit(button_text, button_text_rect)
    
def box_appear(surface):
    show('box image', surface, 'box_image')

def say(object, surface, pos, antialias=True):
    global fontb

    try:
    	button_text = fontb.render(object.name, antialias, object.color)
    	button_text_shadow = fontb.render(object.name, True, (0, 0, 0))
    except:
    	button_text = fontb.render(object+":", antialias, (255, 255, 255))
    	button_text_shadow = fontb.render(object+":", True, (0, 0, 0))

    button_text_rect = button_text.get_rect()
    button_text_rect.topleft = pos
    button_text_shadow_rect = button_text.get_rect()
    button_text_shadow_rect.topleft = [pos[0]+2, pos[1]+2]
    surface.blit(button_text_shadow, button_text_shadow_rect)
    surface.blit(button_text, button_text_rect)

def scene(name, surface):
    try:
        try:
            surface.blit(image[name], (0, 0))
        except:
            surface.blit(image(images[name]), (0, 0))
    except:
        surface.fill(name)

left = [screen_width/4, screen_height/2]
center = [screen_width/2, screen_height/2]
right = [screen_width-200, screen_height/2]
box_image = [screen_width/2, screen_height-85]

def show(name, surface, pos='center'):
    global left, right, center, box_image
    try:
        try:
            name_rect = images[name].get_rect()
            name_rect.center = eval(pos)
            surface.blit(images[name], name_rect)
        except:
            name_surf = image(images[name])
            name_rect = name_surf.get_rect()
            name_rect.center = eval(pos)
            surface.blit(name_surf, name_rect)            
    except:
        error_text("Image '%s' isn't found while loading." % name, surface)
        

class textbutton:
    
    def __init__(self, text, pos, surface, action):
        try:
            self.action = action()
        except:
            self.action = action
        self.surface = surface
        self.pos = pos
        self.color = (0, 255, 255)
        self.text = text
        self.render()
        self.draw()

    def render(self):
        self.button_text = font.render(self.text, True, self.color)
        self.button_text_shadow = font.render(self.text, True, (0, 0, 0))

    def draw(self):
        self.button_text_rect = self.button_text.get_rect()
        self.button_text_rect.topleft = self.pos
        self.button_text_shadow_rect = self.button_text.get_rect()
        self.button_text_shadow_rect.topleft = [self.pos[0]+2, self.pos[1]+2]
        self.surface.blit(self.button_text_shadow, self.button_text_shadow_rect)
        self.surface.blit(self.button_text, self.button_text_rect)

    def events(self, event):
        if event.button in choice_key:
            if self.button_text_rect.collidepoint(event.pos):
                return self.action
