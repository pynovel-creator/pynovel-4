import os, sys

def buildmode():
    file = open(sys.argv[1]+'/run_game.py').readlines()
    window_configure = None
    console_configure = None
    for line in file:
        if line.startswith('#'):
            if 'build window' in line:
                window_configure = True
            if 'build console' in line:
                console_configure = True
    if window_configure:
        os.system('pyinstaller --onefile --windowed --distpath=%s %s/run_game.py' % (sys.argv[1]+'-dist', sys.argv[1]))
    else:
        os.system('pyinstaller --onefile --distpath=%s run_game.py' % str(sys.argv[1]+'-dist'))

def addingfile():
    os.chdir(sys.argv[1])
    if os.path.exists(sys.argv[1]+'/config.bat'):
        os.system("config.bat")
    else:
        print("config.bat file doesn't found in the directory\n"
              "maybe you was cloned a included game in the program.\n",
              "please copy the example one to your game and edit it.")

buildmode()
addingfile()
