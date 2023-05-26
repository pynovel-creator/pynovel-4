images["bg night meadow"] = "night_meadow.jpg"
images["girl happy"] = "girl_normal.png"
images["girl upset"] = "girl_upset.png"

movies["test mode"] = "bigbuckbunny.mp4"

g = Character("Lily", color=(255, 0, 0, 0))

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
        box_appear(surface)
        text("I'm Lily. Welcome to the default scene of this game. The script", (20, 470), surface)
        text("is game/script.py. Press 'E' or 'SHIFT' to open it.", (20, 490), surface)
        say("Girl", surface, (20, 440))

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
        box_appear(surface)
        text("I can demonstrate you some features now.", (20, 470), surface)
        say(g, surface, (20, 440))

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
        box_appear(surface)
        text("I can move to left.", (20, 470), surface)
        say(g, surface, (20, 440))


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
        box_appear(surface)
        text("..or right...", (20, 470), surface)
        say(g, surface, (20, 440))

class goto_4(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto_5()
        
    def update(self):
        pass
    
    def draw(self, surface):
        scene("bg night meadow", surface)
        show('girl happy', surface)
        box_appear(surface)
        text("And return to the default position.", (20, 470), surface)
        say(g, surface, (20, 440))


class goto_5(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        pass
        
    def update(self):
        pass
    
    def draw(self, surface):
        scene("bg night meadow", surface)
        show('girl happy', surface)
        box_appear(surface)
        text("And return to the default position.", (20, 470), surface)
        say(g, surface, (20, 440))

class goto_5(screen.Scene):
    
    def __init__(self):
        super().__init__()
        music_start('twinkle-twinkle-little-star.mid')

    def enter_next_scene(self):
        self.next_scene = goto_6()
        
    def update(self):
        pass
    
    def draw(self, surface):
        scene("bg night meadow", surface)
        show('girl happy', surface)
        box_appear(surface)
        text("I can play a music.", (20, 470), surface)
        say(g, surface, (20, 440))

class goto_6(screen.Scene):
    
    def __init__(self):
        super().__init__()
        music_stop()

    def enter_next_scene(self):
        self.next_scene = goto_7()
        
    def update(self):
        pass
    
    def draw(self, surface):
        scene("bg night meadow", surface)
        show('girl happy', surface)
        box_appear(surface)
        text("I can stop it..", (20, 470), surface)
        say(g, surface, (20, 440))

class goto_7(screen.Scene):
    
    def __init__(self):
        super().__init__()
    def enter_next_scene(self):
        self.next_scene = goto_last()
        
    def update(self):
        pass
    
    def draw(self, surface):
        scene("bg night meadow", surface)
        box_appear(surface)
        text("I can going off the screen by unshow me.", (20, 470), surface)
        say(g, surface, (20, 440))

class goto_last(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = video_start_scene()
        
    def update(self):
        pass
    
    def draw(self, surface):
        scene("bg night meadow", surface)
        show('girl happy', surface)
        box_appear(surface)
        text("Don't worry about me, I'm not gone anywhere now.", (20, 470), surface)
        say(g, surface, (20, 440))

class video_start_scene(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = movie_scene()
        
    def update(self):
        pass
    
    def draw(self, surface):
        scene("bg night meadow", surface)
        show('girl happy', surface)
        box_appear(surface)
        if exists('bigbuckbunny.mp4'):
            text("We also supported movie playing, let me play it now.", (20, 470), surface)
        else:
            text("We also supported movie playing, but you haven't add a 'file.mp4'", (20, 470), surface)
            text("here, so I can't demonstrate it here.", (20, 490), surface)
        say(g, surface, (20, 440))

class movie_scene(screen.Scene):
    
    def __init__(self):
        super().__init__()
        movie_start("test mode")

    def mouse_events(self, event):
        if self.return_button.events is not None:
            self.next_scene = self.return_button.events(event)
        else:
            quit()

    def enter_next_scene(self):
        pass
        
    def update(self):
        pass

    def draw(self, surface):
        scene("bg night meadow", surface)
        show('girl happy', surface)
        box_appear(surface)
        text("That's enough for now. Do you want to restart?", (20, 440), surface)
        self.return_button = ui.textbutton("Return", (20, 470), surface, start_scene)


