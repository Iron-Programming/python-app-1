
# include libraries we use for the game
import pygame, sys
from button import *

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

# @function run_app : runs the app
def run_app():
    
    
    # infinite loop : controls main workflow
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()


        buttons.append(Button(
            image = pygame.image.load("assets/Play Rect.png"),
            pos = (640, 250), 
            text_input = "PLAY",
            font = get_font(75),
            base_color = "#d7fcd4",
            hovering_color = "White"
            #click_effect = lambda : play()
        ))

        buttons.append(Button(
            image = pygame.image.load("assets/Options Rect.png"),
            pos = (640, 400), 
            text_input = "OPTIONS",
            font = get_font(75),
            base_color = "#d7fcd4",
            hovering_color = "White"
            #click_effect = lambda : options()
        ))

        def endGame():
            pygame.quit()
            sys.exit()
        buttons.append(Button(
            image = pygame.image.load("assets/Quit Rect.png"),
            pos = (640, 550), 
            text_input = "QUIT",
            font = get_font(75),
            base_color = "#d7fcd4",
            hovering_color = "White"
            #click_effect = lambda : endGame()
        ))

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        
        for button in buttons:
            button.changeColor(MENU_MOUSE_POS)
            button.display(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.isInside(MENU_MOUSE_POS):
                        button.clicked()

        pygame.display.update()

run_app()