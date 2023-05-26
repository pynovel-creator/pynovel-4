from script import *
import sys, traceback

exec(open('game/script.py').read())
        
class App:

    def __init__(self):
        pygame.init()
        self.running = None
        self.scene = start_scene()
        self.screen = pygame.display.set_mode((config.screen_width, config.screen_height))
        
        pygame.display.set_caption(config.window_title)


    def events(self):
        for event in pygame.event.get():
            
            if event.type == QUIT:
                self.scene.terminate()
                quit()
                
            if event.type == KEYDOWN:
                if event.key in quit_key:
                    self.scene.terminate()
                    quit()
                if event.key in editor_key:
                    open_script('script.py')
                if event.key in fullscreen_key:
                    pygame.display.toggle_fullscreen()
                    fullscreen = True

                self.scene.events(event)
                
            if event.type == MOUSEBUTTONDOWN:
                self.scene.mouse_events(event)

    def draw(self):
        scene('black', self.screen)
        config.clock.tick(config.clock_tick)
        self.scene.update()
        self.scene.draw(self.screen)
        self.scene = self.scene.next_scene

    def running_game(self):
        self.running = True

        try:
            while self.running:

                self.draw()
                self.events()   
            
                pygame.display.flip()
        except:
            traceback.print_exc()

if __name__ == "__main__":
    App().running_game()
