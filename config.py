# To use a file in game.py, use exec(open(<filename>.py, 'r').read()) in your game.py to initalizing your game.

# Loading the image.
image = {
    'girl normal': graph.image("girl_normal.png"),
    'girl sad': graph.image("girl_sad.png"),
    'girl upset': graph.image("girl_upset.png"),
    'girl blushed': graph.image("girl_blushed.png")
    }
yes_command = [ "yes", "Yes", "Y", "y"]
no_command = [ "No", "no", "N", "n"]

# Don't ignore this!
scene = {
    'night meadow': graph.image("night_meadow.jpg")
    }

# This different with the RGB values in in-game init (because this is generated values of them.)
color = {
    'black': (0, 0, 0, 255),
    'white': (255, 255, 255, 255)
    }
# Position. (I'm not sure if I type the position right...)
position = {
    'left': (200, 300),
    'center': (400, 300),
    'right': (600, 300)
    }
