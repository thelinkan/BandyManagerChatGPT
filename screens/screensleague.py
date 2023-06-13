import pygame

from constants import SCREEN_WIDTH,SCREEN_HEIGHT,WHITE,BLACK,GRAY,FONTSIZE_LARGE,FONTSIZE_MEDIUM,FONTSIZE_SMALL,FONTSIZE_VERY_SMALL
from constants import TABLE_HEADER_COLOR, TABLE_ROW_ODD_COLOR, TABLE_ROW_EVEN_COLOR
from guielements import font, medium_font, small_font,very_small_font ,very_small_bold_font , button_width, button_height, button_x, button_spacing
from miscfunctions import get_num_rounds

def draw_league_table(game, highlighted_team):
    selected_league = game.inspected_league
    league = game.return_league_by_name(selected_league)

    teamlist_offset = (140,110)
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_on_list = mouse_pos[0] - teamlist_offset[0], mouse_pos[1] - teamlist_offset[1]
    
    #if game.selected_team_index is not None:
    #    print(f"Selected team {game.selected_team_index}")

    table_width = 600

    league_table_surface = pygame.Surface((table_width,400), pygame.SRCALPHA)
    league_table_surface.fill((255,255,255))


    # Define table header
    header_rect = pygame.Rect(0, 0, table_width, 30)
    pygame.draw.rect(league_table_surface, TABLE_HEADER_COLOR, header_rect)

    # Define header font and draw header labels
    header_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    text = header_font.render("Team", True, BLACK)
    text_rect = text.get_rect(left=header_rect.left + 40, centery=header_rect.centery)
    league_table_surface.blit(text, text_rect)

    text = header_font.render("Played", True, BLACK)
    text_rect = text.get_rect(centerx=header_rect.left + 160, centery=header_rect.centery)
    league_table_surface.blit(text, text_rect)

    text = header_font.render("Wins", True, BLACK)
    text_rect = text.get_rect(centerx=header_rect.left + 200, centery=header_rect.centery)
    league_table_surface.blit(text, text_rect)

    text = header_font.render("Draws", True, BLACK)
    text_rect = text.get_rect(centerx=header_rect.left + 270, centery=header_rect.centery)
    league_table_surface.blit(text, text_rect)

    text = header_font.render("Losses", True, BLACK)
    text_rect = text.get_rect(centerx=header_rect.left + 350, centery=header_rect.centery)
    league_table_surface.blit(text, text_rect)

    text = header_font.render("GF", True, BLACK)
    text_rect = text.get_rect(centerx=header_rect.left + 420, centery=header_rect.centery)
    league_table_surface.blit(text, text_rect)

    text = header_font.render("GA", True, BLACK)
    text_rect = text.get_rect(centerx=header_rect.left + 500, centery=header_rect.centery)
    league_table_surface.blit(text, text_rect)

    text = header_font.render("Points", True, BLACK)
    text_rect = text.get_rect(centerx=header_rect.left + 580, centery=header_rect.centery)
    league_table_surface.blit(text, text_rect)

    # Define font for team names and table rows
    team_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    row_height = FONTSIZE_VERY_SMALL + 8

    # Sort the table by points, then by goal difference, then by goals for
    sorted_table = sorted(league.table.items(), key=lambda x: (-x[1]['points'], -x[1]['goals_for'] + x[1]['goals_against'], -x[1]['goals_for']))

    team_rects = []

    player_font = pygame.font.Font(None, FONTSIZE_SMALL)
    for i, team in enumerate(sorted_table):
        if i == game.selected_team_index:
            game.game_page="player_list"
            game.inspected_team=team[0]
        if i % 2 == 0:
            row_color = TABLE_ROW_EVEN_COLOR
        else:
            row_color = TABLE_ROW_ODD_COLOR

        #print(f"{team[0].name} - {highlighted_team}")
        if team[0].name == highlighted_team.name:
            row_text_color = (255,0,0)
        else:
            row_text_color = BLACK

        row_surface = pygame.Surface((table_width,row_height), pygame.SRCALPHA)

        row_rect = row_surface.get_rect()
        row_rect.top = 30 + i * row_height
        row_rect.left = 0
        if mouse_pos and row_rect.collidepoint(mouse_pos_on_list):
            row_color = (255,200,200)
        row_surface.fill(row_color)

        team_rects.append(row_rect)

        text = player_font.render(str(i+1), True, row_text_color)
        text_rect = text.get_rect(left=4, top=4)
        row_surface.blit(text, text_rect)

        league_row = team[1]
        text = player_font.render(team[0].name, True, row_text_color)
        text_rect = text.get_rect(left=40, top=4)
        row_surface.blit(text, text_rect)

        played = league_row['played']
        text = player_font.render(str(played), True, row_text_color)
        text_rect = text.get_rect(left=180, top=4)
        row_surface.blit(text, text_rect)

        won = league_row['won']
        text = player_font.render(str(won), True, row_text_color)
        text_rect = text.get_rect(left=210, top=4)
        row_surface.blit(text, text_rect)

        drawn = league_row['drawn']
        text = player_font.render(str(drawn), True, row_text_color)
        text_rect = text.get_rect(left=270, top=4)
        row_surface.blit(text, text_rect)

        lost = league_row['lost']
        text = player_font.render(str(lost), True, row_text_color)
        text_rect = text.get_rect(left=330, top=4)
        row_surface.blit(text, text_rect)

        goals_for = league_row['goals_for']
        text = player_font.render(str(goals_for), True, row_text_color)
        text_rect = text.get_rect(left=390, top=4)
        row_surface.blit(text, text_rect)

        goals_against = league_row['goals_against']
        text = player_font.render(str(goals_against), True, row_text_color)
        text_rect = text.get_rect(left=450, top=4)
        row_surface.blit(text, text_rect)

        gd = goals_for - goals_against
        text = player_font.render(str(gd), True, row_text_color)
        text_rect = text.get_rect(left=510, top=4)
        row_surface.blit(text, text_rect)

        points = league_row['points']
        text = player_font.render(str(points), True, row_text_color)
        text_rect = text.get_rect(left=570, top=4)
        row_surface.blit(text, text_rect)

        league_table_surface.blit(row_surface, row_rect)

    return league_table_surface,team_rects

