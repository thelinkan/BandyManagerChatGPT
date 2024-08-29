import pygame

from constants import SCREEN_WIDTH,SCREEN_HEIGHT,WHITE,BLACK,GRAY,FONTSIZE_LARGE,FONTSIZE_MEDIUM,FONTSIZE_SMALL,FONTSIZE_VERY_SMALL
from constants import TABLE_HEADER_COLOR, TABLE_ROW_ODD_COLOR, TABLE_ROW_EVEN_COLOR
from guielements import font, medium_font, small_font,very_small_font ,very_small_bold_font , button_width, button_height, button_x, button_spacing
from graphicscode.jersey import draw_jersey
from graphicscode.arrows import draw_arrow_left, draw_arrow_right, draw_arrow_up, draw_arrow_down

from game import Game
from league import League
from team import Team

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def draw_tactics(game,team):
    tactics_rects = []
    playerlist_offset = (140,125)
    playerlist_surface, player_rects, hover_player_uuid, selected_player_uuid = draw_tactics_playerlist(game,team, playerlist_offset, "tactics")
    screen.blit(playerlist_surface,playerlist_offset)
    
    player_offset = (490,125)
    tactics_list_offset = (740,125)

    if(selected_player_uuid is not None):
        player_surface = draw_player(game,selected_player_uuid)
        screen.blit(player_surface,player_offset)

    tactics_list_surface, tactics_rect = draw_tactics_list(game, team, tactics_list_offset)
    screen.blit(tactics_list_surface,tactics_list_offset)
    
    if(game.selected_tactics_index==0):
        longpasses_surface, tactics_rects = draw_tactics_choose_longpasses(game, player_offset, team.tactics['passing']['longballs'])
        screen.blit(longpasses_surface,player_offset)

    if(game.selected_tactics_index==1):
        defense_surface, tactics_rects = draw_tactics_choose_defense(game, player_offset, team.tactics['defence']['type'])
        screen.blit(defense_surface,player_offset)

    '''
    pitch_surface, jersey_rects = draw_tactics_pitch(game,team,hover_player_uuid, selected_player_uuid, pitch_offset)
    screen.blit(pitch_surface,pitch_offset)

    , jersey_rects
    '''

    return player_rects, tactics_rect, tactics_rects

