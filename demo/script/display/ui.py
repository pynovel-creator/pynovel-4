import pygame, time
from script import images
from script.config import *
from script.screen import choice_key
pygame.init()

font = pygame.font.SysFont('bitstreamverasans', 22)
fontb = pygame.font.SysFont('bitstreamverasans', 22, True)

background = None

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
def text(*text, pos, surface):
    global font, background
    background = pygame.image.load("script/display/frame.png")
    rect = background.get_rect()
    rect.center = [screen_width/2, screen_height-85]
    surface.blit(background, rect)
    for line in text:
        button_text = font.render(line, True, (255, 255, 255))
        button_text_rect = button_text.get_rect()
        button_text_rect.topleft = pos
        button_text_shadow = font.render(line, True, (0, 0, 0))
        button_text_shadow_rect = button_text.get_rect()
        button_text_shadow_rect.topleft = [pos[0]+2, pos[1]+2]
        surface.blit(button_text_shadow, button_text_shadow_rect)
        surface.blit(button_text, button_text_rect)
        pos = (pos[0], pos[1]+20)

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
        self.text = text
        self.render()
        self.draw()

    def render(self):
        self.button_text = font.render(self.text, True, (255, 255, 255))
        self.button_text_shadow = font.render(self.text, True, (0, 0, 0))
        self.idle_background = pygame.transform.scale(pygame.image.load("script/display/choice-idle-background.png"), (int(0.75 * screen_width), self.button_text.get_height()))
        self.hover_background = pygame.transform.scale(pygame.image.load("script/display/choice-hover-background.png"), (int(0.75 * screen_width), self.button_text.get_height()))

    def draw(self):
        self.idle_rect = self.idle_background.get_rect()
        self.hover_rect = self.hover_background.get_rect()
        self.idle_rect.center = self.pos
        self.hover_rect.center = self.pos
        self.button_text_rect = self.button_text.get_rect()
        self.button_text_rect.center = self.pos
        self.button_text_shadow_rect = self.button_text.get_rect()
        self.button_text_shadow_rect.center = [self.pos[0]+2, self.pos[1]+2]
        if self.idle_rect.collidepoint(pygame.mouse.get_pos()):
            self.idle_background = self.hover_background
            self.surface.blit(self.idle_background, self.idle_rect)
        else:
            self.idle_background = self.idle_background
            self.surface.blit(self.idle_background, self.idle_rect)
        self.surface.blit(self.button_text_shadow, self.button_text_shadow_rect)
        self.surface.blit(self.button_text, self.button_text_rect)

    def events(self, event):
        if event.button in choice_key:
            if self.idle_rect.collidepoint(event.pos):
                return self.action
