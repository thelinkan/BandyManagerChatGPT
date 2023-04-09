import pygame
from button import Button
from inputbox import InputBox
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,WHITE,BLACK,GRAY,FONTSIZE_LARGE,FONTSIZE_MEDIUM,FONTSIZE_SMALL



# Define button actions
def quit_game():
    pygame.quit()
    quit()

# Create font objects
font = pygame.font.Font(None, FONTSIZE_LARGE)
medium_font = pygame.font.Font(None, FONTSIZE_MEDIUM)
small_font = pygame.font.Font(None, FONTSIZE_SMALL)

# Define buttons
button_width = 230
button_height = 50
button_x = (SCREEN_WIDTH - button_width) // 2
button_spacing = 20
new_game_button = Button(button_x, 200, button_width, button_height, "New game", font, BLACK, WHITE, GRAY)
load_game_button = Button(button_x, new_game_button.rect.bottom + button_spacing, button_width, button_height, "Load game", font, BLACK, WHITE, GRAY)
credits_button = Button(button_x, load_game_button.rect.bottom + button_spacing, button_width, button_height, "Credits", font, BLACK, WHITE, GRAY)
quit_button = Button(button_x, credits_button.rect.bottom + button_spacing, button_width, button_height, "Quit game", font, BLACK, WHITE, GRAY, quit_game)
new_game_ok_button = Button(button_x,450, button_width, button_height, "OK", font, BLACK, WHITE, GRAY)
choose_team_button = Button(button_x,690, button_width, button_height, "OK", font, BLACK, WHITE, GRAY)

#Define Input
input_name = InputBox(300, 200, 140, 32)
input_age = InputBox(300, 300, 140, 32)




