import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

positions = {
    'left': (screen.get_rect().centerx-200, screen.get_rect().centery),
    'center': screen.get_rect().center,
    'right': (screen.get_rect().centerx-200, screen.get_rect().centery),
    }

def image(load_fn, colorkey=None):

    file = pygame.image.load(load_fn)
    if colorkey:
        file.set_colorkey(colorkey)
    return file

def blit(name, rect):
    return screen.blit(name, rect)

class Image:

    def __init__(self, fn, colorkey=None):
        self.img = image('game/' + fn, colorkey)

    def draw(self, surface, position):
        self.rect = self.img.get_rect()
        self.rect.center = positions[position]            
        blit(self.img, self.rect)

    def clear(self):
        self.img.set_alpha(0)

def show(storer, name, pos='center'):
    storer[name].draw(screen, pos)

def scene(storer, name):
    storer[name].draw(screen, 'center')
