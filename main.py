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
from guielements import font,medium_font, small_font, button_width, button_height, button_x, button_spacing
from guielements import new_game_button, load_game_button, credits_button, quit_button, new_game_ok_button, input_name, input_age, quit_game, choose_team_button
from guielements import home_button,senior_squad_button, competition_button ,u19_squad_button,forward_time_button, save_game_button, quit_game_button

game_state = "start_menu"

# Set the title of the window
pygame.display.set_caption("Bandymanager")

selected_country_index=-1
selected_team_index=-1
selected_player_index=-1

# Define game loop
running = True
while running:
    clock = pygame.time.Clock()
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "show_credits":
            	game_state = "start_menu"
            elif event.button == 1 and game_state == "start_menu":
                if new_game_button.rect.collidepoint(event.pos):
                    game_state="new_game"
                    print("New game click");
                    game = Game(2023,8,1)
                if load_game_button.rect.collidepoint(event.pos):
                    game_state="load_game"
                    game = Game(0,0,0)
                    game.load_game('')
                    #print("Load game click");
                    game_state = "game_mainscreen"
                    game_page = "home"
                if credits_button.rect.collidepoint(event.pos):
                    game_state="show_credits"
                    print("Credits click");
                if quit_button.rect.collidepoint(event.pos):
                    quit_button.do_action()
            elif event.button == 1 and game_state == "new_game":
                if new_game_ok_button.rect.collidepoint(event.pos):
                    manager_name=input_name.return_text()
                    manager_age=int(input_age.return_text())
                    game.new_game(manager_name, manager_age)
                    #print(Sweden.male_first_names)
                    #print(Sweden.female_first_names)
                    #print(sweden.family_names)
                    #game.save_game('c:\temp')
                    game_state="new_game_2"
            elif event.button == 1 and game_state == "new_game_2":
                for i, rect in enumerate(country_rects):
                    if rect.collidepoint(event.pos):
                        selected_country_index = i
                        selected_team_index = -1
                        break
                for i, rect in enumerate(team_rects):
                    if rect.collidepoint(event.pos):
                        selected_team_index = i
                        break
                if selected_team_index>=0:
                    if choose_team_button.rect.collidepoint(event.pos):
                        game.set_manager_team(selected_team)
                        game_state = "game_mainscreen"
                        game_page = "home"
                        print("klick "+ selected_team)
                        game.save_game('c:\temp')
                        break
            elif event.button == 1 and game_state == "game_mainscreen":
                if home_button.rect.collidepoint(event.pos):
                    game_page = "home"
                if(game_page == "player_list" or game_page == "player_list_u19"):
                    for i, rect in enumerate(player_rects):
                        if rect.collidepoint(event.pos):
                            selected_player_index = i
                            break
                if senior_squad_button.rect.collidepoint(event.pos):
                    selected_player_index=-1
                    game_page = "player_list"
                if competition_button.rect.collidepoint(event.pos):
                    print(game_page)
                    game_page = "competition"
                if u19_squad_button.rect.collidepoint(event.pos):
                    selected_player_index=-1
                    game_page = "player_list_u19"
                if forward_time_button.rect.collidepoint(event.pos):
                    game.tick()
                    matches_today = game.match_manager.get_matches_by_date(game.year, game.month, game.day)
                    if len(matches_today) > 0:
                        for match in matches_today:
                            match.play()
                            print (f"{match.home_team.name} - {match.away_team.name}: {match.home_goals} - {match.away_goals}")
                        leagues = game.get_leagues()
                        for league in leagues:
                            league.calculate_table()
                            league.print_table()
                if save_game_button.rect.collidepoint(event.pos):
                    game.save_game('c:\temp')
                if quit_game_button.rect.collidepoint(event.pos):
                    quit_game_button.do_action()
                
                break

        if game_state =="new_game":
            input_name.handle_event(event)
            input_age.handle_event(event)

    if game_state == "start_menu":
        draw_start_menu()
    if game_state == "show_credits":
        draw_credits()
    if game_state == "new_game":
        draw_newgame_menu()
    if game_state == "new_game_2":
        country_rects,team_rects,selected_team=draw_newgame2_menu(game,selected_country_index,selected_team_index)
    if game_state == "game_mainscreen":
        player_rects = draw_game_mainscreen(game,game_page, selected_player_index)
        #print(player_rects)
    clock.tick(30)

pygame.quit()
quit()
