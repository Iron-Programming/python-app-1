
# get libraries, helper functions, and global definitions (globals)
#from pyparsing import null_debug_action
from setup import *

# main menu
def menu():
    SCREEN.blit(BG, (0, 0))
    MENU_TEXT = get_font(90).render("Reality Simulator", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(globals['width']/2, 100))
    SCREEN.blit(MENU_TEXT, MENU_RECT)

# simulation gallery
def simulationGallery():
    SCREEN.blit(BG, (0, 0))
    TITLE_TEXT = get_font(90).render("Simulation Gallery", True, "#b68f40")
    TITLE_RECT = TITLE_TEXT.get_rect(center=(globals['width']/2, 100))
    pygame.draw.line(SCREEN, "#b68f40", (globals['width']/2 - 400, 155), (globals['width']/2 + 400, 155), width=5)
    SUBTITLE_TEXT = get_font(50, "philosopher").render("Pick a Simulation", True, "#b68f40")
    SUBTITLE_RECT = SUBTITLE_TEXT.get_rect(center=(globals['width']/2, 185))

    MATH = get_font(30, "philosopher").render("Math", True, "#b68f40")
    MATH_RECT = MATH.get_rect(center=(190, 350))

    CHEMISTRY = get_font(30, "philosopher").render("Chemistry", True, "#b68f40")
    CHEMISTRY_RECT = CHEMISTRY.get_rect(center=(490, 350))

    PHYSICS = get_font(30, "philosopher").render("Physics", True, "#b68f40")
    PHYSICS_RECT = PHYSICS.get_rect(center=(790, 350))

    ASTRONOMY = get_font(30, "philosopher").render("Astronomy", True, "#b68f40")
    ASTRONOMY_RECT = ASTRONOMY.get_rect(center=(1090, 350))
    
    SCREEN.blit(TITLE_TEXT, TITLE_RECT)
    SCREEN.blit(SUBTITLE_TEXT, SUBTITLE_RECT)
    SCREEN.blit(MATH, MATH_RECT)
    SCREEN.blit(CHEMISTRY, CHEMISTRY_RECT)
    SCREEN.blit(PHYSICS, PHYSICS_RECT)
    SCREEN.blit(ASTRONOMY, ASTRONOMY_RECT)

#simulation area
def simulationArea():
    SCREEN.blit(BG, (0, 0))

    if globals["simulation"] in simulations['subprograms']:
        MENU_TEXT = get_font(90).render(globals["simulation"], True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(globals['width']/2, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        scratch_pad = pygame.Surface((globals['width'], globals['height'] - 200))
        scratch_pad_rect = scratch_pad.get_rect(midbottom=(globals['width']/2, globals['height']))
        scratch_pad.fill((255, 255, 255))
        SCREEN.blit(scratch_pad, scratch_pad_rect)

        simulations['subprograms'][globals["simulation"]]()
    else:
        MENU_TEXT = get_font(100).render("INTERVAL_ERROR", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(globals['width']/2, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

# about/instructions page
def about():
    SCREEN.blit(BG, (0, 0))
    TITLE_TEXT = get_font(90).render("About", True, "#b68f40")
    TITLE_RECT = TITLE_TEXT.get_rect(center=(globals['width']/2, 100))


    BODY_TEXT1 = get_font(30, "philosopher").render("Welcome to \"Reality Simulator\"!", True, "#b68f40")
    BODY_RECT1 = BODY_TEXT1.get_rect(center=(globals['width']/2, 250))
    BODY_TEXT2 = get_font(30, "philosopher").render("This is a beta project whose goal is to allow students to understand complex", True, "#b68f40")
    BODY_RECT2 = BODY_TEXT2.get_rect(center=(globals['width']/2, 300))
    BODY_TEXT3 = get_font(30, "philosopher").render("topics by visual simulations. More simluations of all topics will be coming.", True, "#b68f40")
    BODY_RECT3 = BODY_TEXT3.get_rect(center=(globals['width']/2, 350))
    BODY_TEXT4 = get_font(30, "philosopher").render("Happy learning!", True, "#b68f40")
    BODY_RECT4 = BODY_TEXT4.get_rect(center=(globals['width']/2, 400))

    SCREEN.blit(TITLE_TEXT, TITLE_RECT)
    SCREEN.blit(BODY_TEXT1, BODY_RECT1)
    SCREEN.blit(BODY_TEXT2, BODY_RECT2)
    SCREEN.blit(BODY_TEXT3, BODY_RECT3)
    SCREEN.blit(BODY_TEXT4, BODY_RECT4)

# dictionary of keys
scenes = {
    'menu' : menu,
    'about' : about,
    'simulationGallery' : simulationGallery,
    'simulationArea' : simulationArea
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