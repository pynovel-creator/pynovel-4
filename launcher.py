import os, sys, subprocess
import pygame
from script import *
init()

launcher_script = open('game/script.py')
exec(launcher_script.read())

newscreen = makenewscreen()
pygame.display.set_caption(config.window_title)

while True:

    screen.fill((150, 150, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        
        if event.type == MOUSEBUTTONDOWN:
            for option in buttons:
                if option[0].events(event) is not None:
                    if os.path.exists(option[1]):
                        subprocess.run("cd %s & run_game.py" % option[1].split("/run_game.py")[0], shell=True)
                    else:
                        print("%s was not found while launching the game please\n" 
                              "download a new one instead." % option[1])
                    

    left, top = (100, 151)
    buttons = [] 
    for folder in os.listdir('.'):
        if os.path.isdir(folder + '/game'):
            f = open(folder + '/project.py').read()
            exec(f)
            buttons.append([ ctextbutton(info["project_name"] + " (" + info["project_version"] + ")", (left, top)), folder + '/run_game.py' ])
            top += 30
    text("Please select the game you may want to launch. The new game\n"
         "will open in a new window to avoid errors.", (20, 0))

    render()
 
    pygame.display.flip()
    
            
        
