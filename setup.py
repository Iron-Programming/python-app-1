from library import *
from button import *

def to_simulations():
    globals['scene'] = 'simulationGallery'

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

buttons = {
    'menu' : [],
    'about' : [],
    'simulationGallery' : [],
    'simulationPage' : []
}

# add buttons
buttons['menu'].append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (640, 250), 
    text_input = "Simulations",
    font = get_font(55),
    base_color = "#d7fcd4",
    click_effect = lambda : addInterval(to_simulations, 10)
))
buttons['menu'].append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (640, 400), 
    text_input = "About",
    font = get_font(55),
    base_color = "#d7fcd4",
    click_effect = lambda : addInterval(to_about, 10)
))
buttons['menu'].append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (640, 550), 
    text_input = "Quit",
    font = get_font(55),
    base_color = "#d7fcd4",
    click_effect = lambda : end_game()
))
