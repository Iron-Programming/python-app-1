
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
    pass

# about/instructions page
def about():
    pass

# simulation page
def simulationPage():
    pass

# dictionary of keys
scenes = {
    'menu' : menu,
    'about' : about,
    'simulationGallery' : simulationGallery,
    'simulationPage' : simulationPage
}

addInterval(to_simulations, 1000)

# @function run_app : runs the app
def run_app():
    
    
    # infinite loop : controls main workflow
    while True:
        # calculate mouse position
        mouse_pos = pygame.mouse.get_pos()
        
        # draw the current scene
        scenes[globals['scene']]()
        
        # scene management
        for button in buttons:
            button.display(SCREEN, mouse_pos)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.isInside(mouse_pos):
                        button.clicked()
                        
        for interval in intervals:
            interval.update(SCREEN)
        
        # update scene
        pygame.display.update()

# run the app
run_app()