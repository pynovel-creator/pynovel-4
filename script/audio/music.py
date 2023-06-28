try:
    import pygame.mixer
    pygame.mixer.init()
except ImportError:
    import moviepy.editor
    audio = "no audio"

def play(filename, loops=0):
    global audio
    try:
        pygame.mixer.music.load('game/' + filename)
        pygame.mixer.music.play(loops)
    except:
        audio = moviepy.editor.AudioFileClip('game/' + filename)
        try:
            audio.preview()
        except:
            audio.close()

def stop():
    global audio
    try:
        pygame.mixer.music.stop()
    except:
        audio.close()
