import pygame
from button import Button
from inputbox import InputBox
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,WHITE,BLACK,GRAY,FONTSIZE_LARGE,FONTSIZE_MEDIUM,FONTSIZE_SMALL,FONTSIZE_VERY_SMALL
from constants import TABLE_HEADER_COLOR, TABLE_ROW_ODD_COLOR, TABLE_ROW_EVEN_COLOR
from guielements import font, medium_font, small_font,very_small_font ,very_small_bold_font , button_width, button_height, button_x, button_spacing
from guielements import new_game_button, load_game_button, credits_button, quit_button, new_game_ok_button, input_name, input_age, quit_game, choose_team_button
from guielements import home_button, inbox_button, newspaper_button, senior_squad_button, tactics_button, training_button, schedule_button, competition_button
from guielements import u19_squad_button,forward_time_button, save_game_button, quit_game_button
from miscfunctions import get_club_from_team, draw_calendar, draw_jersey

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

x_offset = 150

def draw_playerlist(game,team, selected_player_index):
    # Draw player table
    header_rect = pygame.Rect(10+x_offset, 100, 600, 30)
    selected_player_uuid = None

    pygame.draw.rect(screen, TABLE_HEADER_COLOR, header_rect)
    header_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    text = header_font.render("Name", True, BLACK)
    text_rect = text.get_rect(left=header_rect.left + 10, centery=header_rect.centery)
    screen.blit(text, text_rect)

    text = header_font.render("Age", True, BLACK)
    text_rect = text.get_rect(centerx=header_rect.centerx, centery=header_rect.centery)
    screen.blit(text, text_rect)

    text = header_font.render("Position", True, BLACK)
    text_rect = text.get_rect(right=header_rect.right - 10, centery=header_rect.centery)
    screen.blit(text, text_rect)

    player_rects = []
    row_height = 30
    player_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    row_height = FONTSIZE_VERY_SMALL+8
    for i, player in enumerate(team.get_players()):
        if i % 2 == 0:
            row_color = TABLE_ROW_EVEN_COLOR
        else:
            row_color = TABLE_ROW_ODD_COLOR
        if(selected_player_index == i):
            row_color = (200,0,0)
            selected_player_uuid = player[0]
            #print(f"{player[2]} {selected_player_uuid}")
        row_rect = pygame.Rect(10+x_offset, 130 + i * row_height, 600, row_height)
        pygame.draw.rect(screen, row_color, row_rect)

        player_rects.append(row_rect)

        text = player_font.render(str(player[1]) + ") " + player[2] + " " + player[3], True, BLACK)
        text_rect = text.get_rect(left=row_rect.left + 10, centery=row_rect.centery)
        screen.blit(text, text_rect)

        text = player_font.render(str(player[4]), True, BLACK)
        text_rect = text.get_rect(centerx=row_rect.centerx, centery=row_rect.centery)
        screen.blit(text, text_rect)

        text = player_font.render(player[5], True, BLACK)
        text_rect = text.get_rect(right=row_rect.right - 10, centery=row_rect.centery)
        screen.blit(text, text_rect)
    #print(len(player_rects))
    #print(player_rects)
    if(selected_player_uuid is not None):
        draw_player(game,selected_player_uuid)
    return player_rects

def draw_player(game,player_uuid):
    player = game.player_manager.find_player_by_uuid(player_uuid)
    #print(player_uuid)
    text = medium_font.render(f"{player.first_name} {player.last_name}", True, BLACK)
    text_rect = pygame.Rect(790, 160, 300, 30)
    screen.blit(text,text_rect)

    text = medium_font.render(f"Age: {player.age}", True, BLACK)
    text_rect = pygame.Rect(790, 190, 300, 30)
    screen.blit(text,text_rect)

    text = medium_font.render(f"Nationality: {game.countries[player.nationality].name}", True, BLACK)
    text_rect = pygame.Rect(790, 220, 300, 30)
    screen.blit(text,text_rect)

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
                text_rect = pygame.Rect(790, 250 + i*15 , 300, 15)
                screen.blit(text,text_rect)
                i += 1
            if attribute.name == "Dribbling":
                text = very_small_bold_font.render("Outfield attributes", True, BLACK)
                text_rect = pygame.Rect(790, 250 + i*15 , 300, 15)
                screen.blit(text,text_rect)
                i += 1
            if attribute.name == "Skating":
                i += 1
                text = very_small_bold_font.render("Generic attributes", True, BLACK)
                text_rect = pygame.Rect(790, 250 + i*15 , 300, 15)
                screen.blit(text,text_rect)
                i += 1

            #attributes.append(f"{attribute.name}: {attribute.level}")
            attributes_text = f"{attribute.name}: {attribute.level}"
            text = very_small_font.render(attributes_text, True, BLACK)
            text_rect = pygame.Rect(790, 250 + i*15 , 300, 15)
            screen.blit(text,text_rect)
            i += 1


