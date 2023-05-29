import script

# This isn't necessary.
#mouse_visible = True

# The screen resolution.
screen_width = 800
screen_height = 600
fullscreen = True

# The program title.
window_title = 'A new window'
window_icon = None

# FPS clock.
clock = script.pygame.time.Clock()
clock_tick = 0

# Script version.
game_script_version = (4, 3, 2)
game_ver = (4, 3, 2)
pause_msg = 'Do you want to continue? Y/N'

def is_lastest_version():
    global game_ver, game_script_version, pause_msg
    if game_ver < game_script_version:
        print('You are running an old version of the game, it is very unsafe')
        print('to continue.')
        ans = input(pause_msg)
        if ans in ['y','Y']:
            game_ver = game_script_version
            return True
        else:
            print('I am happy because you do not do that.')
            raise Exception('script.config: Script version is outdated, please remove it or rewrite it (change into current script).')
    else:
        return True
    
