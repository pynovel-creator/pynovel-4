import pygame
import python.graph
pygame.init()

class Text:
    "Create a text object."

    def __init__(self, text, pos, surface, **options):
        self.text = text
        self.pos = pos

        self.fontname = 'dejavu-sans'
        self.fontsize = 22
        self.fontcolor = python.graph.color(255, 255, 255)
        self.set_font()
        self.render(surface)

    def set_font(self):
        "Set the font from its name and size."
        self.font = pygame.font.SysFont(self.fontname, self.fontsize)
    
    def render(self, surface, box=True):
        "Render the text into an image."
        if box == True:
            self.box = pygame.Surface((800, 200))
            self.box.fill((63, 72, 204))
            self.box.set_alpha(200)
            surface.blit(self.box, (self.pos[0]-20, self.pos[1]-20))
        for text in self.text:
            self.img = self.font.render(text, True, self.fontcolor)
            self.rect = self.img.get_rect()
            self.rect.topleft = self.pos
            surface.blit(self.img, self.rect)
            self.pos = (self.pos[0], self.pos[1] + 20)    
        
