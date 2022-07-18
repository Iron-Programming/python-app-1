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
        
    def update(self, screen):
        #cover = pygame.Rect(0, 0, globals['width'], globals['height'])
        #screen.blit(cover)
        pass

intervals = []

def addInterval(cb, dur):
    intervals.append(Interval(
        callback = cb,
        duration = dur
    ))
    