def draw_home(game,team):
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    next_match = game.match_manager.get_next_match_for_team(team, game.year, game.month, game.day)
    if(next_match is not None):
        #print(next_match)
        next_match_hometeam_name = next_match.home_team.name
        next_match_awayteam_name = next_match.away_team.name

        small_font = pygame.font.Font(None, FONTSIZE_SMALL)

        y = 130
        text = small_font.render("Next game", True, BLACK)
        text_rect = pygame.Rect(10+x_offset, y,200, 20)
        screen.blit(text, text_rect)
        y += 20
        text = small_font.render(next_match.league.name, True, BLACK)
        text_rect = pygame.Rect(10+x_offset, y,200, 20)
        screen.blit(text, text_rect)
        y += 20
        text = small_font.render(f"{next_match.day} {month_names[next_match.month-1]}", True, BLACK)
        text_rect = pygame.Rect(10+x_offset, y ,200, 20)
        screen.blit(text, text_rect)
        y += 20
        text = small_font.render(f"{next_match_hometeam_name} - {next_match_awayteam_name}", True, BLACK)
        text_rect = pygame.Rect(10+x_offset, y ,200, 20)
        screen.blit(text, text_rect)

def draw_league_table(game, selected_league):
    league = game.return_league_by_name(selected_league)

    # Define table header
    header_rect = pygame.Rect(10+x_offset, 100, 600, 30)
    pygame.draw.rect(screen, TABLE_HEADER_COLOR, header_rect)

    # Define header font and draw header labels
    header_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    text = header_font.render("Team", True, BLACK)
    text_rect = text.get_rect(left=header_rect.left + 10, centery=header_rect.centery)
    screen.blit(text, text_rect)

    text = header_font.render("Played", True, BLACK)
    text_rect = text.get_rect(centerx=header_rect.left + 150, centery=header_rect.centery)
    screen.blit(text, text_rect)

    text = header_font.render("Wins", True, BLACK)
    text_rect = text.get_rect(centerx=header_rect.left + 200, centery=header_rect.centery)
    screen.blit(text, text_rect)

    text = header_font.render("Draws", True, BLACK)
    text_rect = text.get_rect(centerx=header_rect.left + 270, centery=header_rect.centery)
    screen.blit(text, text_rect)

    text = header_font.render("Losses", True, BLACK)
    text_rect = text.get_rect(centerx=header_rect.left + 350, centery=header_rect.centery)
    screen.blit(text, text_rect)

    text = header_font.render("GF", True, BLACK)
    text_rect = text.get_rect(centerx=header_rect.left + 420, centery=header_rect.centery)
    screen.blit(text, text_rect)

    text = header_font.render("GA", True, BLACK)
    text_rect = text.get_rect(centerx=header_rect.left + 500, centery=header_rect.centery)
    screen.blit(text, text_rect)

    text = header_font.render("Points", True, BLACK)
    text_rect = text.get_rect(centerx=header_rect.left + 580, centery=header_rect.centery)
    screen.blit(text, text_rect)

    # Define font for team names and table rows
    team_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    row_height = FONTSIZE_VERY_SMALL + 8

    #print(selected_league)
    #print(league)

    # Sort the table by points, then by goal difference, then by goals for
    sorted_table = sorted(league.table.items(), key=lambda x: (-x[1]['points'], -x[1]['goals_for'] + x[1]['goals_against'], -x[1]['goals_for']))

    player_font = pygame.font.Font(None, FONTSIZE_SMALL)
    for i, team in enumerate(sorted_table):
        if i % 2 == 0:
            row_color = TABLE_ROW_EVEN_COLOR
        else:
            row_color = TABLE_ROW_ODD_COLOR


        row_rect = pygame.Rect(10+x_offset, 130 + i * row_height, 600, row_height)
        pygame.draw.rect(screen, row_color, row_rect)

        text = player_font.render(str(i+1), True, BLACK)
        text_rect = text.get_rect(left=row_rect.left + 10, centery=row_rect.centery)
        screen.blit(text, text_rect)

        league_row = team[1]
        text = player_font.render(team[0].name, True, BLACK)
        text_rect = text.get_rect(left=row_rect.left + 40, centery=row_rect.centery)
        screen.blit(text, text_rect)

        played = league_row['played']
        text = player_font.render(str(played), True, BLACK)
        text_rect = text.get_rect(centerx=row_rect.left + 180, centery=row_rect.centery)
        screen.blit(text, text_rect)

        won = league_row['won']
        text = player_font.render(str(won), True, BLACK)
        text_rect = text.get_rect(centerx=row_rect.left + 210, centery=row_rect.centery)
        screen.blit(text, text_rect)

        drawn = league_row['drawn']
        text = player_font.render(str(drawn), True, BLACK)
        text_rect = text.get_rect(centerx=row_rect.left + 270, centery=row_rect.centery)
        screen.blit(text, text_rect)

        lost = league_row['lost']
        text = player_font.render(str(lost), True, BLACK)
        text_rect = text.get_rect(centerx=row_rect.left + 330, centery=row_rect.centery)
        screen.blit(text, text_rect)

        goals_for = league_row['goals_for']
        text = player_font.render(str(goals_for), True, BLACK)
        text_rect = text.get_rect(centerx=row_rect.left + 390, centery=row_rect.centery)
        screen.blit(text, text_rect)

        goals_against = league_row['goals_against']
        text = player_font.render(str(goals_against), True, BLACK)
        text_rect = text.get_rect(centerx=row_rect.left + 450, centery=row_rect.centery)
        screen.blit(text, text_rect)

        gd = goals_for - goals_against
        text = player_font.render(str(gd), True, BLACK)
        text_rect = text.get_rect(centerx=row_rect.left + 510, centery=row_rect.centery)
        screen.blit(text, text_rect)

        points = league_row['points']
        text = player_font.render(str(points), True, BLACK)
        text_rect = text.get_rect(centerx=row_rect.left + 570, centery=row_rect.centery)
        screen.blit(text, text_rect)

