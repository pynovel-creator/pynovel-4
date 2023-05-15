from script import *
import sys, time, traceback, os

class ExceptionScene(screen.Scene):
    
    def __init__(self):
        super().__init__()
        os.startfile("traceback.txt")

    def update(self):
        pass
    
    def draw(self, surface):
        ui.text("I'm sorry but we caught an unexpected exception has occured.", (20, 0), surface)

exec(open('game/script.py').read())            

class App:

    def __init__(self):
        pygame.init()
        
        try:
            self.scene = start_scene()
            if os.path.exists("traceback.txt"):
                os.remove("traceback.txt")
        except:
            traceback.print_exc(file=open("traceback.txt", 'w'))
            self.scene = ExceptionScene()
            open_script('script.py')
        
        config.screen_width = 800
        config.screen_height = 600
        
        config.window_title = "Test Game"
        
        self.screen = pygame.display.set_mode((config.screen_width, config.screen_height))
        
        pygame.display.set_caption(config.window_title)
        
        config.clock_tick = 60

    def events(self):
        for event in pygame.event.get():
            
            if event.type == QUIT:
                self.scene.terminate()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key in screen.editor_key:
                    open_script('script.py')

                self.scene.events(event)
                
            if event.type == MOUSEBUTTONDOWN:
                self.scene.mouse_events(event)

    def draw(self):
        self.screen.fill((255, 0, 0))
        config.clock.tick(config.clock_tick)
        try:
            self.scene.update()
            self.scene.draw(self.screen)
            self.scene = self.scene.next_scene
        except:
            traceback.print_exc(file=open("traceback.txt", 'w'))
            self.scene = ExceptionScene()            
            self.scene.update()
            self.scene.draw(self.screen)
            self.scene = self.scene.next_scene        
    def running(self):
        running = True
        
        while running:
         
            self.draw()
            self.events()   
            
            pygame.display.flip()

if __name__ == "__main__":
    App().running()
