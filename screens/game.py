import pygame
from button import Button
from inputbox import InputBox
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,WHITE,BLACK,GRAY,FONTSIZE_LARGE,FONTSIZE_MEDIUM,FONTSIZE_SMALL,FONTSIZE_VERY_SMALL
from constants import TABLE_HEADER_COLOR, TABLE_ROW_ODD_COLOR, TABLE_ROW_EVEN_COLOR
from guielements import font, medium_font, small_font,very_small_font ,very_small_bold_font , button_width, button_height, button_x, button_spacing
from guielements import new_game_button, load_game_button, credits_button, quit_button, new_game_ok_button, input_name, input_age, quit_game, choose_team_button
from guielements import home_button, inbox_button, newspaper_button, senior_squad_button, tactics_button, training_button, schedule_button, competition_button
from guielements import u19_squad_button,forward_time_button, save_game_button, quit_game_button
from miscfunctions import get_club_from_team, draw_calendar, yesterday
from graphicscode.jersey import draw_jersey
from graphicscode.arrows import draw_arrow_left, draw_arrow_right, draw_arrow_up, draw_arrow_down

from debug_functions import print_yesterdays_results

from screens.screensleague import draw_league_table, draw_schedule


pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

x_offset = 150

def draw_squad(game,team):
    title_rect = pygame.Rect(140, 110, 600, 40)
    title_text = small_font.render(f"Squad for {team.name}", True, BLACK)
    screen.blit(title_text,title_rect)
    playerlist_offset = (140,125)
    player_offset = (790,125)
    playerlist_surface, player_rects, hover_player_uuid, selected_player_uuid = draw_playerlist(game,team, playerlist_offset)
    screen.blit(playerlist_surface,playerlist_offset)
    if(selected_player_uuid is not None):
        player_surface = draw_player(game,selected_player_uuid)
        screen.blit(player_surface,player_offset)
    return player_rects

def draw_playerlist(game,team, playerlist_offset):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_on_list = mouse_pos[0] - playerlist_offset[0], mouse_pos[1] - playerlist_offset[1]

    hover_player_uuid = None

    playerlist_surface = pygame.Surface((600,600), pygame.SRCALPHA)
    header_rect = pygame.Rect(0, 0, 600, 30)
    selected_player_uuid = None

    pygame.draw.rect(playerlist_surface, TABLE_HEADER_COLOR, header_rect)

    header_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    text = header_font.render("Name", True, BLACK)
    text_rect = text.get_rect(left=header_rect.left + 10, centery=header_rect.centery)
    playerlist_surface.blit(text, text_rect)

    text = header_font.render("Age", True, BLACK)
    text_rect = text.get_rect(centerx=header_rect.centerx, centery=header_rect.centery)
    playerlist_surface.blit(text, text_rect)

    text = header_font.render("Position", True, BLACK)
    text_rect = text.get_rect(right=header_rect.right - 10, centery=header_rect.centery)
    playerlist_surface.blit(text, text_rect)

    player_rects = []
    row_height = 30
    player_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    row_height = FONTSIZE_VERY_SMALL+8
    for i, player in enumerate(team.get_players()):
        if i % 2 == 0:
            row_color = TABLE_ROW_EVEN_COLOR
        else:
            row_color = TABLE_ROW_ODD_COLOR
        if(game.selected_player_index == i):
            row_color = (200,0,0)
            selected_player_uuid = player[0]
            #print(f"{player[2]} {selected_player_uuid}")
        row_rect = pygame.Rect(0, 30 + i * row_height, 600, row_height)
        if mouse_pos and row_rect.collidepoint(mouse_pos_on_list):
            row_color = (255,200,200)
            hover_player_uuid = player[0]


        pygame.draw.rect(playerlist_surface, row_color, row_rect)

        player_rects.append(row_rect)

        text = player_font.render(str(player[1]) + ") " + player[2] + " " + player[3], True, BLACK)
        text_rect = text.get_rect(left=row_rect.left + 10, centery=row_rect.centery)
        playerlist_surface.blit(text, text_rect)

        text = player_font.render(str(player[4]), True, BLACK)
        text_rect = text.get_rect(centerx=row_rect.centerx, centery=row_rect.centery)
        playerlist_surface.blit(text, text_rect)

        text = player_font.render(player[5], True, BLACK)
        text_rect = text.get_rect(right=row_rect.right - 10, centery=row_rect.centery)
        playerlist_surface.blit(text, text_rect)

    return playerlist_surface,player_rects,hover_player_uuid, selected_player_uuid

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

