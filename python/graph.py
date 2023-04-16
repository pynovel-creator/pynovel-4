import pygame

def image(fn):
    try:
        return pygame.image.load('game/images/' + fn)
    except:
        return pygame.image.load('game' + fn)

def screenshot(surface):
    name = input("Please name the file please.\n")
    if name == "":
        name = "file"
    print("Saved!")
    pygame.image.save(name + ".png", surface)

def color(red=0, green=0, blue=0):
    return pygame.color.Color(red, green, blue)

def Rect(rect):
    return pygame.Rect(rect)

def draw_rect(surface, color, rect):
    return pygame.draw.rect(surface, color, rect)  
