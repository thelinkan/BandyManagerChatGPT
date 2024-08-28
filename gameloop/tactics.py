import pygame

#from screens.game import draw_game_mainscreen
from guielements import font,medium_font, small_font, button_width, button_height, button_x, button_spacing
from guielements import new_game_button, load_game_button, credits_button, quit_button, new_game_ok_button, input_name, input_age, quit_game, choose_team_button
from guielements import home_button,senior_squad_button, tactics_button, competition_button ,u19_squad_button,forward_time_button, save_game_button, quit_game_button

def gameloop_tactics(game, player_rects, tactics_rects, event_pos):
    #print("tactics - loop")
    position_list = ["goalkeeper","libero","leftdef","rightdef","lefthalf","righthalf","leftmid","centralmid","rightmid","leftattack","rightattack","sub1","sub2","sub3","sub4","sub5"]

    playerlist_offset = (140,125)
    tactics_list_offset = (740,125)
    event_pos_on_players = event_pos[0] - playerlist_offset[0], event_pos[1] - playerlist_offset[1]
    event_pos_on_tactics = event_pos[0] - tactics_list_offset[0], event_pos[1] - tactics_list_offset[1]
    manager_team_name = game.manager.return_team()
    manager_team = game.teams[manager_team_name]
    for i, rect in enumerate(player_rects):
        if rect.collidepoint(event_pos_on_players):
            game.selected_player_index = i
            game.selected_tactics_index = -1

            break
    for i, rect in enumerate(tactics_rects):
        if rect.collidepoint(event_pos_on_tactics):
            if i == 0:
                game.selected_player_index = -1
                game.selected_tactics_index = 0
            if i == 1:
                game.selected_player_index = -1
                game.selected_tactics_index = 1
            if i == 2:
                game.selected_player_index = -1
                game.selected_tactics_index = 2

    if game.selected_player_index >=0:
        selected_player_pos = -1
        for i, player in enumerate(manager_team.get_players_positions()):
            if(i == game.selected_player_index):
                selected_player_uuid = player[0]
                for j in range (15):
                    if str(selected_player_uuid) == str(manager_team.actual_positions[position_list[j]]["player_uuid"]):
                        selected_player_pos = j
        for i, rect in enumerate(tactics_rects):
            if rect.collidepoint(event_pos_on_tactics):

                if(i>=3 and i<=7):
                    if manager_team.tactics['corner']['cornertaker'] == selected_player_uuid:
                        manager_team.tactics['corner']['cornertaker'] = None
                    game.selected_tactics_index = -1
                    for k in range(len(manager_team.tactics['corner']['targetplayers'])):
                        if manager_team.tactics['corner']['targetplayers'][k] == selected_player_uuid:
                            manager_team.tactics['corner']['targetplayers'][k] = None  # Clear the target player if it's the selected player

                if(i>=8):
                    game.selected_tactics_index = -1
                    for k in range(len(manager_team.tactics['freestroke']['targetplayers'])):
                        if manager_team.tactics['freestroke']['targetplayers'][k] == selected_player_uuid:
                            manager_team.tactics['freestroke']['targetplayers'][k] = None  # Clear the target player if it's the selected player

                if(i==3):
                    manager_team.tactics['corner']['cornertaker'] = selected_player_uuid
                    game.selected_player_index =-1

                # Ensure the list has at least 4 elements before setting values
                while len(manager_team.tactics['corner']['targetplayers']) < 4:
                    manager_team.tactics['corner']['targetplayers'].append(None)  # Append a placeholder value

                while len(manager_team.tactics['freestroke']['targetplayers']) < 3:
                    manager_team.tactics['freestroke']['targetplayers'].append(None)  # Append a placeholder value

                if(i == 4):
                    manager_team.tactics['corner']['targetplayers'][0] = selected_player_uuid
                    game.selected_player_index =-1
                if(i == 5):
                    manager_team.tactics['corner']['targetplayers'][1] = selected_player_uuid
                    game.selected_player_index =-1
                if(i == 6):
                    manager_team.tactics['corner']['targetplayers'][2] = selected_player_uuid
                    game.selected_player_index =-1
                if(i == 7):
                    manager_team.tactics['corner']['targetplayers'][3] = selected_player_uuid
                    game.selected_player_index =-1
                if(i == 8):
                    manager_team.tactics['freestroke']['targetplayers'][0] = selected_player_uuid
                    game.selected_player_index =-1
                if(i == 9):
                    manager_team.tactics['freestroke']['targetplayers'][1] = selected_player_uuid
                    game.selected_player_index =-1
                if(i == 10):
                    manager_team.tactics['freestroke']['targetplayers'][2] = selected_player_uuid
                    game.selected_player_index =-1

                print(f"Tactics {i} - {selected_player_uuid}")
