import pygame
import math
import random
from library import *

g1 = {
    'mapX' : globals['width']/2,
    'mapY' : globals['height'] - 250,
    'mapWidth' : 400,
    'mapHeight' : 400
}

particleColor = (0, 0, 200) # color of the particles
numPoints = 250 # of points int he program
speed = 1 # how fast the points move
timer = 0

class Point():
    def __init__(self, **config):
        self.x = config['x']
        self.y = config['y']
        self.xVel = 0
        self.yVel = 0
        self.speed = speed * random.uniform(0.3, 1)
        self.slope = 0
    
    def update(self):
        self.slope = slopeField(self.x - g1['mapX'], self.y - g1['mapY'])

        self.xVel = self.speed
        self.yVel = self.slope * self.speed

        self.x += self.xVel
        self.y += self.yVel
    
    def display(self):
        pygame.draw.ellipse(SCREEN, (0, 255, 0), (self.x, self.y, 10, 10))

points = []

for i in range (0, numPoints):
    points.append(Point(
        x = random.uniform(g1['mapX'] - g1['mapWidth']/2, g1['mapX'] + g1['mapWidth']/2),
        y = random.uniform(g1['mapY'] - g1['mapHeight']/2, g1['mapY'] + g1['mapHeight']/2)
    ))

def slopeField(x, y):
    dxDy = -math.cos(x/25)
    return dxDy

def vectorSlopeField():
    '''MENU_TEXT = get_font(90).render("Vector Slope Field", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(globals['width']/2, 100))
    SCREEN.blit(MENU_TEXT, MENU_RECT)

    addRect(globals['width']/2, g1['mapY'], globals['width'], globals['height'] - 200, (255, 255, 255))'''


    # WORK AREA
    for x in range(-200, 200, 25):
        for y in range(-250, 250, 25):
            slope = slopeField(x, y)
            addLine(g1['mapX'] + x - 1, g1['mapY'] + y - slope, g1['mapX'] + x + 1, g1['mapY'] + y + slope, 3, (0, 0, 0))

    global timer
    timer += 1
    if timer > 2:
        points.append(Point(
            x = random.uniform(g1['mapX'] - 235, g1['mapX'] - 230),
            y = random.uniform(g1['mapY'] - 200, g1['mapY'] + 200)
        ))
        timer = 0

    for p in points:
        p.display()
        p.update()
        if p.x > g1['mapX'] + g1['mapWidth']:
            points.remove(p)
    
    addRect((g1['mapX'] - g1['mapWidth']/2)/2.2, g1['mapY'] - 10, g1['mapX'] - g1['mapWidth']/2, globals['height'] - 200, (200, 200, 200))
    addRect(globals['width'] - (g1['mapX'] - g1['mapWidth']/2)/2, g1['mapY'] - 10, g1['mapX'] - g1['mapWidth']/2, globals['height'] - 200, (200, 200, 200))
    # END OF WORK AREA1