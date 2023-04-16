PyNovel 4.0.0
==================================================
The changed or anything you want to see.

Update
===================================================
It's still not had any choice yet since that time...

Preview
===================================================
![preview_img](https://user-images.githubusercontent.com/108453991/190960355-5b9bac79-7d09-40dc-a26b-2982961c65d3.png)

(The image is when I test the game UI customize.)

The demo is also added a sprite class example (I'm added again for those haven't known yet):

```py
# The sprite class example
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
        
 # The girl sprite.
 
 class Girl(manage.Sprite):
 
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image 
        self.rect = self.image.get_rect()
        self.rect.center = position["center"]

```

The game itself not contains a `pygame.sprite.Group()` based class, since the sprite class already has all features of sprite and group class. So if you want to include sprites repeatedly:

```py
# Try this (the example is taken idea from my game I create for test how I'm good at pygame)
# [...]
    if event.type == BIRD_COMING: # BIRD_COMING event will repeatedly running after 1 sec by pygame.time.set_timer (BIRD_COMING is an USEREVENT)
        self.new_bird = [Bird()]
        self.new_bird[0].draw(self.screen)
# [...]
