from script import *
from script.config import *
from script.render import choice_key
import pygame

pygame.init()

font = pygame.font.SysFont('dejavu-sans', 22)
fontb = pygame.font.SysFont('dejavu-sans', 22, True)

background = pygame.image.load("script/display/frame.png")

screen = pygame.display.set_mode((screen_width, screen_height))

def get_image_list():
    global _image
    image_files = list(images.values())
    return print('Stored: ' + str(image_files))
    
def error_text(text):
    global font, screen
    button_text = font.render(text, True, (255, 0, 0))
    button_text_rect = button_text.get_rect()
    button_text_rect.topleft = (0, 0)
    screen.blit(button_text, button_text_rect)
    
def image(name):
    try:
        surface = pygame.image.load('game/' + name).convert_alpha()
    except:
        surface = "Error"
    return surface

# Let's add some user interaction.
def text(string, pos=(20, 470)):
    global font, background, screen
    rect = background.get_rect()
    rect.center = [screen_width/2, screen_height-85]
    screen.blit(background, rect)
    button_text = font.render(string, True, (255, 255, 255))
    button_text_rect = button_text.get_rect()
    button_text_rect.topleft = pos
    screen.blit(button_text, button_text_rect)

def say(object, pos=(20, 450), antialias=True):
    global fontb, screen
    try:
    	button_text = fontb.render(object.name, antialias, object.color)
    	button_text_shadow = fontb.render(object.name, True, (0, 0, 0))
    except:
    	button_text = fontb.render(object+":", antialias, (255, 255, 255))
    	button_text_shadow = fontb.render(object+":", True, (0, 0, 0))
    button_text_rect = button_text.get_rect()
    button_text_rect.topleft = pos
    screen.blit(button_text, button_text_rect)

def scene(name):
    try:
        try:
            screen.blit(image[name], (0, 0))
        except:
            screen.blit(image(images[name]), (0, 0))
    except:
        screen.fill(name)

left = [screen_width/4, screen_height/2]
center = [screen_width/2, screen_height/2]
right = [screen_width-200, screen_height/2]

def show(name, pos='center'):
    global left, right, center, box_image
    try:
        try:
            name_rect = images[name].get_rect()
            name_rect.center = eval(pos)
            screen.blit(images[name], name_rect)
        except:
            name_surf = image(images[name])
            name_rect = name_surf.get_rect()
            name_rect.center = eval(pos)
            screen.blit(name_surf, name_rect)            
    except:
        error_text("Image '%s' isn't found while loading." % name, surface)       

class textbutton:
    
    def __init__(self, text, pos=center): 
        self.surface = screen
        self.pos = pos
        self.text = text
        self.sound = None
        if click_sound:
            self.sound = pygame.mixer.Sound(click_sound)
        self.render()
        self.draw()

    def render(self):
        self.button_text = font.render(self.text, True, (200, 255, 255))
        self.idle_background = pygame.Rect(0, 0, int(0.75 * screen_width), self.button_text.get_height())
        self.idle_background.center = self.pos
        
    def draw(self):
        self.button_text_rect = self.button_text.get_rect()
        self.button_text_rect.center = self.pos
        if self.idle_background.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.surface, (0, 60, 180), self.idle_background, 0, 12)
        else:
            pygame.draw.rect(self.surface, (0, 60, 120), self.idle_background, 0, 12)
        self.surface.blit(self.button_text, self.button_text_rect)

    def events(self, event):
        if event.button in choice_key:
            if self.idle_background.collidepoint(event.pos):
                if self.sound != None:
                    self.sound.play()
                return True

class Input:

    def __init__(self, text, pos=center):
        self.text = text 
        self.pos = pos
        self.active = True
        self.contents = self.text + '_'

    def update(self, event):
        if self.active:

            if event.key == K_RETURN:
                return self.text

            elif event.key == K_BACKSPACE:
                self.text = self.text[:-1]

            else:
                self.text += event.unicode

            self.contents = self.text + '_'
            self.img = font.render(self.contents, True, (255, 255, 0))
            self.rect = self.img.get_rect()
            self.rect.center = self.pos
            screen.blit(self.img, self.rect)
            self.background = pygame.transform.scale(background, (background.get_width(), self.img.get_height()))
            self.brect = self.background.get_rect()
            self.brect.center = self.pos
            screen.blit(self.background, self.brect)

    def draw(self):
        self.img = font.render(self.contents, True, (255, 255, 0))
        self.rect = self.img.get_rect()
        self.rect.center = self.pos
        self.background = pygame.transform.scale(background, (background.get_width(), self.img.get_height()))
        self.brect = self.background.get_rect()
        self.brect.center = self.pos
        screen.blit(self.background, self.brect)
        screen.blit(self.img, self.rect)
        
