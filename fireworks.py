################## LIBRARIES ##################
from logging import NullHandler
import pygame
import random
from library import *
from vector import *
import numpy as np

################## SIMULATION AREA VARIABLES ##################
g1 = {
    'mapX' : globals['width']/2,
    'mapY' : globals['height'] - 250,
    'mapWidth' : 400,
    'mapHeight' : 400
}
fireworks = []
gravity = vec['new'](0, 0.125)
timer = 0

################## PARTICLE CLASS ##################
class Particle():
    # Particle Constructor
    def __init__(self, x, y, hue, firework, i, choice):
        self.pos = vec['new'](x, y)
        if firework:
            self.vel = vec['new'](0, random.uniform(-6, -10))
        else: 
            # determines how the firework explodes
            if choice < 1:
                x = random.uniform(-4, 4)
                y = random.uniform(-4, 4)
            elif choice < 2:
                angle = map(i, 0, 100, 0, 360)
                x = math.cos(angle) * 5
                y = math.sin(angle) * 5
            else:
                theta = np.linspace(0, 2 * np.pi, 100)
                x = (16 * np.sin(theta[i]) ** 3) / 5
                y = -(13 * np.cos(theta[i]) - 5 * np.cos(2*theta[i]) - 2 * np.cos(3*theta[i]) - np.cos(4*theta[i]))/5

            self.vel = vec['new'](x, y)
        self.acc = vec['new'](0, 0)
        self.lifespan = 255
        self.hue = hue

    # applies a force to a Particle by adding a vector to its acceleration
    def applyForce(self, force):
        self.acc = vec['addVector'](self.acc, force)
    
    # updates the Particle
    def update(self):
        self.vel = vec['addVector'](self.vel, self.acc)
        self.pos = vec['addVector'](self.pos, self.vel)
        self.acc = vec['mult'](self.acc, 0)

    # draw the Particle
    def show(self):
        surface1 = pygame.Surface((5, 5))
        surface1.set_alpha(self.lifespan)
        pygame.draw.circle(surface1, self.hue, (0, 0), 5)
        SCREEN.blit(surface1, (self.pos['x'], self.pos['y']))

################## FIRE WORK CLASS ##################
class Firework():
    # Firework Constructor
    def __init__(self):
        self.hue = (random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))
        self.firework = Particle(random.uniform(0, globals['width']), globals['height'], self.hue, True, 0, None)
        self.exploded = False
        self.particles = []

    # Explodes the Firework into a specific pattern (see Particle Class)
    def explode(self):
        choice = random.uniform(0, 3)
        for i in range(0, 100):
            self.particles.append(Particle(
                self.firework.pos['x'],
                self.firework.pos['y'],
                self.hue,
                False,
                i,
                choice
            ))
    
    # Updates and displays the firework
    def update(self):
        if self.exploded != True:
            self.firework.applyForce(gravity)
            self.firework.update()

            if self.firework.vel['y'] >= 0:
                self.exploded = True
                self.explode()
        else:
            for particle in self.particles:
                particle.applyForce(gravity)
                particle.update()
    
    # display the firework
    def show(self):
        if self.exploded != True:
            self.firework.show()

        for particle in self.particles:
            particle.show()
            particle.lifespan -= 5

            if particle.lifespan <= 20:
                self.particles.remove(particle)

# firework program
def fireworksProgram():

    # black background
    addRect(globals['width']/2, g1['mapY'] - 10, globals['width'], globals['height'] - 200, (0, 0, 0))

    # add fireworks
    if random.uniform(0, 1) < 0.05:
        fireworks.append(Firework())

    # draw each firework
    for firework in fireworks:
        firework.update()
        firework.show()

        if firework.exploded and len(firework.particles) == 0:
            fireworks.remove(firework)
    