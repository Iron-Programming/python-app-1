from library import *
from button import *

def to_simulations():
    globals['scene'] = 'play'

def to_about():
    globals['scene'] = 'about'

def end_game():
    pygame.quit()
    sys.exit()

# initalize pygame canvas
pygame.init()

# set screen size
SCREEN = pygame.display.set_mode((globals['width'], globals['height']))

# set app name
pygame.display.set_caption("Final Project")

# load background image
BG = pygame.image.load("assets/background.jpg")

# add buttons
buttons.append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (640, 250), 
    text_input = "Simulations",
    font = get_font(55),
    base_color = "#d7fcd4",
    click_effect = lambda : to_simulations()
))
buttons.append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (640, 400), 
    text_input = "About",
    font = get_font(55),
    base_color = "#d7fcd4",
    click_effect = lambda : to_about()
))
buttons.append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (640, 550), 
    text_input = "Quit",
    font = get_font(55),
    base_color = "#d7fcd4",
    click_effect = lambda : end_game()
))