def draw_tactics_list(game, team, tactics_list_offset):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_on_list = mouse_pos[0] - tactics_list_offset[0], mouse_pos[1] - tactics_list_offset[1]

    tactics_list_surface = pygame.Surface((600,600), pygame.SRCALPHA)
    header_rect = pygame.Rect(0, 0, 300, 30)

    pygame.draw.rect(tactics_list_surface, TABLE_HEADER_COLOR, header_rect)
    header_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    text = header_font.render("Tactic", True, BLACK)
    text_rect = text.get_rect(left=header_rect.left + 10, centery=header_rect.centery)
    tactics_list_surface.blit(text, text_rect)
    text = header_font.render("Setting", True, BLACK)
    text_rect = text.get_rect(right=header_rect.right - 10, centery=header_rect.centery)
    tactics_list_surface.blit(text, text_rect)

    tactics_rects = []
    row_height = 30
    tactics_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    row_height = FONTSIZE_VERY_SMALL+8

    i=0
    row_color = TABLE_ROW_EVEN_COLOR
    row_rect = pygame.Rect(0, 30 + i * row_height, 300, row_height)
    if mouse_pos and row_rect.collidepoint(mouse_pos_on_list):
        row_color = (255,200,200)
    if(game.selected_tactics_index == i):
        row_color = (200,0,0)
        
    pygame.draw.rect(tactics_list_surface, row_color, row_rect)
    text = tactics_font.render("Long Passes", True, BLACK)
    text_rect = text.get_rect(left=row_rect.left + 10, centery=row_rect.centery)
    tactics_list_surface.blit(text, text_rect)
    text = tactics_font.render(str(team.tactics['passing']['longballs'])+"0 %", True, BLACK)
    text_rect = text.get_rect(right=row_rect.right - 10, centery=row_rect.centery)
    tactics_list_surface.blit(text, text_rect)
    tactics_rects.append(row_rect)

    i=1
    row_color = TABLE_ROW_ODD_COLOR
    row_rect = pygame.Rect(0, 30 + i * row_height, 300, row_height)
    if mouse_pos and row_rect.collidepoint(mouse_pos_on_list):
        row_color = (255,200,200)
    if(game.selected_tactics_index == i):
        row_color = (200,0,0)
    pygame.draw.rect(tactics_list_surface, row_color, row_rect)
    text = tactics_font.render("Defensive tactics", True, BLACK)
    text_rect = text.get_rect(left=row_rect.left + 10, centery=row_rect.centery)
    tactics_list_surface.blit(text, text_rect)
    match team.tactics['defence']['type']:
        case 0:
            text = tactics_font.render("Neutral", True, BLACK)
        case 1:
            text = tactics_font.render("High pressure", True, BLACK)
        case 2:
            text = tactics_font.render("Park the buss", True, BLACK)
        case 3:
            text = tactics_font.render("Garbage bag", True, BLACK)
        case _:
            text = tactics_font.render("Error", True, BLACK)
    text_rect = text.get_rect(right=row_rect.right - 10, centery=row_rect.centery)
    tactics_list_surface.blit(text, text_rect)
    tactics_rects.append(row_rect)

    i=2
    row_color = TABLE_ROW_EVEN_COLOR
    row_rect = pygame.Rect(0, 30 + i * row_height, 300, row_height)
    if mouse_pos and row_rect.collidepoint(mouse_pos_on_list):
        row_color = (255,200,200)
    if(game.selected_tactics_index == i):
        row_color = (200,0,0)
    pygame.draw.rect(tactics_list_surface, row_color, row_rect)
    text = tactics_font.render("Offensive tactics", True, BLACK)
    text_rect = text.get_rect(left=row_rect.left + 10, centery=row_rect.centery)
    tactics_list_surface.blit(text, text_rect)
    match team.tactics['offence']['type']:
        case 0:
            text = tactics_font.render("Neutral", True, BLACK)
        case 1:
            text = tactics_font.render("Value and slow advance", True, BLACK)
        case 2:
            text = tactics_font.render("Offensive", True, BLACK)
        case 3:
            text = tactics_font.render("Counter-attack", True, BLACK)
        case _:
            text = tactics_font.render("Error", True, BLACK)
    text_rect = text.get_rect(right=row_rect.right - 10, centery=row_rect.centery)
    tactics_list_surface.blit(text, text_rect)
    tactics_rects.append(row_rect)

    # Adding Cornertaker Row
    i = 3
    row_color = TABLE_ROW_ODD_COLOR
    row_rect = pygame.Rect(0, 30 + i * row_height, 300, row_height)
    if mouse_pos and row_rect.collidepoint(mouse_pos_on_list):
        row_color = (255, 200, 200)
    pygame.draw.rect(tactics_list_surface, row_color, row_rect)
    text = tactics_font.render("Corner Taker", True, BLACK)
    text_rect = text.get_rect(left=row_rect.left + 10, centery=row_rect.centery)
    tactics_list_surface.blit(text, text_rect)

    # Checking for the player's name or "No player selected"
    cornertaker_uuid = team.tactics['corner']['cornertaker']
    player_name = "No player selected"
    # Look up player by UUID in the actual_positions dict
    for position, details in team.actual_positions.items():
        if details['player_uuid'] == cornertaker_uuid:
            player = team.players[details['player_uuid']]
            player_name = f"{player.first_name} {player.last_name}"
            #print("yes")
            break  # Stop the loop once a match is found
    text = tactics_font.render(player_name, True, BLACK)
    text_rect = text.get_rect(right=row_rect.right - 10, centery=row_rect.centery)
    tactics_list_surface.blit(text, text_rect)
    tactics_rects.append(row_rect)
    targetplayers_uuid = team.tactics['corner']['targetplayers']
    num_targetplayers = len(targetplayers_uuid)
    for j in range(4):
        i=i+1
        row_rect = pygame.Rect(0, 30 + i * row_height, 300, row_height)
        row_color = TABLE_ROW_ODD_COLOR
        if mouse_pos and row_rect.collidepoint(mouse_pos_on_list):
            row_color = (255, 200, 200)
        pygame.draw.rect(tactics_list_surface, row_color, row_rect)
        if(j==0):
            text = tactics_font.render("Target players", True, BLACK)
        else:
            text = tactics_font.render("", True, BLACK)
        text_rect = text.get_rect(left=row_rect.left + 10, centery=row_rect.centery)
        tactics_list_surface.blit(text, text_rect)

        player_name = "No player selected"
        if num_targetplayers>j:
        # Look up player by UUID in the actual_positions dict
            for position, details in team.actual_positions.items():
                if details['player_uuid'] == targetplayers_uuid[j]:
                    player = team.players[details['player_uuid']]
                    player_name = f"{player.first_name} {player.last_name}"
                
        text = tactics_font.render(player_name, True, BLACK)
        text_rect = text.get_rect(right=row_rect.right - 10, centery=row_rect.centery)
        tactics_list_surface.blit(text, text_rect)
        tactics_rects.append(row_rect)
    targetplayers_uuid = team.tactics['freestroke']['targetplayers']
    num_targetplayers = len(targetplayers_uuid)
    for j in range(3):
        i=i+1
        row_rect = pygame.Rect(0, 30 + i * row_height, 300, row_height)
        row_color = TABLE_ROW_EVEN_COLOR
        if mouse_pos and row_rect.collidepoint(mouse_pos_on_list):
            row_color = (255, 200, 200)
        pygame.draw.rect(tactics_list_surface, row_color, row_rect)
        if(j==0):
            text = tactics_font.render("Freestroke players", True, BLACK)
        else:
            text = tactics_font.render("", True, BLACK)
        text_rect = text.get_rect(left=row_rect.left + 10, centery=row_rect.centery)
        tactics_list_surface.blit(text, text_rect)

        player_name = "No player selected"
        if num_targetplayers>j:
        # Look up player by UUID in the actual_positions dict
            for position, details in team.actual_positions.items():
                if details['player_uuid'] == targetplayers_uuid[j]:
                    player = team.players[details['player_uuid']]
                    player_name = f"{player.first_name} {player.last_name}"
                
        text = tactics_font.render(player_name, True, BLACK)
        text_rect = text.get_rect(right=row_rect.right - 10, centery=row_rect.centery)
        tactics_list_surface.blit(text, text_rect)
        tactics_rects.append(row_rect)


    return tactics_list_surface, tactics_rects

