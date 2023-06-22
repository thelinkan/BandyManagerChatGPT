import pygame
import json
import pickle
#import classes for GUI
from inputbox import InputBox
from button import Button
pygame.init()
from game import Game

from constants import SCREEN_WIDTH,SCREEN_HEIGHT,WHITE,BLACK,GRAY
from screens.start import screen,draw_start_menu, draw_credits, draw_newgame_menu, draw_newgame2_menu
from screens.game import draw_game_mainscreen
from screens.screensMatch import draw_view_match
from guielements import font,medium_font, small_font, button_width, button_height, button_x, button_spacing
from guielements import new_game_button, load_game_button, credits_button, quit_button, new_game_ok_button, input_name, input_age, quit_game, choose_team_button
from guielements import home_button,senior_squad_button, tactics_button, schedule_button, competition_button ,u19_squad_button,forward_time_button, save_game_button, quit_game_button
from gameloop.mainloop import start_menu, new_game_menu, new_game_menu2, mainscreen_loop, new_game_input

game_state = "start_menu"

# Set the title of the window
pygame.display.set_caption("Bandymanager")

selected_country_index=-1
selected_league_index = -1
selected_team_index=-1
selected_player_index=-1
selected_news_index=-1
isMatchesPlayed = False
start_page=-1

# Define game loop
running = True
while running:
    clock = pygame.time.Clock()
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  
            if event.button == 1 and (game_state == "start_menu" or game_state == "show_credits"):
                game,game_state = start_menu(game_state,new_game_button,load_game_button,credits_button,quit_button,event)
            elif event.button == 1 and game_state == "new_game":
                game_state = new_game_menu(game, game_state, input_name, input_age, new_game_ok_button, event)
            elif event.button == 1 and game_state == "new_game_2":
                game_state = new_game_menu2(game, game_state,country_rects,league_rects,team_rects,selected_team,choose_team_button, event)
            elif event.button == 1 and game_state == "game_mainscreen":
                game_state = mainscreen_loop(game, game_state, rectslist_1, rectslist_2, event)
        if game_state =="new_game":
            new_game_input(event)

    if game_state == "start_menu":
        draw_start_menu()
    if game_state == "show_credits":
        draw_credits()
    if game_state == "new_game":
        draw_newgame_menu()
    if game_state == "new_game_2":
        country_rects,league_rects, team_rects,selected_team=draw_newgame2_menu(game)
    if game_state == "game_mainscreen":
        rectslist_1, rectslist_2 = draw_game_mainscreen(game)
    if game_state == "view_match":
        #draw_view_match(game,match_to_view)
        game_state = "game_mainscreen"
    clock.tick(30)

pygame.quit()
quit()
