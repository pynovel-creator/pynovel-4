# Scenes state

class Scene(object):

    def __init__(self):
        super().__init__()
        self.next_scene = self

    def get_event(self, events):
        return "I'm sorry but these no events handle state."

    def update(self):
        return "There's no update state."

    def render(self):
        return "No rendering object or anything is added."

class Sprite(object):

    def __init__(self):
        self.images = []
        self.image = None
        self.rect = None

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def kill():
        self.image.set_alpha(0) # Transparent! By that the sprite has been erased from the screen.