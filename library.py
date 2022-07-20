# file : library.py
# contains classes, functions, and miscellaneous helper code

# included libraries
import pygame, sys
from button import *

# global definitions (multi-file)
globals = {
    'scene' : 'menu',
    'width' : 1280,
    'height' : 720
}

def get_font(size, name="lemon_days"): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/" + name + ".ttf", size)


# timed intervals (switching scenes)
class Interval():
    def __init__(self, **config):
        # button graphic
        self.callback = config['callback']
        self.duration = config['duration']
        self.cover = pygame.Surface((globals['width'], globals['height']))
        self.alpha = 0
        self.direction = "forward"
        self.done = False
        
    def update(self, screen):
        if self.direction == "forward":
            self.alpha += (255 - self.alpha) / (self.duration / 2)

            if (255 - self.alpha < 0.01):
                self.direction = "backward"
                self.callback()
        elif self.direction == "backward":
            self.alpha += (0 - self.alpha) / (self.duration / 2)

            if (self.alpha < 0.01):
                self.done = True
        
        self.cover.set_alpha(self.alpha)
        self.cover.fill((0, 0, 0))
        screen.blit(self.cover, (0, 0))


intervals = []

def addInterval(cb, dur, **kwargs):
    intervals.append(Interval(
        callback = cb,
        duration = dur
    ))
    