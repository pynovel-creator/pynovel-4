import os, subprocess
import sys, shutil


script_py_contents = [
    'config.screen_width = 800',
    'config.screen_height = 600',
    '',
    'config.window_title = "Quick Start"',
    '',
    'class start_scene(Scene):'
    '',
    '    def __init__(self):',
    '        super().__init__()',
    '',
    '    def enter_next_scene(self):',
    '        pass',
    '',
    '    def update(self):',
    '        pass',
    '',
    '    def draw(self, surface):',
    '        scene("black", surface)',
    '        text("Text goes here.", pos=(20, 440), surface=surface)',
    ]

includes = [
    "demo/script",
    "demo/build.bat",
    "demo/run_game.py",
    ]

quickstart_path = "template"

def clean():
    global quickstart_path
    shutil.rmtree(quickstart_path)

clean()

def copy(files=includes):
    for file in includes:
        try:
             shutil.copy2(file, os.path.join(quickstart_path, os.path.split(file)[1]))
        except:
             shutil.copytree(file, os.path.join(quickstart_path, os.path.split(file)[1]))            
        print('Added %s to %s' % (file, os.path.join(quickstart_path, os.path.split(file)[1])))
    print('Done.')
    return

def make(contents=script_py_contents):
    os.makedirs(os.path.join(quickstart_path, "game"))
    script = open(os.path.join(quickstart_path, "game", "script.py"), "w")
    for line in contents:
        print(line, file=script)
    print('Done.')

if __name__ == "__main__":
    copy()
    make()
