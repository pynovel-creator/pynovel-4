import script, sys, time
from importlib import reload
from script.display.graphics import *
import script.ui as ui

import random

pygame.init()

# Eileen
eileen = {}

eileen["happy"] = Image('9a_happy.png')
eileen["vhappy"] = Image('9a_vhappy.png')
eileen["concerned"] = Image('9a_concerned.png')

bg = {}

bg['whitehouse'] = Image('whitehouse.jpg')

version = 'lazy_version'
next_scene = None

running = True

def ui_save(scene):
    print('Saved data at %s' % time.ctime())
    print('The current saved scene is %s' % str(scene.__name__))
    f = open('game/savegame', 'w')
    f.write(scene.__name__)
    f.close()

def ui_load():
    print('Loaded data at %s' % time.ctime())
    print('The current scene is %s' % str(scene.__name__))
    f = open('game/savegame').read()
    return exec(f)

def start_scene():
    global cur_scene
    screen.fill((255, 255, 255))
    scene(bg, 'whitehouse')
    show(eileen, "happy")
    ui.text("Hi, I'm Eileen.", (20, 480), box_mode=True)
    ui.say('Girl:', (20, 450))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                ui_save(start_scene)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                cur_scene = ui_load()
                reload(script)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                cur_scene = start_scene()
    pygame.display.flip()
    
clock = pygame.time.Clock()
while running:

    clock.tick(120)
    cur_scene = start_scene()

pygame.quit()