def draw_lineup(game: Game,team: Team):
    playerlist_offset = (140,125)
    player_offset = (490,125)
    pitch_offset = (740,125)

    playerlist_surface, player_rects, hover_player_uuid, selected_player_uuid = draw_tactics_playerlist(game,team, playerlist_offset, "lineup")
    screen.blit(playerlist_surface,playerlist_offset)
    if(selected_player_uuid is not None):
        player_surface = draw_player(game,selected_player_uuid)
        screen.blit(player_surface,player_offset)

    pitch_surface, jersey_rects = draw_tactics_pitch(game,team,hover_player_uuid, selected_player_uuid, pitch_offset)
    screen.blit(pitch_surface,pitch_offset)

    return player_rects, jersey_rects

def draw_tactics_pitch(game, team, hover_player_uuid, selected_player_uuid, pitch_offset):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_on_pitch = mouse_pos[0] - pitch_offset[0], mouse_pos[1] - pitch_offset[1]
    pitch_surface = pygame.Surface((600,600), pygame.SRCALPHA)
    pitch = pygame.image.load("images/pitch.png")
    pitch = pygame.transform.scale(pitch,(int(611*0.60),int(1000*0.60)))
    pitch_rect = pitch.get_rect()
    pitch_surface.blit(pitch,pitch_rect)
    position_list = [("goalkeeper",(140,525)),("libero",(140,455)),("leftdef",(40,405)),("rightdef",(240,405)),("lefthalf",(10,335)),("righthalf",(270,335)),("leftmid",(25,235)),("centralmid",(140,275)),("rightmid",(255,235)),("leftattack",(60,135)),("rightattack",(220,135)),("sub1",(380,100)),("sub2",(380,200)),("sub3",(380,300)),("sub4",(380,400)),("sub5",(380,500))]
    jersey_colors = team.return_jersey_colors()
    jersey_decorations = team.return_jersey_decorations()
    logo = team.club.logo
    actual_positions = team.actual_positions
    players = team.get_players()
    jersey_rects = []

    for position in position_list:
        jersey_rect = pygame.Rect(position[1], (90, 70))
        jersey_rects.append(jersey_rect)
        if mouse_pos and jersey_rect.collidepoint(mouse_pos_on_pitch):
            is_hovered = True
        else:
            is_hovered = False
        position_uuid = actual_positions[position[0]]["player_uuid"]
        for player in players:
            player_uuid = player[0]
            if(str(player_uuid) == str(position_uuid)):
                jersey_number = player[1]
                jersey_name = player[3]
                if str(selected_player_uuid) == str(position_uuid):
                    is_selected = True
                else:
                    is_selected = False
                tactics_jersey = draw_tactics_jersey(jersey_colors, jersey_decorations, jersey_number, logo, jersey_name,is_hovered,is_selected)
                pitch_surface.blit(tactics_jersey,position[1])
    return pitch_surface,jersey_rects

