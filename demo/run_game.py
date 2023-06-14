from script import *
import sys, traceback, codecs

init()

file = open(pathjoin('game', 'script.py')).read()
exec(file)

config.is_lastest_version()
config.window_title = "New Game"
    
class App:

    def __init__(self):
        self.running = None
        self.scene = start_scene()
        self.screen = makescreen()
        pygame.display.set_caption(window_title)

    def events(self):
        for event in pygame.event.get():
            
            if event.type == QUIT:
                self.scene.terminate()
                quit()
                
            if event.type == KEYDOWN:
                if event.key in quit_key:
                    self.scene.terminate()
                    quit()

                self.scene.events(event)
                
            if event.type == MOUSEBUTTONDOWN:
                self.scene.mouse_events(event)

    def draw(self):
        scene('black')
        config.clock.tick(config.clock_tick)
        self.scene.update()
        self.scene.draw()
        self.scene = self.scene.next_scene

    def running_game(self):
        self.running = True

        try:
            while self.running:

                self.events() 
                self.draw()  
            
                pygame.display.flip()
        except:
            traceback.print_exc()

if __name__ == "__main__":
    try:
         game = App()
         game_parser = game.running_game()
    except Exception as e:
         f = open('traceback.txt', 'w')
         print("I'm found an error while executing your script.py file, the error", file=f)
         print("made the game has stopped working.", file=f) 
         print(file=f)
         type, value, tb = sys.exc_info()
         print(type.__name__ + ":", f)
         traceback.print_exc(None, f)
         print(file=f)
         print("-------------------------------------- Begin traceback info --------------------------------------", file=f)
         traceback.print_exc(None, f)
         print(file=f)
         print('Game version : %s.%s.%s' % config.game_ver, file=f)
         f.close()
         os.system("traceback.txt")
