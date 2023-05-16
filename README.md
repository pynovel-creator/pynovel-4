# Updated.
This version, 4.3 added choice and fullscreen.

# Code compare.

```py
# Old version
image["character name"] = ui.image("path/to/your/file.png")
# Current version.
image["character name"] = "path/to/your/file.png"
```

# Changed
Loading an image no longer needed the `ui.image()` function.
Just add it to the screen.

# Some common functions.

`Character(name, color)`

Name and color you want to use will be here.

`name`

Type a string inside it to add name.

`color`

The filled color of the name text.

`ui.say(object, pos, surface)`

The object can be a `Character()` object or a name, you can
load a character here to say.

`object`

`Character()` object or a string.

`pos`

Where the character name is placed.

`surface`

The screen will be load.

`ui.text(text, pos, surface)`

Text of the line. (You may have to multiply them.)

`text`

The line text info.

`pos`

Where the text is placed.

`surface`

The text is here.

`ui.image(name)`

The image will be loaded for scene and show.
You can skip this since you can show the image
without load it.

`name`

The file name, the default location is in 'game/'.

`ui.scene(name, surface)`

The scene view.

`name`

The key name of the loaded file in `image` dictionary
or stored a path to the file in string format in 
`image` dictionary. (If you type color in it,
you can fill the scene, if you aren't
call it the screen is red colored.

`surface`

We'll draw here.

`ui.show(name, surface, pos='center')`

Showing an character image.

`name`

Same as `ui.scene()` name paramenter.

`surface`

We will draw here.

`position`

We have 3 position for character and 1 for textbox.
Center (default)

`ui.box_appear(surface)`

The textbox

`surface`
We'll draw here.

`Scene`
The scene manager class.

`__init__()`

Defining here.

`update()`

Updating objects or redraw something here.

`events()`

The key events handler. (Jump to `enter_next_scene()` when dissmiss.)

`mouse_events()`

The mouse events handler. Clicking left button will dismiss the scene.

`draw()`

Draw anything here.

`enter_next_scene()`

The next scene is here.

`App`

Game class

`config.screen_width, config.screen_height`

The screen width and height, default is (0, 0).

`config.window_title, config.window_icon=None'

The game title, icon.

 `config.name, config.version`
 
 Nickname, and game version.


# Bug report
If you found any bug in it, post to https://github.com/pynovel-creator/pynovel-4/issues. 
I will fix it soon so you can play it or download the current code.
