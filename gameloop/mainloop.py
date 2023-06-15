import pygame

from game import Game

from guielements import input_name, input_age
from guielements import home_button,senior_squad_button, tactics_button, schedule_button, competition_button ,u19_squad_button,forward_time_button, save_game_button, quit_game_button
from gameloop.tactics import gameloop_tactics
from screens.screensleague import choose_league
pygame.init()

def mainscreen_loop(game, game_state, rectslist_1, rectslist_2, event):
    if home_button.rect.collidepoint(event.pos):
        game.game_page = "home"
        game.start_page = 1
    if(game.game_page == "player_list" or game.game_page == "player_list_u19"):
        event_pos = event.pos
        playerlist_offset = (140,125)
        event_pos_on_list = event_pos[0] - playerlist_offset[0], event_pos[1] - playerlist_offset[1]
        for i, rect in enumerate(rectslist_1):
            if rect.collidepoint(event_pos_on_list):
                game.selected_player_index = i
                break
    if(game.game_page == "competition" and game.game_sub_page != "chooseleague"):
        event_pos = event.pos
        playerlist_offset = (140,110)
        event_pos_on_list = event_pos[0] - playerlist_offset[0], event_pos[1] - playerlist_offset[1]
        rect_2_offset = (890,150)
        event_pos_on_list2 = event_pos[0] - rect_2_offset[0], event_pos[1] - rect_2_offset[1]
        #print(rectslist_1)
        for i, rect in enumerate(rectslist_1):
            #print(rect)
            if rect.collidepoint(event_pos_on_list):
                game.selected_team_index = i
                selected_league = game.inspected_league
                league = game.return_league_by_name(selected_league)
                sorted_table = sorted(league.table.items(), key=lambda x: (-x[1]['points'], -x[1]['goals_for'] + x[1]['goals_against'], -x[1]['goals_for']))
                for j, team in enumerate(sorted_table):
                    if j == game.selected_team_index:
                        game.inspected_team = team
                        pass                
        for i, rect in enumerate(rectslist_2):
            if rect.collidepoint(event_pos_on_list2) and i==0:
                game.game_sub_page = "chooseleague"
                game.selected_league_index = -1
                print("choose league")                    
               
        
    if(game.game_page == "tactics"):
        gameloop_tactics(game, rectslist_1, rectslist_2, event.pos)
    if (game.game_page == "home"):
        home_loop(game, rectslist_1, event)
    if ((game.game_page == "schedule" or game.game_page == "competition") and game.game_sub_page == "chooseleague"):
        choice_offset = (250,75)
        border = (2,2)
        country_offset = (10,10)
        league_offset = (360,10)

        mouse_pos = pygame.mouse.get_pos()
        mouse_pos_on_country = mouse_pos[0] - choice_offset[0] - border[0] - country_offset[0], mouse_pos[1] - choice_offset[1] - border[1] - country_offset[1]        
        mouse_pos_on_league = mouse_pos[0] - choice_offset[0] - border[0] - league_offset[0], mouse_pos[1] - choice_offset[1] - border[1] - league_offset[1]        
        for i, rect in enumerate(rectslist_1):
            if rect.collidepoint(mouse_pos_on_country):
                game.selected_country_index = i
                game.selected_league_index = -1
                if i==0:
                    game.game_sub_page = ""
                    game.selected_country_index = -1
                print(f"clicking country {i} - {game.game_sub_page}")
        for i, rect in enumerate(rectslist_2):
            if rect.collidepoint(mouse_pos_on_league):
                if i==0 and game.selected_league_index>0:
                    countries = game.return_countries_with_leagues()
                    selected_country = countries[game.selected_country_index-1].return_name()
                    leagues = game.return_leagues_in_country(selected_country)
                    game.inspected_league = leagues[game.selected_league_index-1].name                    
                    game.selected_country_index = -1
                    game.selected_league_index = -1
                    game.game_sub_page = ""
                    print(f"{game.inspected_league}")
                    break
                game.selected_league_index = i
                print(f"clicking league {i}")
        #game.game_sub_page = ""
    if (game.game_page == "schedule" and game.game_sub_page != "chooseleague"):
        rect_2_offset = (890,150)
        event_pos = event.pos
        event_pos_on_list = event_pos[0] - rect_2_offset[0], event_pos[1] - rect_2_offset[1]
        for i, rect in enumerate(rectslist_1):
            print(f"{game.inspected_league}")
            if rect.collidepoint(event.pos) and i == 0:
                game.start_page = game.start_page - 1
                break                    
            if rect.collidepoint(event.pos) and i == 1:
                game.start_page = game.start_page + 1
                break
        for i, rect in enumerate(rectslist_2):
            if rect.collidepoint(event_pos_on_list) and i==0:
                game.game_sub_page = "chooseleague"
                game.selected_league_index = -1
                print("choose league")                    
    if senior_squad_button.rect.collidepoint(event.pos):
        game.selected_team_index=-1
        game.selected_player_index=-1
        game.inspected_team = None
        game.game_page = "player_list"
    if tactics_button.rect.collidepoint(event.pos):
        game.selected_player_index=-1
        game.selected_team_index=-1
        game.inspected_team = None
        game.game_page = "tactics"
    if schedule_button.rect.collidepoint(event.pos):
        game.start_page = 1
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
        game.selected_player_index=-1
        game.inspected_team = None
        game.game_page = "player_list_u19"
    if forward_time_button.rect.collidepoint(event.pos):
        match_viewed, match_to_view = game.tick()
        if match_viewed:
            game_state = "view_match"
            

    if save_game_button.rect.collidepoint(event.pos):
        game.save_game('c:\temp')
    if quit_game_button.rect.collidepoint(event.pos):
        quit_game_button.do_action()

    return game_state

