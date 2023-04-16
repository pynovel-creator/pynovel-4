import pygame, sys
from pygame.locals import *
from python import *
pygame.init()
# Let's load all the important stuff by executing config.py.
exec(open('config.py', 'r').read())
class Girl(manage.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position["center"]

g = "Girl"

audio = {
    'sunflower slow drag': mixer_music.load('sunflower-slow-drag.ogg')
    }

# Finally, define a scene class.
class StartScene(manage.Scene):
    "The class started scene while you writing your own game."

    def __init__(self):
        super().__init__()
        self.girl = Girl(image["girl normal"])

    def get_event(self, events):
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.next_scene = SecondScene()
                    
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.next_scene = SecondScene()
                
    def update(self):
        self.girl.update()

    def render(self, surface):
        surface.fill(color["white"])
        surface.blit(scene["night meadow"], (0, 0))
        self.girl.draw(surface)
        text.Text([ "???", "Hi, I'm %s! I can be your template character for your mod!" % g ], (20, 440), surface)
        pygame.display.flip()

class SecondScene(manage.Scene):

    def __init__(self):
        super().__init__()
        self.girl = Girl(image["girl normal"])

    def get_event(self, events):
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.next_scene = ThirdScene()
                    
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.next_scene = ThirdScene()
                
    def update(self):
        self.girl.update()

    def render(self, surface):
        surface.fill(color["white"])
        surface.blit(scene["night meadow"], (0, 0))
        self.girl.draw(surface)
        text.Text([g, 'Welcome to the demo program.' ], (20, 440), surface)
        pygame.display.flip()

class ThirdScene(manage.Scene):

    def __init__(self):
        super().__init__()
        self.girl = Girl(image["girl upset"])

    def get_event(self, events):
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass
                
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    pass
                
    def update(self):
        self.girl.update()

    def render(self, surface):
        surface.fill(color["white"])
        surface.blit(scene["night meadow"], (0, 0))
        self.girl.draw(surface)
        text.Text([g, 'It is a bit upset to just only standing here alone...Why do not you add',
                   'some pictures, music, and your own story?' ], (20, 440), surface)
        pygame.display.flip()
class App:

    def __init__(self):
        self.scene = StartScene()
        self.canvas = window.screen.set_display((800, 600))
        window.screen.set_caption("NovelPy Window")
        self.running = True
        self.clock = pygame.time.Clock()
        mixer_music.play()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    print('Are you sure you want to exit the game?')
                    print('Yes/No')
                    choice = input('')
                    if choice in yes_command:
                        print('Loop breaked.')
                        self.running = False
                        pygame.quit()
                        sys.exit(0)
                    if choice in no_command:
                        print('Loop continued.')
                    else:
                        pass

            self.dt = int(self.clock.tick(60))
            self.scene.get_event(get_event.events())
            self.scene.render(self.canvas)
            self.scene.update()
            self.scene = self.scene.next_scene
            pygame.display.flip()
if __name__ == "__main__":
    app = App()
    app.run()
        
        
