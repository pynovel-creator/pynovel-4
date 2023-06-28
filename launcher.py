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
            for option in run_text:
                if option[0].events(event) is not None:
                    subprocess.run("cd %s & run_game.py" % option[1].split("/run_game.py")[0], shell=True)
                    

    run_text = []

    for folder in os.listdir('.'):
        x, y = center
        if os.path.exists(pathjoin(folder, 'game')):
            if folder == "demo":
                run_text.append([ ctextbutton("Launch Tutorial/Demo", (x, y)), pathjoin(folder, "run_game.py") ])
            else:
                run_text.append([ ctextbutton(folder, (x, y)), pathjoin(folder, "run_game.py") ])
            y += 30
    text("Please select the game you may want to launch. The new game\n"
         "will open in a new window to avoid errors.", (20, 0))

    render()
 
    pygame.display.flip()
    
            
        