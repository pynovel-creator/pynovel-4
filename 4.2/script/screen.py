import script.config
import pygame

from pygame.locals import *

pygame.init()

dismiss_key = [ K_RETURN, K_SPACE, 1 ]
editor_key = [ K_e, K_LSHIFT, K_RSHIFT ]
choice_key = [ 1 ]
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
