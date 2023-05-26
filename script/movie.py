import moviepy.editor
import pygame
from script.config import *

class Movie:

    # This is muted.

    def __init__(self, filename):
        self.video = moviepy.editor.VideoFileClip('game/' + filename).resize((screen_width, screen_height))
        self.video = self.video.resize((screen_width, screen_height))
        self.end = False

    def play(self):
        if not self.end:
            try:
                self.video.preview()
                self.end = False
            except:
                self.video.close()
                self.end = True

    def stop(self):
        self.video.close()
        self.end = True

    def get_frame(self):
        return round(self.video.fps * self.video.duration)
            
            