def draw_next_match(game, team):
    next_match_surface = pygame.Surface((300,130), pygame.SRCALPHA)
    next_match_surface.fill(WHITE)
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    next_match = game.match_manager.get_next_match_for_team(team, game.year, game.month, game.day)

    y = 10
    text = medium_font.render("Next game", True, BLACK)
    text_rect = pygame.Rect(10, y,200, 20)
    next_match_surface.blit(text, text_rect)
    if(next_match is not None):
        next_match_hometeam_name = next_match.home_team.name
        next_match_awayteam_name = next_match.away_team.name

        y += 20
        text = small_font.render(next_match.league.name, True, BLACK)
        text_rect = pygame.Rect(10, y,200, 20)
        next_match_surface.blit(text, text_rect)
        y += 20
        text = small_font.render(f"{next_match.day} {month_names[next_match.month-1]}", True, BLACK)
        text_rect = pygame.Rect(10, y ,200, 20)
        next_match_surface.blit(text, text_rect)
        y += 20
        text = small_font.render(f"{next_match_hometeam_name} - {next_match_awayteam_name}", True, BLACK)
        text_rect = pygame.Rect(10, y ,200, 20)
        next_match_surface.blit(text, text_rect)
    else:
        y += 20
        text = medium_font.render("No game in system", True, BLACK)
        text_rect = pygame.Rect(10, y,200, 20)
        next_match_surface.blit(text, text_rect)

    border_surface = pygame.Surface((next_match_surface.get_width() + 4, next_match_surface.get_height() + 4))
    border_surface.fill(BLACK)
    border_surface.blit(next_match_surface, (2, 2))

    return border_surface


def draw_yesterday_results(game, team, list_offset):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_on_list = mouse_pos[0] - list_offset[0], mouse_pos[1] - list_offset[1]

    year_yesterday, month_yesterday, day_yesterday = yesterday(game.year, game.month, game.day)
    matches_today = game.match_manager.get_matches_by_date(year_yesterday, month_yesterday, day_yesterday)
    yesterdays_result_surface = pygame.Surface((375,600), pygame.SRCALPHA)
    yesterdays_result_surface.fill(WHITE)
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    arrow_rects = []

    if len(matches_today) > 0:
        #print_yesterdays_results(game)
        y = 10
        text = medium_font.render(f"Matches {day_yesterday} {month_names[month_yesterday-1]} {year_yesterday}", True, BLACK)
        y += 5
        last_league = ""
        text_rect = pygame.Rect(10, y,200, 20)
        yesterdays_result_surface.blit(text, text_rect)
        for match in matches_today:
            match_league = game.match_manager.get_league_of_match(match)
            if match_league.name != last_league:
                last_league = match_league.name
                country = match_league.country
                flag = game.return_countryflag(country)
                y+=25
                text = medium_font.render(f"{match_league.name}", True, (80,80,80))
                combined_surface = pygame.Surface((375,30))
                combined_surface.fill((240,240,240))
                combined_surface.blit(text, (4,4))
                combined_surface.blit(flag, (325,2))
                rect = combined_surface.get_rect()
                rect.topleft = (0, y)
                yesterdays_result_surface.blit(combined_surface, rect)
                y+=12
            y += 20
            if(match.home_team.name == team or match.away_team.name == team):
                row_text_color = (255,0,0)
            else:
                row_text_color = (0,0,0)
            text = small_font.render(f"{match.home_team.name} - {match.away_team.name}: {match.home_goals} - {match.away_goals}", True, row_text_color)
            text_rect = pygame.Rect(10, y,375, 20)
            yesterdays_result_surface.blit(text, text_rect)
            #print (f"{match.home_team.name} - {match.away_team.name}: {match.home_goals} - {match.away_goals}")

    border_surface = pygame.Surface((yesterdays_result_surface.get_width() + 4, yesterdays_result_surface.get_height() + 4))
    border_surface.fill(BLACK)
    border_surface.blit(yesterdays_result_surface, (2, 2))

    total_surface = pygame.Surface((border_surface.get_width() + 60, border_surface.get_height()))
    total_surface.fill(WHITE)
    total_surface.blit(border_surface,(0,0))

    arrow_rect = pygame.Rect(total_surface.get_width() -50, 10, 50, 50)
    arrow_rects.append(arrow_rect)
    if mouse_pos and arrow_rect.collidepoint(mouse_pos_on_list):
        arrow_color = (200,100,100)
    else:
        arrow_color = (0,0,0)
    arrow_surface = draw_arrow_up(arrow_color)
    total_surface.blit(arrow_surface,arrow_rect)
    arrow_rect = pygame.Rect(total_surface.get_width() -50, total_surface.get_height() - 60, 50, 50)
    arrow_rects.append(arrow_rect)
    if mouse_pos and arrow_rect.collidepoint(mouse_pos_on_list):
        arrow_color = (200,100,100)
    else:
        arrow_color = (0,0,0)
    arrow_surface = draw_arrow_down(arrow_color)
    total_surface.blit(arrow_surface,arrow_rect)
    return total_surface, arrow_rects




