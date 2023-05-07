import script.display.graphics as graphics

graphics.pygame.init()

load_sysfont = graphics.pygame.font.SysFont
load_font = graphics.pygame.font.Font
        
def text(text, pos, box_mode=False):
    if box_mode:
        box_surf = graphics.pygame.Surface((800, 150), graphics.pygame.SRCALPHA)
        box_img = graphics.image('game/frame.png')
        box_rect = box_img.get_rect(topleft=(pos[0]-20, pos[1]-40))
        graphics.screen.blit(box_img, (pos[0]-20, pos[1]-40))
        graphics.screen.blit(box_surf, (pos[0]-20, pos[1]-40))
        if box_rect.collidepoint(graphics.pygame.mouse.get_pos()):
            box_img = graphics.image('game/frame-hover.png')
            graphics.screen.blit(box_img, (pos[0]-20, pos[1]-40))
    font = load_sysfont('dejavu-sans', 22)
    text_surf = font.render(text, True, graphics.pygame.Color('black'))
    rect = text_surf.get_rect()
    rect.topleft = (pos[0]+2, pos[1]+2)
    graphics.screen.blit(text_surf, rect)
    text_surf = font.render(text, True, graphics.pygame.Color('white'))
    rect = text_surf.get_rect()
    rect.topleft = pos
    graphics.screen.blit(text_surf, rect)

def say(text, pos, col='white'):
    font = load_sysfont('dejavu-sans', 22, bold=True)
    text_surf = font.render(text, True, graphics.pygame.Color('black'))
    rect = text_surf.get_rect()
    rect.topleft = (pos[0]+2, pos[1]+2)
    graphics.screen.blit(text_surf, rect)
    text_surf = font.render(text, True, graphics.pygame.Color(col))
    rect = text_surf.get_rect()
    rect.topleft = pos
    graphics.screen.blit(text_surf, rect)


def _text(text, pos):
    print('Testing...')
    return text(text, pos)

def error(text):
    print('An unlucky exception has been caught.')
    print(('Exception handled: ' + str(e)))
    return