def draw_tactics_jersey(jersey_colors, jersey_decorations, number, logo, name, is_hovered=False, is_selected=False):
    is_front = False
    jersey_surface = pygame.Surface((90, 70), pygame.SRCALPHA)
    if is_selected:
        jersey_surface.fill((200,0,0,128))
    if is_hovered:
        jersey_surface.fill((255,200,200,128))
    jersey = draw_jersey(jersey_colors, jersey_decorations,  str(number),logo, is_front = is_front)
    jersey = pygame.transform.scale(jersey, (40, 40))
    jersey_surface.blit(jersey, (25, 0))
    text = very_small_bold_font.render(name, True, BLACK)
    text_rect = pygame.Rect(0, 40, 90, 15)
    # Calculate the position of the text to center it in the text_rect
    text_rect.center = (45, 50)
    text_pos = text.get_rect(center=text_rect.center)
    jersey_surface.blit(text, text_pos)
    return jersey_surface

def draw_tactics_playerlist(game,team, playerlist_offset, useage: str):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_on_list = mouse_pos[0] - playerlist_offset[0], mouse_pos[1] - playerlist_offset[1]

    hover_player_uuid = None

    playerlist_surface = pygame.Surface((600,600), pygame.SRCALPHA)
    header_rect = pygame.Rect(0, 0, 300, 30)
    selected_player_uuid = None

    pygame.draw.rect(playerlist_surface, TABLE_HEADER_COLOR, header_rect)
    header_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    text = header_font.render("Name", True, BLACK)
    text_rect = text.get_rect(left=header_rect.left + 10, centery=header_rect.centery)
    playerlist_surface.blit(text, text_rect)

    text = header_font.render("Position", True, BLACK)
    text_rect = text.get_rect(right=header_rect.right - 10, centery=header_rect.centery)
    playerlist_surface.blit(text, text_rect)

    player_rects = []
    row_height = 30
    player_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    row_height = FONTSIZE_VERY_SMALL+8

    if useage == "lineup":
        playerlist = team.get_players()
    else:
        playerlist = team.get_players_positions()

    for i, player in enumerate(playerlist):
        if i % 2 == 0:
            row_color = TABLE_ROW_EVEN_COLOR
        else:
            row_color = TABLE_ROW_ODD_COLOR
        if(game.selected_player_index == i):
            row_color = (200,0,0)
            selected_player_uuid = player[0]
            #print(f"{player[2]} {selected_player_uuid}")
        row_rect = pygame.Rect(0, 30 + i * row_height, 300, row_height)
        if mouse_pos and row_rect.collidepoint(mouse_pos_on_list):
            row_color = (255,200,200)
            hover_player_uuid = player[0]


        pygame.draw.rect(playerlist_surface, row_color, row_rect)

        player_rects.append(row_rect)

        text = player_font.render(str(player[1]) + ") " + player[2] + " " + player[3], True, BLACK)
        text_rect = text.get_rect(left=row_rect.left + 10, centery=row_rect.centery)
        playerlist_surface.blit(text, text_rect)

        if useage == "lineup":
            text = player_font.render(player[5], True, BLACK)
        else:
            text = player_font.render(player[6], True, BLACK)
        text_rect = text.get_rect(right=row_rect.right - 10, centery=row_rect.centery)
        playerlist_surface.blit(text, text_rect)
    return playerlist_surface,player_rects,hover_player_uuid, selected_player_uuid

