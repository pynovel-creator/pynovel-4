images["bg night meadow"] = "night_meadow.jpg"
    
images["girl happy"] = "girl_normal.png"
images["girl sad"] = "girl_sad.png"
images["girl upset"] = "girl_upset.png"
images["girl blushed"] = "girl_blushed.png"

movies["test mode"] = "countdown.mp4"

g = Character("Lily", color=(255, 0, 0, 0))

config.window_title = "New Game"
config.game_ver = (4, 3, 2)

class start_scene(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto()
    
    def update(self):
        pass
    
    def draw(self, surface):
        scene("white", surface)
        show('girl happy', surface)
        text("I'm Lily. Welcome to the default scene of this game. The script", "is game/script.py, open it in a text-editor.", pos=(20,470), surface=surface)
        say("Girl", surface, pos=(20,440))

class goto(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto_2()

    def update(self):
        pass
    
    def draw(self, surface):
        scene("bg night meadow", surface)
        show('girl happy', surface)
        text("I can demonstrate you some features now.", pos=(20,470), surface=surface)
        say(g, surface, pos=(20,440))

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
        scene("bg night meadow", surface)
        show('girl happy', surface, 'left')
        text("I can move to left.", pos=(20,470), surface=surface)
        say(g, surface, pos=(20,440))


class goto_3(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto_4()
        
    def update(self):
        pass
    
    def draw(self, surface):
        scene("bg night meadow", surface)
        show('girl happy', surface, 'right')
        text("..or right...", pos=(20,470), surface=surface)
        say(g, surface, pos=(20,440))

class goto_4(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto_5()
        
    def update(self):
        pass
    
    def draw(self, surface):
        scene("bg night meadow", surface=surface)
        show('girl happy', surface)
        text("And return to the default position.", pos=(20,470), surface=surface)
        say(g,surface, pos=(20,440))


class goto_5(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto_6()
        
    def update(self):
        pass
    
    def draw(self, surface):
        scene("bg night meadow", surface)
        show('girl happy', surface)
        text("And return to the default position.", pos=(20,470), surface=surface)
        say(g, surface=surface, pos=(20,440))

class goto_6(screen.Scene):
    
    def __init__(self):
        super().__init__()
        music_start('twinkle-twinkle-little-star.mid')

    def enter_next_scene(self):
        self.next_scene = goto_7()
        
    def update(self):
        pass
    
    def draw(self, surface):
        scene("bg night meadow", surface)
        show('girl happy', surface)
        text("I can play a music.", pos=(20,470), surface=surface)
        say(g, surface, pos=(20,440))

class goto_7(screen.Scene):
    
    def __init__(self):
        super().__init__()
        music_stop()

    def enter_next_scene(self):
        self.next_scene = goto_8()
        
    def update(self):
        pass
    
    def draw(self, surface):
        scene("bg night meadow", surface)
        show('girl happy', surface)
        text("I can stop it..", pos=(20,470), surface=surface)
        say(g, surface, pos=(20,440))

class goto_8(screen.Scene):
    
    def __init__(self):
        super().__init__()
    def enter_next_scene(self):
        self.next_scene = goto_last()
        
    def update(self):
        pass
    
    def draw(self, surface):
        scene("bg night meadow", surface)
        text("I can going off the screen by unshow me.", pos=(20,470), surface=surface)
        say(g, surface, pos=(20,440))

class goto_last(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = movie_start_scene()
        
    def update(self):
        pass
    
    def draw(self, surface):
        scene("bg night meadow", surface)
        show('girl happy', surface)
        text("Don't worry about me, I'm not gone anywhere now.", pos=(20,470), surface=surface)
        say(g, surface, pos=(20,440))

class movie_start_scene(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = movie_scene()
        
    def update(self):
        pass
    
    def draw(self, surface):
        scene("bg night meadow", surface=surface)
        show('girl happy', surface)
        if exists('countdown.mp4'):
            text("We also supported movie playing, let me play it now.", pos=(20,470), surface=surface)
        else:
            text("We also supported movie playing, but you haven't add a 'file.mp4'", "here, so I can't demonstrate it here.", pos=(20,470), surface=surface)
        say(g, surface, pos=(20,440))

class movie_scene(screen.Scene):
    
    def __init__(self):
        super().__init__()
        movie_start("test mode")

    def mouse_events(self, event):
        if self.return_button.events(event) is not None:
            self.next_scene = self.return_button.events(event)
        if self.end_button.events(event) is not None:
            quit()
        else:
            self.next_scene = self
        
    def update(self):
        pass

    def draw(self, surface):
        scene("bg night meadow", surface)
        show('girl happy', surface)
        text("That's enough for now. Do you want to restart?", pos=(20,470), surface=surface)
        self.return_button = ui.textbutton("Yes", (400, 300), surface, start_scene)
        self.end_button = ui.textbutton("No", (400, 330), surface, start_scene)
        say(g, surface, pos=(20,440))


