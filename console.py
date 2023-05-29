from script import *
import os, sys

def execfile(filename, globals=None, locals=None):
    
    if globals is None:
        globals = {}

    globals.update({
            "__file__": filename,
            "__main__": "__main__"
        })
    with open(filename, 'r') as f:
        compiled = compile(f.read(), filename, 'exec')
        exec(compiled, globals, locals)

def main():

    sys_args = [ ("--game", "-g") ,
                 ("--file", "-f") ]

    if len(sys.argv) > 1:
        if sys.argv[1] in sys_args[0]:
            os.system("run_game.py")

        if sys.argv[1] in sys_args[1]:
            f = open('file.txt', 'w')
            image_count = 0
            script_count = 0
            sound_object_count = 0
            for filename in os.listdir('game'):
                if filename.endswith('.png') or filename.endswith('.jpg'):
                    image_count += 1
                if filename.endswith('.py'):
                    script_count += 1
                if filename.endswith('.mp3') or filename.endswith('.wav') or filename.endswith('.mid') or filename.endswith('.midi') or filename.endswith('.mp4'):
                    sound_object_count += 1
            print('There is ' + str(image_count) + ' files, ' + str(script_count) + ' scripts and', file=f)
            print(str(sound_object_count) + ' audio, music, sound and video in totals.', file=f)
            print(file=f)
            print('This tools is not a fine idea for testing.', file=f)
            print(file=f)
            print('Game version : %s.%s.%s' % config.game_ver, file=f)
            f.close()
            os.system("file.txt")
    else:
        os.system("run_game.py")

if __name__ == "__main__":
    main()
    