def draw_tactics_choose_longpasses(game, tactics_offset,longballs_selected):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_on_list = mouse_pos[0] - tactics_offset[0], mouse_pos[1] - tactics_offset[1]

    longpasses_surface = pygame.Surface((150,600), pygame.SRCALPHA)
    header_rect = pygame.Rect(0, 0, 150, 30)

    pygame.draw.rect(longpasses_surface, TABLE_HEADER_COLOR, header_rect)
    header_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    text = header_font.render("Percentage of passes long", True, BLACK)
    text_rect = text.get_rect(left=header_rect.left + 10, centery=header_rect.centery)
    longpasses_surface.blit(text, text_rect)
    longpass_rects = []
    row_height = 30
    player_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    row_height = FONTSIZE_VERY_SMALL+8

    for i in range(11):
        if i % 2 == 0:
            row_color = TABLE_ROW_EVEN_COLOR
        else:
            row_color = TABLE_ROW_ODD_COLOR        
        row_rect = pygame.Rect(0, 30 + i * row_height, 300, row_height)
        if mouse_pos and row_rect.collidepoint(mouse_pos_on_list):
            row_color = (255,200,200)
        if(longballs_selected == i):
            row_color = (200,0,0)

        #    hover_player_uuid = player[0]


        pygame.draw.rect(longpasses_surface, row_color, row_rect)

        longpass_rects.append(row_rect)

        text = player_font.render(str(i) + "0 % ", True, BLACK)
        text_rect = text.get_rect(left=row_rect.left + 10, centery=row_rect.centery)
        longpasses_surface.blit(text, text_rect)
    return longpasses_surface, longpass_rects

def draw_tactics_choose_defense(game, tactics_offset,defense_selected):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_on_list = mouse_pos[0] - tactics_offset[0], mouse_pos[1] - tactics_offset[1]

    defense_surface = pygame.Surface((150,600), pygame.SRCALPHA)
    header_rect = pygame.Rect(0, 0, 150, 30)

    defense_tactics = ['Neutral', 'High pressure', 'Park the buss', 'Garbage bag']

    pygame.draw.rect(defense_surface, TABLE_HEADER_COLOR, header_rect)
    header_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    text = header_font.render("Defencive tactics", True, BLACK)
    text_rect = text.get_rect(left=header_rect.left + 10, centery=header_rect.centery)
    defense_surface.blit(text, text_rect)
    longpass_rects = []
    row_height = 30
    player_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    row_height = FONTSIZE_VERY_SMALL+8

    for i, defense_tactic in enumerate(defense_tactics):
        if i % 2 == 0:
            row_color = TABLE_ROW_EVEN_COLOR
        else:
            row_color = TABLE_ROW_ODD_COLOR        
        row_rect = pygame.Rect(0, 30 + i * row_height, 300, row_height)
        if mouse_pos and row_rect.collidepoint(mouse_pos_on_list):
            row_color = (255,200,200)
        if(defense_selected == i):
            row_color = (200,0,0)

        #    hover_player_uuid = player[0]


        pygame.draw.rect(defense_surface, row_color, row_rect)

        longpass_rects.append(row_rect)

        text = player_font.render(defense_tactic, True, BLACK)
        text_rect = text.get_rect(left=row_rect.left + 10, centery=row_rect.centery)
        defense_surface.blit(text, text_rect)
    return defense_surface, longpass_rects

