import script.config
import script.ui
import pygame

from pygame.locals import *

pygame.init()

dismiss_key = [ K_RETURN, K_SPACE, 1 ]
choice_key = [ 1 ]
quit_key = [ K_ESCAPE, K_q ]

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
       self.surface = script.ui.makescreen()

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
       self.imagesprites.append(sprites)

   def remove(self, *sprites):
       self.imagesprites.remove(sprites)

   def update(self):
       for sprite in self.imagesprites:
           sprite.update()

   def draw(self):
       for sprite in self.imagesprites:
           sprite.draw()

   def sprites(self):
       return self.imagesprites

   def has(self, *sprites):
       if sprites in self.imagesprites:
           return True
       else:
           return False

   def clear(self, color):
       for sprite in self.imagesprites:
           sprite.image.fill(color)

   def empty(self):
       for sprite in self.imagesprites:
           sprite.kill()
           self.imagesprites.remove(sprite)
   

   
