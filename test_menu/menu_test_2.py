import pygame

# Initialize Pygame
pygame.init()

# Set up the Pygame window
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)

# Define the options for the dropdown menu
options = ['Option 1', 'Option 2', 'Option 3']

# Define the position and size of the dropdown menu
menu_x = 100
menu_y = 100
menu_width = 200
menu_height = 40

# Define the position and size of the options within the dropdown menu
option_x = menu_x
option_y = menu_y + menu_height
option_width = menu_width
option_height = 30

# Set up a boolean variable to keep track of whether the dropdown menu is open or closed
menu_open = False

# Set up a variable to keep track of the currently selected option
selected_option = None

# Main game loop
running = True
while running:

    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked within the dropdown menu
            if menu_x <= event.pos[0] <= menu_x + menu_width and menu_y <= event.pos[1] <= menu_y + menu_height:
                menu_open = not menu_open
            else:
                menu_open = False

            # Check if the user clicked on one of the options within the dropdown menu
            if menu_open:
                for i, option in enumerate(options):
                    if option_x <= event.pos[0] <= option_x + option_width and option_y + i*option_height <= event.pos[1] <= option_y + (i+1)*option_height:
                        selected_option = option
                        menu_open = False

    # Draw the screen
    screen.fill((255, 255, 255))
    
    # Draw the dropdown menu
    pygame.draw.rect(screen, (0, 0, 0), (menu_x, menu_y, menu_width, menu_height))
    pygame.draw.rect(screen, (255, 255, 255), (menu_x+1, menu_y+1, menu_width-2, menu_height-2))
    pygame.draw.rect(screen, (0, 0, 0), (menu_x, option_y-1, menu_width, len(options)*option_height+2))
    for i, option in enumerate(options):
        pygame.draw.rect(screen, (255, 255, 255), (option_x, option_y+i*option_height, option_width, option_height))
        pygame.draw.rect(screen, (0, 0, 0), (option_x, option_y+i*option_height, option_width, option_height), 1)
        text = pygame.font.SysFont(None, 20).render(option, True, (0, 0, 0))
        text_rect = text.get_rect(center=(menu_x + menu_width/2, option_y + (i+0.5)*option_height))
        screen.blit(text, text_rect)

    # Draw the currently selected option
    if selected_option is not None:
        selected_text = pygame.font.SysFont(None, 30).render(selected_option, True, (0, 0, 0))
        selected_rect = selected_text.get_rect(center=(menu_x + menu_width/2, menu_y + menu_height/2))
        screen.blit(selected_text, selected_rect)

    # Update the Pygame display
    pygame.display.update()

# Quit Pygame
