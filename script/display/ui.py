from script import *
from script.config import *
from script.render import choice_key
import pygame

pygame.init()

name = 'dejavu-sans'
size = 22
thick = True

font = pygame.font.SysFont(name, size)
fontb = pygame.font.SysFont(name, size, thick)

screen = pygame.Surface((screen_width, screen_height))

def drawbox(fill_color, outline_color, rect, outline, radius):
    global screen
    pygame.draw.rect(screen, fill_color, rect, 0, radius)
    pygame.draw.rect(screen, outline_color, rect, outline, radius)

background = pygame.Rect(0, 0, screen.get_width(), screen.get_height()/4)

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
def text(string, pos=(20, 470), backxoffset=20, backyoffset=20):
    global font, background, screen
    background.topleft = (pos[0]-backxoffset, pos[1]-backyoffset) 
    drawbox(pygame.Color("blue"), (255, 255, 255), background, 3, 10)
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

left = [screen.get_width()/4, screen.get_height()/2]
center = [screen.get_width()/2, screen.get_height()/2]
right = [screen.get_width()-200, screen.get_height()/2]

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
        try:
            self.sound = pygame.mixer.Sound("../script/display/click.wav")
        except:
            self.sound = pygame.mixer.Sound("script/display/click.wav")
        self.render()
        self.draw()

    def render(self):
        self.button_text = font.render(self.text, True, (255, 255, 255))
        self.idle_background = pygame.Rect(0, 0, int(0.75 * screen_width), self.button_text.get_height())
        self.idle_background.center = self.pos
        
    def draw(self):
        self.button_text_rect = self.button_text.get_rect()
        self.button_text_rect.center = self.pos
        if self.idle_background.collidepoint(pygame.mouse.get_pos()):
            drawbox(pygame.Color("darkblue"), (255, 255, 255), self.idle_background, 3, 16)
        else:
            drawbox(pygame.Color("blue"), (255, 255, 255), self.idle_background, 3, 16)
        self.surface.blit(self.button_text, self.button_text_rect)

    def events(self, event):
        if event.button in choice_key:
            if self.idle_background.collidepoint(event.pos):
                self.sound.play()
                return True

class ctextbutton:

    # This is used in the launcher.
    
    def __init__(self, text, pos=center): 
        self.surface = screen
        self.pos = pos
        self.text = text
        try:
            self.sound = pygame.mixer.Sound("../script/display/click.wav")
        except:
            self.sound = pygame.mixer.Sound("script/display/click.wav")
        self.render()
        self.draw()

    def render(self):
        self.button_text = font.render("      %s" % self.text, True, (255, 255, 255))
        self.idle_background = pygame.Rect(0, 0, self.button_text.get_width()+50, self.button_text.get_height())
        self.idle_background.center = self.pos
        
    def draw(self):
        self.button_text_rect = self.button_text.get_rect()
        self.button_text_rect.center = self.pos
        if self.idle_background.collidepoint(pygame.mouse.get_pos()):
            drawbox(pygame.Color("darkblue"), (255, 255, 255), self.idle_background, 3, 16)
        else:
            drawbox(pygame.Color("blue"), (255, 255, 255), self.idle_background, 3, 16)
        self.surface.blit(self.button_text, self.button_text_rect)

    def events(self, event):
        if event.button in choice_key:
            if self.idle_background.collidepoint(event.pos):
                self.sound.play()
                return True

class Input:

    def __init__(self, text='', length=None, pos=(20, 470)):
        self.text = text 
        self.pos = pos
        self.active = True
        self.contents = self.text + '_'
        self.length = length
    def update(self, event):
        if self.active:

            if event.key == K_RETURN:
                self.active = False

            elif event.key == K_BACKSPACE:
                self.text = self.text[:-1]

            else:

                if self.length != None:

                   if len(self.text) == self.length:
                       self.text = self.text

                   else:
                       self.text += event.unicode
                else:
                    self.text += event.unicode

            self.contents = self.text + '_'
            self.img = font.render(self.contents, True, (255, 255, 0))
            self.rect = self.img.get_rect()
            self.rect.topleft = self.pos
            screen.blit(self.img, self.rect)

        if not self.active:
             return self.text

    def draw(self):
        self.img = font.render(self.contents, True, (255, 255, 0))
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
        screen.blit(self.img, self.rect)

screen = pygame.Surface((screen_width, screen_height))
        
