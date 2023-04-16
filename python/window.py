import pygame

class Canvas:

    pygame.display.init()

    def set_display(self, size, depth=32, flags=0):
        return pygame.display.set_mode(size, flags, depth)

    def set_caption(self, caption, icontitle=''):
        return pygame.display.set_caption(caption, icontitle)

    def set_icon(self, surface):
        return pygame.display.set_icon(surface)
        
screen = Canvas()