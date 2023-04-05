import pygame

pygame.init()

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# define some constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT_SIZE = 32

# create the screen and font objects
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont(None, FONT_SIZE)

# create a list of countries
countries = ['Sweden', 'Finland', 'Norway', 'Russia']

# create a variable to store the selected country
selected_country = None

# create a function to draw the country list
def draw_country_list():
    y = 50
    for country in countries:
        text = font.render(country, True, BLACK)
        rect = text.get_rect(center=(SCREEN_WIDTH/2, y))
        screen.blit(text, rect)
        y += FONT_SIZE + 10

# create a function to check if the mouse is over a country
def mouse_over_country(mouse_pos):
    y = 50
    for country in countries:
        text = font.render(country, True, BLACK)
        rect = text.get_rect(center=(SCREEN_WIDTH/2, y))
        if rect.collidepoint(mouse_pos):
            return country
        y += FONT_SIZE + 10
    return None

# create a function to handle events
def handle_events():
    global selected_country
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            selected_country = mouse_over_country(mouse_pos)
            if selected_country is not None:
                print(f'Selected country: {selected_country}')

# create a function to draw the screen
def draw_screen():
    screen.fill(WHITE)
    draw_country_list()
    pygame.display.update()

# main game loop
while True:
    handle_events()
    draw_screen()
