from game import Game

def start_menu(game_state,new_game_button,load_game_button,credits_button,quit_button,event):
    if game_state == "show_credits":
        game_state = "start_menu"
        game = None
        return game,game_state
    if new_game_button.rect.collidepoint(event.pos):
        game_state="new_game"
        print("New game click");
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
        print("Credits click");
        game = None
        return game,game_state
    if quit_button.rect.collidepoint(event.pos):
        quit_button.do_action()

    game = None
    return game,game_state

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
            print("klick "+ selected_team)
            game.save_game('c:\temp')
            
    return game_state