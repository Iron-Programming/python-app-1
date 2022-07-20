import pygame
from library import *

# equation: 0.60x^8 − 2.52x^7 + 0.42x^6 + 8.26x^5 − 5.10x^4 − 7.72x^3 + 4.46x^2 + 1.70x
equation = {
    'coeffecients': [0.6, -2.52, 0.42, 8.26, -5.1, -7.72, 4.46, 1.7],
    'exponents' : [8, 7, 6, 5, 4, 3, 2, 1],
    'color' : (255, 0, 0)
}

# where the taylor series is centered at
# At center = 0 we have a Maclaurin Series
center = 0

# the number of terms in the series
numTerms = 1

def factorialize(num):
    if (num < 0):
        return -1
    elif num == 0:
        return 1
    else:
        return num * factorialize(num - 1)

def returnValue(terms, X):
    x = center

    # list of derivatives
    derivatives = [
        # original (equation)
        0.6 * x ** 8 - 2.52 * x ** 7 + 0.42 * x ** 6 + 8.26 * x ** 6 - 5.1 * x ** 4 - 7.72 * x ** 3 + 4.46 * x ** 2 + 1.7 * x,
        # first
        8 * 0.6 * x ** 7 - 7 * 2.52 * x ** 6 + 6 * 0.42 * x ** 5 + 5 * 8.26 * x ** 4 - 4 * 5.1 * x ** 3 - 3 * 7.72 * x ** 2 + 2 * 4.46 * x + 1.7,
        # second
        56 * 0.6 * x ** 6 - 42 * 2.52 * x ** 5 + 30 * 0.42 * x ** 4 + 20 * 8.26 * x ** 3 - 12 * 5.1 * x ** 2 - 6 * 7.72 * x + 2 * 4.46,
        # third
        6 * 56 * 0.6 * x ** 5 - 5 * 42 * 2.52 * x ** 4 + 120 * 0.42 * x ** 3 + 60 * 8.26 * x ** 2 - 24 * 5.1 * x - 6 * 7.72,
        # fourth
        30 * 56 * 0.6 * x ** 4 - 20 * 42 * 2.52 * x ** 3 + 360 * 0.42 * x ** 2 + 120 * 8.26 * x - 24 * 5.1,
        # fifth
        120 * 56 * 0.6 * x ** 3 - 60 * 42 * 2.52 * x ** 2 + 720 * 0.42 * x + 120 * 8.26,
        # sixth
        360 * 56 * 0.6 * x ** 2 - 120 * 42 * 2.52 * x + 720 * 0.42,
        # seventh
        720 * 56 * 0.6 * x - 120 * 42 * 2.52,
        # eigth
        720 * 56 * 0.6,
        # ninth
        0
    ]

def addLine():
    pygame.draw.line(SCREEN, "#b68f40", (globals['width']/2 - 400, 155), (globals['width']/2 + 400, 155), width=5)

def taylorSeries():
    pass


# temporary

