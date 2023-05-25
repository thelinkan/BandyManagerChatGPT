import pygame

from screens.game import draw_game_mainscreen
from guielements import font,medium_font, small_font, button_width, button_height, button_x, button_spacing
from guielements import new_game_button, load_game_button, credits_button, quit_button, new_game_ok_button, input_name, input_age, quit_game, choose_team_button
from guielements import home_button,senior_squad_button, tactics_button, competition_button ,u19_squad_button,forward_time_button, save_game_button, quit_game_button

def gameloop_tactics(game, player_rects, jersey_rects, event_pos):
    #print("tactics - loop")
    position_list = ["goalkeeper","libero","leftdef","rightdef","lefthalf","righthalf","leftmid","centralmid","rightmid","leftattack","rightattack","sub1","sub2","sub3","sub4","sub5"]

    playerlist_offset = (140,125)
    field_offset = (740,125)
    event_pos_on_list = event_pos[0] - playerlist_offset[0], event_pos[1] - playerlist_offset[1]
    event_pos_on_field = event_pos[0] - field_offset[0], event_pos[1] - field_offset[1]
    manager_team_name = game.manager.return_team()
    manager_team = game.teams[manager_team_name]
    #print("Tactics")
    #print(event_pos)
    for i, rect in enumerate(player_rects):
        #print("player_rects")
        if rect.collidepoint(event_pos_on_list):
            game.selected_player_index = i
            #print(selected_player_index)
            break

    if game.selected_player_index >=0:
        selected_player_pos = -1
        for i, player in enumerate(manager_team.get_players()):
            if(i == game.selected_player_index):
                selected_player_uuid = player[0]
                #print(selected_player_uuid)
                for j in range (15):
                    if str(selected_player_uuid) == str(manager_team.actual_positions[position_list[j]]["player_uuid"]):
                        selected_player_pos = j
        #print(selected_player_pos)
        for i, rect in enumerate(jersey_rects):
            if rect.collidepoint(event_pos_on_field):
                position_uuid = manager_team.actual_positions[position_list[i]]["player_uuid"]
                if str(position_uuid) == str(selected_player_uuid):
                    game.selected_player_index = -1
                else:
                    manager_team.actual_positions[position_list[selected_player_pos]]["player_uuid"]=position_uuid
                    manager_team.actual_positions[position_list[i]]["player_uuid"]=selected_player_uuid

