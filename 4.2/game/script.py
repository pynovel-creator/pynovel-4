image["bg night meadow"] = ui.image("night_meadow.jpg")

image["girl happy"] = ui.image("girl_normal.png")
image["girl upset"] = ui.image("girl_upset.png")

def music_start(file, loops=-1):
    # Ensure that's in game/ directory
    return audio.audio.play(file, -1)

def music_stop():
    return audio.audio.stop()

# For the example, reveal girl's name.
g = Character("Lily", color=(255, 0, 0, 0))

class start_scene(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto()
    
    def update(self):
        pass
    
    def draw(self, surface):
        ui.scene("black", surface)
        ui.show('girl happy', surface)
        ui.box_appear(surface)
        ui.text("I'm Girl. Welcome to the default scene of this game. The script", (20, 470), surface)
        ui.text("is game/script.py. Press 'E' or 'S' to open it.", (20, 490), surface)
        ui.say("Girl", surface, (20, 440))

class goto(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto_2()

    def update(self):
        pass
    
    def draw(self, surface):
        ui.scene("bg night meadow", surface)
        ui.show('girl happy', surface)
        ui.box_appear(surface)
        ui.text("I can demonstrate you some features now.", (20, 470), surface)
        ui.say(g, surface, (20, 440))

class goto_2(screen.Scene):
    
    def __init__(self):
        super().__init__()
        
        
    def enter_next_scene(self):
        self.next_scene = goto_3()

    def events(self, event):
        pass

    def update(self):
        pass
    
    def draw(self, surface):
        ui.scene("bg night meadow", surface)
        ui.show('girl happy', surface, 'left')
        ui.box_appear(surface)
        ui.text("I can move to left.", (20, 470), surface)
        ui.say(g, surface, (20, 440))


class goto_3(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto_4()
        
    def update(self):
        pass
    
    def draw(self, surface):
        ui.scene("bg night meadow", surface)
        ui.show('girl happy', surface, 'right')
        ui.box_appear(surface)
        ui.text("..or right...", (20, 470), surface)
        ui.say(g, surface, (20, 440))

class goto_4(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto_5()
        
    def update(self):
        pass
    
    def draw(self, surface):
        ui.scene("bg night meadow", surface)
        ui.show('girl happy', surface)
        ui.box_appear(surface)
        ui.text("And return to the default position.", (20, 470), surface)
        ui.say(g, surface, (20, 440))


class goto_5(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        pass
        
    def update(self):
        pass
    
    def draw(self, surface):
        ui.scene("bg night meadow", surface)
        ui.show('girl happy', surface)
        ui.box_appear(surface)
        ui.text("And return to the default position.", (20, 470), surface)
        ui.say(g, surface, (20, 440))

class goto_5(screen.Scene):
    
    def __init__(self):
        super().__init__()
        music_start('twinkle-twinkle-little-star.mid')

    def enter_next_scene(self):
        self.next_scene = goto_6()
        
    def update(self):
        pass
    
    def draw(self, surface):
        ui.scene("bg night meadow", surface)
        ui.show('girl happy', surface)
        ui.box_appear(surface)
        ui.text("I can play a music.", (20, 470), surface)
        ui.say(g, surface, (20, 440))

class goto_6(screen.Scene):
    
    def __init__(self):
        super().__init__()
        music_stop()

    def enter_next_scene(self):
        self.next_scene = goto_7()
        
    def update(self):
        pass
    
    def draw(self, surface):
        ui.scene("bg night meadow", surface)
        ui.show('girl happy', surface)
        ui.box_appear(surface)
        ui.text("I can stop it..", (20, 470), surface)
        ui.say(g, surface, (20, 440))

class goto_7(screen.Scene):
    
    def __init__(self):
        super().__init__()
    def enter_next_scene(self):
        self.next_scene = goto_last()
        
    def update(self):
        pass
    
    def draw(self, surface):
        ui.scene("bg night meadow", surface)
        ui.box_appear(surface)
        ui.text("I can going off the screen by unshow me.", (20, 470), surface)
        ui.say(g, surface, (20, 440))

class goto_last(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = end_scene()
        
    def update(self):
        pass
    
    def draw(self, surface):
        ui.scene("bg night meadow", surface)
        ui.show('girl happy', surface)
        ui.box_appear(surface)
        ui.text("Don't worry about me, I'm not gone anywhere now.", (20, 470), surface)
        ui.say(g, surface, (20, 440))

class end_scene(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        pass
        
    def update(self):
        pass
    
    def draw(self, surface):
        ui.scene("bg night meadow", surface)
        ui.show('girl happy', surface)
        ui.box_appear(surface)
        ui.text("Thank you for viewing to the end, hope you fine.", (20, 470), surface)
        ui.say(g, surface, (20, 440))


