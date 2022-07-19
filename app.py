
# get libraries, helper functions, and global definitions (globals)
from setup import *

# main menu
def menu():
    SCREEN.blit(BG, (0, 0))
    MENU_TEXT = get_font(100).render("Reality Simulator", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
    SCREEN.blit(MENU_TEXT, MENU_RECT)

# simulation gallery
def simulationGallery():
    SCREEN.blit(BG, (0, 0))

# about/instructions page
def about():
    SCREEN.blit(BG, (0, 0))

# simulation page
def simulationPage():
    SCREEN.blit(BG, (0, 0))

# dictionary of keys
scenes = {
    'menu' : menu,
    'about' : about,
    'simulationGallery' : simulationGallery,
    'simulationPage' : simulationPage
}

# @function run_app : runs the app
def run_app():
    
    
    # infinite loop : controls main workflow
    while True:
        # calculate mouse position
        mouse_pos = pygame.mouse.get_pos()
        
        # draw the current scene
        scenes[globals['scene']]()
        
        # scene management
        for button in buttons[globals['scene']]:
            button.display(SCREEN, mouse_pos)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons[globals['scene']]:
                    if button.isInside(mouse_pos):
                        button.clicked()
                        
        for interval in intervals:
            interval.update(SCREEN)

            if interval.done:
                intervals.remove(interval)

        
        # update scene
        pygame.display.update()

# run the app
run_app()