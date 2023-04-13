import pygame
from button import Button
from inputbox import InputBox
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,WHITE,BLACK,GRAY,FONTSIZE_LARGE,FONTSIZE_MEDIUM,FONTSIZE_SMALL, FONTSIZE_VERY_SMALL



# Define button actions
def quit_game():
    pygame.quit()
    quit()

# Create font objects
font = pygame.font.Font(None, FONTSIZE_LARGE)
medium_font = pygame.font.Font(None, FONTSIZE_MEDIUM)
small_font = pygame.font.Font(None, FONTSIZE_SMALL)
very_small_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)

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

#Define maingame buttons
button_width = 110
button_height = 23
button_x = 0
button_spacing = 0
home_button = Button(button_x,0,button_width,button_height, "Home", very_small_font,WHITE , BLACK, GRAY)
senior_squad_button = Button(button_x,home_button.rect.bottom + button_spacing,button_width,button_height, "Squad", very_small_font, WHITE, BLACK, GRAY)
u19_squad_button = Button(button_x,senior_squad_button.rect.bottom + button_spacing,button_width,button_height, "U19 squad", very_small_font, WHITE, BLACK, GRAY)
forward_time_button = Button(button_x,u19_squad_button.rect.bottom + button_spacing,button_width,button_height, "Forward Time", very_small_font, WHITE, BLACK, GRAY)
save_game_button = Button(button_x,forward_time_button.rect.bottom + button_spacing,button_width,button_height, "Save game", very_small_font, WHITE, BLACK, GRAY)
quit_game_button = Button(button_x, save_game_button.rect.bottom + button_spacing, button_width, button_height, "Quit game", very_small_font, WHITE, BLACK, GRAY, quit_game)
#Define Input
input_name = InputBox(300, 200, 140, 32)
input_age = InputBox(300, 300, 140, 32)