def draw_home(game,team):
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    list_offset = (470,110)
    arrow_rects = []
    next_match_surface = draw_next_match(game,team)
    screen.blit(next_match_surface,(150,110))
    if game.isMatchesPlayed == True:
        #year_yesterday, month_yesterday, day_yesterday = yesterday(game.year, game.month, game.day)
        yesterdays_result_surface, arrow_rects = draw_yesterday_results(game, team, list_offset)
        screen.blit(yesterdays_result_surface,list_offset)

    #arrow_surface = draw_arrow_left((0,0,0))
    #screen.blit(arrow_surface,(200,300))
    #arrow_surface = draw_arrow_right((200,0,0))
    #screen.blit(arrow_surface,(300,300))
    #arrow_surface = draw_arrow_up((0,100,0))
    #screen.blit(arrow_surface,(200,400))
    #arrow_surface = draw_arrow_down((0,0,70))
    #screen.blit(arrow_surface,(300,400))
    return arrow_rects

def draw_tactics(game,team):
    playerlist_offset = (140,125)
    player_offset = (490,125)
    pitch_offset = (740,125)

    playerlist_surface, player_rects, hover_player_uuid, selected_player_uuid = draw_tactics_playerlist(game,team, playerlist_offset)
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

def draw_tactics_playerlist(game,team, playerlist_offset):
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
    for i, player in enumerate(team.get_players()):
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

        text = player_font.render(player[5], True, BLACK)
        text_rect = text.get_rect(right=row_rect.right - 10, centery=row_rect.centery)
        playerlist_surface.blit(text, text_rect)
    return playerlist_surface,player_rects,hover_player_uuid, selected_player_uuid


def draw_game_mainscreen(game):
    # Draw screen
    screen.fill(WHITE)
    title = font.render("Bandymanager - Main screen", True, BLACK)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 40))
    screen.blit(title, title_rect)

    rectlist_1 = []
    rectlist_2 = []

    manager_name = game.manager.return_name()
    manager_team_name = game.manager.return_team()
    manager_team = game.teams[manager_team_name]
    manager_club = get_club_from_team(game, manager_team)
    manager_club_name = manager_club.name

    if(manager_team.team_type == "Men"):
        manager_u19teams = manager_club.get_teams_by_type("Men U19")
    else:
        manager_u19teams = manager_club.get_teams_by_type("Women U19")

    manager_u19team = manager_u19teams[0]
    toprow_font = pygame.font.Font(None, FONTSIZE_SMALL)
    text = toprow_font.render(f"Manager: {manager_name}    Club: {manager_club_name}", True, BLACK)
    text_rect = (10+x_offset,80,600,30)
    #text_rect = text.get_rect(left=header_rect.left + 10, centery=header_rect.centery)
    screen.blit(text, text_rect)

    calendar_surface = draw_calendar(game.year, game.month, game.day)

    home_button.draw(screen)
    inbox_button.draw(screen)
    newspaper_button.draw(screen)
    senior_squad_button.draw(screen)
    tactics_button.draw(screen)
    training_button.draw(screen)
    schedule_button.draw(screen)
    competition_button.draw(screen)
    u19_squad_button.draw(screen)
    forward_time_button.draw(screen)
    save_game_button.draw(screen)
    quit_game_button.draw(screen)

    screen.blit(calendar_surface, (1150,10))

    leagues = game.get_leagues_for_team(manager_team_name)

    if (game.game_page == "home"):
        rectlist_1 = draw_home(game,manager_team_name)
    if (game.game_page == "player_list"):
        if game.inspected_team is not None:
            team_viewed = game.inspected_team
        else:
            team_viewed = manager_team
        #print(f"team viewed {team_viewed}, inspected_team {game.inspected_team}")
        rectlist_1 = draw_squad(game,team_viewed)
    if (game.game_page == "tactics"):
        rectlist_1, rectlist_2 = draw_tactics(game,manager_team)
    if (game.game_page == "schedule"):
        rectlist_1 = draw_schedule(game,screen, leagues[0].name, manager_team)
    if (game.game_page == "competition"):
        league_table_surface, rectlist_1 = draw_league_table(game, manager_team)
        screen.blit(league_table_surface,(140,110))
    if (game.game_page == "player_list_u19"):
        rectlist_1 = draw_squad(game,manager_u19team)
    # Update display
    pygame.display.flip()

    return rectlist_1, rectlist_2
