images["bg night meadow"] = "night_meadow.jpg"
    
images["girl happy"] = "girl_normal.png"
images["girl sad"] = "girl_sad.png"
images["girl upset"] = "girl_upset.png"
images["girl blushed"] = "girl_blushed.png"

movies["test mode"] = "countdown.mp4"

g = Character("Lily", color=(255, 0, 0, 0))

config.game_ver = (4, 3, 2)

user = ''

class start_scene(Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto()
    
    def update(self):
        pass
    
    def draw(self):
        scene("white")
        show('girl happy')
        text("I'm Lily. Welcome to the default scene of this game. The script\n" 
             "is game/script.py, open it in a text-editor.")
        say("Girl")

class goto(Scene):
    
    def __init__(self):
        super().__init__()
        self.input = input('Pov')
        self.user = ''

    def events(self, event):
        global user
        user = self.input.update(event)            

    def enter_next_scene(self):
        self.next_scene = goto_1_2()

    def update(self):
        pass
    
    def draw(self):
        scene("bg night meadow")
        show('girl happy')
        text("What's your name?")
        self.input.draw()
        say(g)

class goto_1_2(Scene):
    
    def __init__(self):
        super().__init__()
                
    def enter_next_scene(self):
        self.next_scene = goto_2()

    def events(self, event):
        pass

    def update(self):
        pass
    
    def draw(self):
        scene("bg night meadow")
        show('girl happy')
        text("Nice to meet you, %s" % user)
        say(g)

class goto_2(Scene):
    
    def __init__(self):
        super().__init__()
                
    def enter_next_scene(self):
        self.next_scene = goto_3()

    def events(self, event):
        pass

    def update(self):
        pass
    
    def draw(self):
        scene("bg night meadow")
        show('girl happy', 'left')
        text("I can move to left.")
        say(g)


class goto_3(Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto_4()
        
    def update(self):
        pass
    
    def draw(self):
        scene("bg night meadow")
        show('girl happy', 'right')
        text("..or right...")
        say(g)

class goto_4(Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto_5()
        
    def update(self):
        pass
    
    def draw(self):
        scene("bg night meadow")
        show('girl happy')
        text("And return to the default position.")
        say(g)


class goto_5(Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto_6()
        
    def update(self):
        pass
    
    def draw(self):
        scene("bg night meadow")
        show('girl happy')
        text("And return to the default position.")
        say(g)

class goto_6(Scene):
    
    def __init__(self):
        super().__init__()
        music_start('twinkle-twinkle-little-star.mid')

    def enter_next_scene(self):
        self.next_scene = goto_7()
        
    def update(self):
        pass
    
    def draw(self):
        scene("bg night meadow")
        show('girl happy')
        text("I can play a music.")
        say(g)

class goto_7(Scene):
    
    def __init__(self):
        super().__init__()
        music_stop()

    def enter_next_scene(self):
        self.next_scene = goto_8()
        
    def update(self):
        pass
    
    def draw(self):
        scene("bg night meadow")
        show('girl happy')
        text("I can stop it..")
        say(g)

class goto_8(Scene):
    
    def __init__(self):
        super().__init__()
    def enter_next_scene(self):
        self.next_scene = goto_last()
        
    def update(self):
        pass
    
    def draw(self):
        scene("bg night meadow")
        text("I can going off the screen by unshow me.")
        say(g)

class goto_last(Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = movie_start_scene()
        
    def update(self):
        pass
    
    def draw(self):
        scene("bg night meadow")
        show('girl happy')
        text("Don't worry about me, I'm not gone anywhere now.")
        say(g)

class movie_start_scene(Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = movie_end_scene()
        
    def update(self):
        pass
    
    def draw(self):
        scene("bg night meadow")
        show('girl happy')
        if exists('countdown.mp4'):
            text("We also supported movie playing, let me play it now.")
        else:
            text("We also supported movie playing, but you haven't add a 'file.mp4'\n" 
                 "here, so I can't demonstrate it here.")
        say(g)

class movie_end_scene(Scene):
    
    def __init__(self):
        super().__init__()
        movie_start("test mode")

    def mouse_events(self, event):
        if self.return_button.events(event):
            self.next_scene = start_scene()
        elif self.end_button.events(event):
            quit()
        else:
            self.next_scene = self
        
    def update(self):
        pass

    def draw(self):
        scene("bg night meadow")
        show('girl happy')
        text("That's enough for now. Do you want to restart?")
        self.return_button = textbutton("Yes")
        self.end_button = textbutton("No", (400, 330))
        say(g)


