import pygame

def events():
    return pygame.event.get()

def pump():
    return pygame.event.pump()

def single_event():
    return pygame.event.poll()

def wait():
    return pygame.event.wait()

def peek():
    return pygame.event.peek()

def reset():
    return pygame.event.clear()

def name(type):
    return pygame.event.event_name()

def allowed(type=None):
    return pygame.event.set_allowed(type)

def blocked(type=None):
    return pygame.event.set_blocked(type)
    
    