def draw_tactics(game,team):
    pitch = pygame.image.load("images/pitch.png")
    pitch = pygame.transform.scale(pitch,(int(611*0.60),int(1000*0.60)))
    pitch_rect = pitch.get_rect()
    pitch_rect.left=700
    pitch_rect.top=125
    screen.blit(pitch,pitch_rect)

    jersey_colors = team.return_jersey_colors()

    actual_positions = team.actual_positions
    players = team.get_players()
    goalkeeper_uuid = actual_positions["goalkeeper"]["player_uuid"]
    for player in players:
        player_uuid = player[0]
        #print(f" {player_uuid} - {goalkeeper_uuid}")
        if(str(player_uuid) == str(goalkeeper_uuid)):
            jersey_number = player[1]
            jersey_name = player[3]
            draw_tactics_jersey(0,jersey_colors,jersey_number,jersey_name)

    #print(actual_positions["goalkeeper"]["player_uuid"])
    #for actual_position in actual_positions:
    #    print(actual_position)
    #    #print(actual_position['player_uuid'])


    draw_tactics_jersey(1,jersey_colors,2,"Lindquist")
    draw_tactics_jersey(2,jersey_colors,3,"Jansson")
    draw_tactics_jersey(3,jersey_colors,4,"Berg")
    draw_tactics_jersey(4,jersey_colors,5,"Karlsson")
    draw_tactics_jersey(5,jersey_colors,6,"Muhren")
    draw_tactics_jersey(6,jersey_colors,7,"Fosshaug")
    draw_tactics_jersey(7,jersey_colors,11,"Erixon")
    draw_tactics_jersey(8,jersey_colors,19,"Johansson")
    draw_tactics_jersey(9,jersey_colors,13,"Jonung")
    draw_tactics_jersey(10,jersey_colors,8,"Larsson")

def draw_tactics_jersey(position,jersey_colors,number,name):
    if (position == 0):
        x_pos = 864
        y_pos = 650
    if (position == 1):
        x_pos = 864
        y_pos = 580
    if (position == 2):
        x_pos = 764
        y_pos = 530
    if (position == 3):
        x_pos = 964
        y_pos = 530
    if (position == 4):
        x_pos = 710
        y_pos = 490
    if (position == 5):
        x_pos = 1018
        y_pos = 490
    if (position == 6):
        x_pos = 864
        y_pos = 440
    if (position == 7):
        x_pos = 764
        y_pos = 390
    if (position == 8):
        x_pos = 964
        y_pos = 390
    if (position == 9):
        x_pos = 710
        y_pos = 210
    if (position == 10):
        x_pos = 1018
        y_pos = 210
    jersey = draw_jersey(jersey_colors,str(number))
    jersey = pygame.transform.scale(jersey,(40,40))
    screen.blit(jersey,(x_pos,y_pos))
    text = very_small_bold_font.render(name, True, BLACK)
    text_rect = pygame.Rect(x_pos-10, y_pos+40 , 90, 15)
    screen.blit(text,text_rect)

def draw_game_mainscreen(game, game_page, selected_player_index):
    # Draw screen
    screen.fill(WHITE)
    title = font.render("Bandymanager - Main screen", True, BLACK)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 40))
    screen.blit(title, title_rect)

    list1 = []

    manager_name = game.manager.return_name()
    manager_team_name = game.manager.return_team()
    manager_team = game.teams[manager_team_name]
    manager_club = get_club_from_team(game, manager_team)
    manager_club_name = manager_club.name

    manager_u19teams = manager_club.get_teams_by_type("Men U19")
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

    if (game_page == "home"):
        draw_home(game,manager_team_name)
    if (game_page == "player_list"):
        list1 = draw_playerlist(game,manager_team, selected_player_index)
    if (game_page == "tactics"):
        draw_tactics(game,manager_team)
    if (game_page == "competition"):
        draw_league_table(game, "Elitserien")
    if (game_page == "player_list_u19"):
        list1 = draw_playerlist(game,manager_u19team, selected_player_index)
    # Update display
    pygame.display.flip()

    return list1
