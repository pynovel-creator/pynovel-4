import script.config
import script.ui
import pygame

from pygame.locals import *

pygame.init()

dismiss_key = [ K_RETURN, K_SPACE, 1 ]
choice_key = [ 1 ]
quit_key = [ K_ESCAPE]

class Scene:
    
    def __init__(self):
        self.next_scene = self
        
    def events(self, event):
        if event.key in dismiss_key:
            self.enter_next_scene()

    def mouse_events(self, event):
        if event.button in dismiss_key:
            self.enter_next_scene()
            
    def enter_next_scene(self):
        self.next_scene = self
    
    def update(self):
        raise NotImplementedError
    
    def draw(self, surface):
        raise NotImplementedError

    def terminate(self):
        self.next_scene = None

class Sprite:

   def __init__(self):
       self.images = [pygame.Surface((script.config.screen_width / 2, script.config.screen_height / 2))]
       self.image = self.images[0]
       self.rect = self.image.get_rect()

   def update(self):
       pass

   def draw(self):
       script.ui.screen.blit(self.image, self.rect)

   def kill(self):
       self.image.set_alpha(0)

class Group:

   def __init__(self):
       self.imagesprites = []

   def add(self, *sprites):
       for sprite in sprites:
           self.imagesprites.append(sprite)

   def remove(self, *sprites):
       for sprite in sprites:
           self.imagesprites.remove(sprite)

   def update(self):
       for sprite in self.imagesprites:
           sprite.update()

   def draw(self):
       for sprite in self.imagesprites:
           sprite.draw()
   

   