def draw_player(game,player_uuid):
    player_surface = pygame.Surface((250,600), pygame.SRCALPHA)
    player = game.player_manager.find_player_by_uuid(player_uuid)
    #print(player_uuid)
    text = small_font.render(f"{player.first_name} {player.last_name}", True, BLACK)
    text_rect = pygame.Rect(0, 0, 250, 20)
    player_surface.blit(text,text_rect)

    text = small_font.render(f"Age: {player.age}", True, BLACK)
    text_rect = pygame.Rect(0, 20, 250, 20)
    player_surface.blit(text,text_rect)

    text = small_font.render(f"Nationality: {game.countries[player.nationality].name}", True, BLACK)
    text_rect = pygame.Rect(0, 40, 250, 20)
    player_surface.blit(text,text_rect)

    attributes = []
    i=0
    if player.position == "goalkeeper":
        attribute_list = ['Saveing','Reflexes','Placement','Throwing','Skating','Acceleration', 'Agility', 'Agression','Endurance']
    else:
        attribute_list = ["Dribbling", "Intercept", 'Shooting', 'Passing', 'Long pass', 'Corners','Skating','Acceleration', 'Agility', 'Agression','Endurance']
    for attribute_name in attribute_list:
        attribute = player.get_attribute(attribute_name)
        if attribute:
            if attribute.name == "Saveing":
                text = very_small_bold_font.render("Goalkeeper attributes", True, BLACK)
                text_rect = pygame.Rect(0, 80 + i*15 , 250, 15)
                player_surface.blit(text,text_rect)
                i += 1
            if attribute.name == "Dribbling":
                text = very_small_bold_font.render("Outfield attributes", True, BLACK)
                text_rect = pygame.Rect(0, 80 + i*15 , 250, 15)
                player_surface.blit(text,text_rect)
                i += 1
            if attribute.name == "Skating":
                i += 1
                text = very_small_bold_font.render("Generic attributes", True, BLACK)
                text_rect = pygame.Rect(0, 80 + i*15 , 250, 15)
                player_surface.blit(text,text_rect)
                i += 1

            #attributes.append(f"{attribute.name}: {attribute.level}")
            attributes_text = f"{attribute.name}: {attribute.level}"
            text = very_small_font.render(attributes_text, True, BLACK)
            text_rect = pygame.Rect(0, 80 + i*15 , 250, 15)
            player_surface.blit(text,text_rect)
            i += 1

    stats_goalkeeper = player.calculate_composite_values('goalkeeper')
    stats_libero = player.calculate_composite_values('libero')
    stats_defender = player.calculate_composite_values('leftdef')
    stats_half = player.calculate_composite_values('lefthalf')
    stats_midfield = player.calculate_composite_values('leftmid')
    stats_attack = player.calculate_composite_values('leftattack')

    i +=2

    attributes_text = f"Goalkeeper: {int(stats_goalkeeper[0])} - {int(stats_goalkeeper[1])}"
    text = very_small_font.render(attributes_text, True, BLACK)
    text_rect = pygame.Rect(0, 80 + i*15 , 250, 15)
    player_surface.blit(text,text_rect)
    i += 1

    attributes_text = f"Libero: {int(stats_libero[0])} - {int(stats_libero[1])}"
    text = very_small_font.render(attributes_text, True, BLACK)
    text_rect = pygame.Rect(0, 80 + i*15 , 250, 15)
    player_surface.blit(text,text_rect)
    i += 1

    attributes_text = f"Defender: {int(stats_defender[0])} - {int(stats_defender[1])}"
    text = very_small_font.render(attributes_text, True, BLACK)
    text_rect = pygame.Rect(0, 80 + i*15 , 250, 15)
    player_surface.blit(text,text_rect)
    i += 1

    attributes_text = f"Half back: {int(stats_half[0])} - {int(stats_half[1])}"
    text = very_small_font.render(attributes_text, True, BLACK)
    text_rect = pygame.Rect(0, 80 + i*15 , 250, 15)
    player_surface.blit(text,text_rect)
    i += 1

    attributes_text = f"Midfielder: {int(stats_midfield[0])} - {int(stats_midfield[1])}"
    text = very_small_font.render(attributes_text, True, BLACK)
    text_rect = pygame.Rect(0, 80 + i*15 , 250, 15)
    player_surface.blit(text,text_rect)
    i += 1

    attributes_text = f"Attacker: {int(stats_attack[0])} - {int(stats_attack[1])}"
    text = very_small_font.render(attributes_text, True, BLACK)
    text_rect = pygame.Rect(0, 80 + i*15 , 250, 15)
    player_surface.blit(text,text_rect)
    i += 1

    return player_surface
