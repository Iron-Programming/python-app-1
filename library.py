# file : library.py
# contains classes, functions, and miscellaneous helper code

# included libraries
import pygame, sys
from button import *

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)