def start_menu(game_state,new_game_button,load_game_button,credits_button,quit_button,event):
    if game_state == "show_credits":
        game_state = "start_menu"
        game = None
        return game,game_state
    if new_game_button.rect.collidepoint(event.pos):
        game_state="new_game"
        #print("New game click");
        game = Game(2023,8,1)
        return game,game_state
    if load_game_button.rect.collidepoint(event.pos):
        game_state="load_game"
        game = Game(0,0,0)
        game.load_game('')
        #print("Load game click");
        game_state = "game_mainscreen"
        game.game_page = "home"
        return game,game_state
    if credits_button.rect.collidepoint(event.pos):
        game_state="show_credits"
        #print("Credits click");
        game = None
        return game,game_state
    if quit_button.rect.collidepoint(event.pos):
        quit_button.do_action()

    game = None
    return game,game_state

def home_loop(game,rectslist_1,event):
        list_offset = (470,110)
        mouse_pos = event.pos
        mouse_pos_on_list = mouse_pos[0] - list_offset[0], mouse_pos[1] - list_offset[1]

        for i, rect in enumerate(rectslist_1):
            if rect.collidepoint(mouse_pos_on_list) and i == 0:
                game.start_page = game.start_page - 1
                break                    
            if rect.collidepoint(mouse_pos_on_list) and i == 1:
                game.start_page = game.start_page + 1
                break


def new_game_menu(game, game_state, input_name, input_age, new_game_ok_button, event):
    if new_game_ok_button.rect.collidepoint(event.pos):
        manager_name=input_name.return_text()
        if(len(input_age.return_text())>0):
            manager_age=int(input_age.return_text())
        else:
            manager_age=0
        if len(manager_name)>0 and manager_age>0 and manager_age < 120:
            game.new_game(manager_name, manager_age)
            game_state="new_game_2"

    return game_state

def new_game_menu2(game, game_state,country_rects,league_rects,team_rects, selected_team,choose_team_button, event):
    for i, rect in enumerate(country_rects):
        if rect.collidepoint(event.pos):
            game.selected_country_index = i
            game.selected_league_index = -1
            game.selected_team_index = -1
            break
    for i, rect in enumerate(league_rects):
        if rect.collidepoint(event.pos):
            game.selected_team_index = -1
            game.selected_league_index = i
            break
    for i, rect in enumerate(team_rects):
        if rect.collidepoint(event.pos):
            game.selected_team_index = i
            break
    if game.selected_team_index>=0:
        if choose_team_button.rect.collidepoint(event.pos):
            game.set_manager_team(selected_team)
            game_state = "game_mainscreen"
            game.game_page = "home"
            #print("klick "+ selected_team)
            game.save_game('c:\temp')
            
    return game_state

def new_game_input(event):
    name_active = False
    age_active = False
    if input_name.active:
        name_active = True
    if input_age.active:
        age_active = True
    input_name.handle_event(event, name_active, input_age)
    input_age.handle_event(event, age_active, input_name)

