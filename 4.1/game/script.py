image["eileen concerned"] = ui.image('9a_concerned.png')
image["eileen happy"] = ui.image('9a_happy.png')
image["bg washington"] = ui.image('washington.jpg')

def music_start(file, loops=-1):
    # Ensure that's in game/ directory
    return audio.audio.play(file, -1)

music_start('sun-flower-slow-drag.mid')

class start_scene(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto_washington()
    
    def update(self):
        pass
    
    def draw(self, surface):
        ui.scene("black", surface)
        ui.show('eileen happy', surface)
        ui.box_appear(surface)
        ui.text("I'm Eileen. Welcome to the default scene of this game. The script", (20, 470), surface)
        ui.text("is game/script.py. Press 'E' or 'S' to open it.", (20, 490), surface)
        ui.say("Girl", surface, (20, 440))

class goto_washington(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto_washington_2()

    def update(self):
        pass
    
    def draw(self, surface):
        ui.scene("bg washington", surface)
        ui.show('eileen happy', surface)
        ui.box_appear(surface)
        ui.text("This is Washington DC, is it beautiful?", (20, 470), surface)
        ui.say("Eileen", surface, (20, 440), (200, 255, 200))

class goto_washington_2(screen.Scene):
    
    def __init__(self):
        super().__init__()
        
        
    def enter_next_scene(self):
        self.next_scene = goto_washington_3()

    def events(self, event):
        pass

    def update(self):
        pass
    
    def draw(self, surface):
        ui.scene("bg washington", surface)
        ui.show('eileen happy', surface)
        ui.box_appear(surface)
        # No one is saying.
        ui.text("May I ask him/her name? Oh! wait, ui.input() haven't ready yet.", (20, 440), surface)


class goto_washington_3(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.next_scene = goto_whitehouse_standby()
        
    def update(self):
        pass
    
    def draw(self, surface):
        ui.scene("bg washington", surface)
        ui.show('eileen concerned', surface)
        ui.box_appear(surface)
        # No one is saying.
        ui.text("I wanted to ask for your name but can't let you enter text. If would be", (20, 470), surface)
        ui.text("bad. Sorry, about this bad news.", (20, 490), surface)
        ui.say("Eileen", surface, (20, 440), (200, 255, 200))

class goto_whitehouse_standby(screen.Scene):
    
    def __init__(self):
        super().__init__()

    def enter_next_scene(self):
        self.terminate()
        pygame.quit()
        sys.exit()
        
    def update(self):
        pass
    
    def draw(self, surface):
        ui.scene("black", surface)
        ui.show('eileen concerned', surface)
        ui.box_appear(surface)
        ui.text("Hey! You made my phone broken. What an unlucky day!", (20, 470), surface)
        ui.say("Eileen", surface, (20, 440), (200, 255, 200))