def draw_schedule_page(game, screen, selected_league, highlighted_team,page):
    league = game.return_league_by_name(selected_league)
    num_teams = league.num_teams
    num_rounds = league.num_rounds

    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    rounds_per_page,num_pages = get_num_rounds(num_teams,num_rounds)

    schedule_surface = pygame.Surface((350,600), pygame.SRCALPHA)
    schedule_surface.fill(WHITE)
    y=10
    text = medium_font.render(selected_league, True, BLACK)
    text_rect = pygame.Rect(10, y,200, 20)
    schedule_surface.blit(text, text_rect)

    matches_league = game.match_manager.get_matches_by_league(selected_league)

    if len(matches_league) > 0:
        round = 0
        last_month = 0
        last_day = 0
        for match in matches_league:
            if match.day != last_day or match.month != last_month:
                round += 1
                last_day = match.day
                last_month = match.month
                if round > rounds_per_page*(page-1) and round <= rounds_per_page*page:
                    y += 30
                    row_text_color = (0,0,0)
                    text = small_font.render(f"{match.day} {month_names[match.month-1]} {match.year}: ", True, row_text_color)
                    text_rect = pygame.Rect(10, y,200, 20)
                    schedule_surface.blit(text, text_rect)

            if round > rounds_per_page*(page-1) and round <= rounds_per_page*page:
                y += 20
                if(match.home_team.name == highlighted_team.name or match.away_team.name == highlighted_team.name):
                    row_text_color = (255,0,0)
                else:
                    row_text_color = (0,0,0)
                if match.played == True:
                    text = small_font.render(f"{match.home_team.name} - {match.away_team.name}: {match.home_goals} - {match.away_goals}", True, row_text_color)
                else:
                    text = small_font.render(f"{match.home_team.name} - {match.away_team.name}: ", True, row_text_color)
                text_rect = pygame.Rect(10, y,200, 20)
                schedule_surface.blit(text, text_rect)


    border_surface = pygame.Surface((schedule_surface.get_width() + 4, schedule_surface.get_height() + 4))
    border_surface.fill(BLACK)
    border_surface.blit(schedule_surface, (2, 2))

    return border_surface


def draw_schedule(game, screen, selected_league, highlighted_team):
    league = game.return_league_by_name(selected_league)
    num_teams = league.num_teams
    num_rounds = league.num_rounds

    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    navigation_rects = []

    rounds_per_page,num_pages = get_num_rounds(num_teams,num_rounds)

    #match_per_round = num_teams//2

    #rounds_per_page = 28//(match_per_round+2)
    #num_pages = -(-num_rounds//rounds_per_page)

    if game.start_page < 1:
        game.start_page = 1
    if game.start_page >= num_pages:
        game.start_page = num_pages - 1

    schedule_surface = draw_schedule_page(game, screen, selected_league, highlighted_team,game.start_page)
    screen.blit(schedule_surface,(150,110))
    schedule_surface = draw_schedule_page(game, screen, selected_league, highlighted_team,game.start_page +1)
    screen.blit(schedule_surface,(520,110))

    # Define button positions and text
    x1, x2, y = 40, 1000, 700
    font = pygame.font.Font(None, 20)
    prev_text = font.render("Previous Page", True, BLACK)
    prev_rect = prev_text.get_rect(midleft=(x1, y))
    navigation_rects.append(prev_rect)
    next_text = font.render("Next Page", True, BLACK)
    next_rect = next_text.get_rect(midright=(x2, y))
    navigation_rects.append(next_rect)

    # Blit buttons onto screen surface
    screen.blit(prev_text, prev_rect)
    screen.blit(next_text, next_rect)

    return navigation_rects




