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
from gameloop.tactics import gameloop_tactics
from guielements import font,medium_font, small_font, button_width, button_height, button_x, button_spacing
from guielements import new_game_button, load_game_button, credits_button, quit_button, new_game_ok_button, input_name, input_age, quit_game, choose_team_button
from guielements import home_button,senior_squad_button, tactics_button, schedule_button, competition_button ,u19_squad_button,forward_time_button, save_game_button, quit_game_button
from gameloop.mainloop import start_menu, new_game_menu, new_game_menu2

game_state = "start_menu"

# Set the title of the window
pygame.display.set_caption("Bandymanager")

selected_country_index=-1
selected_league_index = -1
selected_team_index=-1
selected_player_index=-1
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
                if home_button.rect.collidepoint(event.pos):
                    game.game_page = "home"
                if(game.game_page == "player_list" or game.game_page == "player_list_u19"):
                    for i, rect in enumerate(rectslist_1):
                        if rect.collidepoint(event.pos):
                            selected_player_index = i
                            break
                if(game.game_page == "competition"):
                    playerlist_offset = (140,110)
                    event_pos = event.pos
                    event_pos_on_list = event_pos[0] - playerlist_offset[0], event_pos[1] - playerlist_offset[1]
                    for i, rect in enumerate(rectslist_1):
                        if rect.collidepoint(event_pos_on_list):
                            game.selected_team_index = i
                            print(game.selected_team_index)
                            break
                    
                if(game.game_page == "tactics"):
                    selected_player_index = gameloop_tactics(game, rectslist_1, rectslist_2, selected_player_index, event.pos)
                if (game.game_page == "schedule"):
                    for i, rect in enumerate(rectslist_1):
                        if rect.collidepoint(event.pos) and i == 0:
                            start_page = start_page - 1
                            break                    
                        if rect.collidepoint(event.pos) and i == 1:
                            start_page = start_page + 1
                            break                    
                if senior_squad_button.rect.collidepoint(event.pos):
                    game.selected_team_index=-1
                    selected_player_index=-1
                    game.inspected_team = None
                    game.game_page = "player_list"
                if tactics_button.rect.collidepoint(event.pos):
                    selected_player_index=-1
                    game.selected_team_index=-1
                    game.inspected_team = None
                    game.game_page = "tactics"
                if schedule_button.rect.collidepoint(event.pos):
                    start_page = 1
                    game.game_page = "schedule"
                if competition_button.rect.collidepoint(event.pos):
                    game.selected_team_index=-1
                    game.inspected_team = None
                    manager_team_name = game.manager.return_team()
                    temp_leagues = game.get_leagues_for_team(manager_team_name)
                    game.inspected_league = temp_leagues[0].name
                    #print(game_page)
                    game.game_page = "competition"
                if u19_squad_button.rect.collidepoint(event.pos):
                    selected_player_index=-1
                    game.inspected_team = None
                    game.game_page = "player_list_u19"
                if forward_time_button.rect.collidepoint(event.pos):
                    isMatchesPlayed, match_viewed, match_to_view = game.tick()
                    if match_viewed:
                        game_state = "view_match"
                        

                if save_game_button.rect.collidepoint(event.pos):
                    game.save_game('c:\temp')
                if quit_game_button.rect.collidepoint(event.pos):
                    quit_game_button.do_action()
                
                break

        if game_state =="new_game":
            name_active = False
            age_active = False
            if input_name.active:
                name_active = True
            if input_age.active:
                age_active = True
            input_name.handle_event(event, name_active, input_age)
            input_age.handle_event(event, age_active, input_name)

    if game_state == "start_menu":
        draw_start_menu()
    if game_state == "show_credits":
        draw_credits()
    if game_state == "new_game":
        draw_newgame_menu()
    if game_state == "new_game_2":
        country_rects,league_rects, team_rects,selected_team=draw_newgame2_menu(game)
    if game_state == "game_mainscreen":
        rectslist_1, rectslist_2, start_page = draw_game_mainscreen(game, selected_player_index,isMatchesPlayed, start_page)
    if game_state == "view_match":
        #draw_view_match(game,match_to_view)
        game_state = "game_mainscreen"
    clock.tick(30)

pygame.quit()
quit()
