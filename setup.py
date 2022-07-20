from library import *
from button import *

def to_simulations():
    globals['scene'] = 'simulationGallery'

def to_simulation_area():
    globals['scene'] = 'simulationArea'

def to_about():
    globals['scene'] = 'about'

def to_menu():
    globals['scene'] = 'menu'

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
    'simulationArea' : []
}

#menu buttons
buttons['menu'].append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (640, 250), 
    size = (400, 100),
    text_input = "Simulations",
    font = get_font(55),
    color = "#d7fcd4",
    click_effect = lambda : addInterval(to_simulations, 10)
))
buttons['menu'].append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (640, 400), 
    size = (400, 100),
    text_input = "About",
    font = get_font(55),
    color = "#d7fcd4",
    click_effect = lambda : addInterval(to_about, 10)
))
buttons['menu'].append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (640, 550), 
    size = (400, 100),
    text_input = "Quit",
    font = get_font(55),
    color = "#d7fcd4",
    click_effect = lambda : end_game()
))

#about
buttons['about'].append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (globals['width'] - 75, 50), 
    size = (100, 50),
    text_input = "Menu",
    font = get_font(20),
    color = "#d7fcd4",
    click_effect = lambda : addInterval(to_menu, 10)
))

# simulation gallery
simulations = {
    'math' : [
        "???",
        "???",
        "???",
        "???",
        "???",
        "???"
    ],
    'chemistry' : [
        "???",
        "???",
        "???",
        "???",
        "???",
        "???"
    ],
    'physics' : [
        "???",
        "???",
        "???",
        "???",
        "???",
        "???"
    ],
    'astronomy' : [
        "???",
        "???",
        "???",
        "???",
        "???",
        "???"
    ]
}

buttons['simulationGallery'].append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (globals['width'] - 75, 50), 
    size = (100, 50),
    text_input = "Menu",
    font = get_font(20),
    color = "#d7fcd4",
    click_effect = lambda : addInterval(to_menu, 10)
))

j = 0
for category in simulations:
    i = 0
    for simulation in simulations[category]:
        buttons['simulationGallery'].append(Button(
            image = pygame.image.load("assets/button.jpg"),
            hover_image = pygame.image.load("assets/buttonhover.jpg"),
            pos = (190 + j*300, 400 + i*50), 
            size = (200, 50),
            text_input = simulation,
            font = get_font(25),
            color = "#d7fcd4",
            click_effect = lambda : addInterval(to_simulation_area, 10)
        ))
        i += 1
    j += 1