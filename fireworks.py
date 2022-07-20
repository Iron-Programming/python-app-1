import pygame
from library import *

g1 = {
    'mapX' : globals['width']/2,
    'mapY' : globals['height'] - 250,
    'mapWidth' : 400,
    'mapHeight' : 400
}

# temporary
pygame.init()

# set app name
pygame.display.set_caption("Final Project")

# load background image
BG = pygame.image.load("assets/background.jpg")

def fireworks():
    MENU_TEXT = get_font(90).render("Fireworks", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(globals['width']/2, 100))
    SCREEN.blit(MENU_TEXT, MENU_RECT)

    addRect(globals['width']/2, g1['mapY'], globals['width'], globals['height'] - 200, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # START OF WORK AREA

    # END OF WORK AREA

    # temporary
    pygame.display.update()

# temporary
while True:
    fireworks()