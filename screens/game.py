import pygame
from button import Button
from inputbox import InputBox
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,WHITE,BLACK,GRAY,FONTSIZE_LARGE,FONTSIZE_MEDIUM,FONTSIZE_SMALL,FONTSIZE_VERY_SMALL
from constants import TABLE_HEADER_COLOR, TABLE_ROW_ODD_COLOR, TABLE_ROW_EVEN_COLOR
from guielements import font, medium_font, small_font,very_small_font ,very_small_bold_font , button_width, button_height, button_x, button_spacing
from guielements import new_game_button, load_game_button, credits_button, quit_button, new_game_ok_button, input_name, input_age, quit_game, choose_team_button
from guielements import home_button, inbox_button, media_button, senior_squad_button, lineup_button, tactics_button, training_button, schedule_button, competition_button
from guielements import u19_squad_button,forward_time_button, save_game_button, quit_game_button
from miscfunctions import get_club_from_team, draw_calendar, yesterday
from graphicscode.jersey import draw_jersey
from graphicscode.arrows import draw_arrow_left, draw_arrow_right, draw_arrow_up, draw_arrow_down

from screens.media import draw_media
from debug_functions import print_yesterdays_results

from screens.screensleague import draw_league, draw_schedule
from screens.screenstactics import draw_tactics, draw_lineup, draw_player

from game import Game
from league import League
from team import Team
from club import Club

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


def draw_next_match(game, team) -> pygame.Surface:
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


def draw_yesterday_results(game, team, list_offset: tuple[int,int]) -> tuple[pygame.Surface,list[pygame.Rect]]:
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
        if game.start_page<1:
            game.start_page = 1
        y = 10
        text = medium_font.render(f"Matches {day_yesterday} {month_names[month_yesterday-1]} {year_yesterday}", True, BLACK)
        y += 5
        last_league = ""
        text_rect = pygame.Rect(10, y,200, 20)
        yesterdays_result_surface.blit(text, text_rect)
        num_pages = 1
        page_size = 0
        page_surfaces = []
        page_surface = pygame.Surface((375,0))
        league_surface = pygame.Surface((375,0))
        size = 0
        for i,match in enumerate(matches_today):
            match_league = game.match_manager.get_league_of_match(match)
            if match_league.name != last_league:
                if(page_size + size >28):
                    num_pages += 1
                    page_size = 0
                    page_surfaces.append(page_surface)
                    page_surface = pygame.Surface((375,0))
            
                page_size += size
                page_height = page_surface.get_height()
                league_height = league_surface.get_height()
                new_page_surface =pygame.Surface((league_surface.get_width(),page_height+league_height))
                new_page_surface.blit(page_surface,(0,0))
                new_page_surface.blit(league_surface,(0,page_height))
                page_surface = new_page_surface
                size = 2
                league_surface = pygame.Surface((375,30))
                league_surface.fill(WHITE)
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
                rect.topleft = (0,0)
                league_surface.blit(combined_surface, rect)
                y+=12
            y += 20
            size += 1
            new_height = league_surface.get_height() + 20
            new_surface = pygame.Surface((league_surface.get_width(), new_height))
            new_surface.fill(WHITE)
            new_surface.blit(league_surface, (0, 0))
            if(match.home_team.name == team or match.away_team.name == team):
                row_text_color = (255,0,0)
            else:
                row_text_color = (0,0,0)
            text = small_font.render(f"{match.home_team.name} - {match.away_team.name}: {match.home_goals} - {match.away_goals}", True, row_text_color)
            text_rect = pygame.Rect(10, new_height-20,375, 20)
            new_surface.blit(text, text_rect)
            league_surface = new_surface

        if(page_size + size >28):
            num_pages += 1
            page_surfaces.append(page_surface)
            page_surface = pygame.Surface((375,0))
        page_size += size
        page_height = page_surface.get_height()
        league_height = league_surface.get_height()
        new_page_surface =pygame.Surface((league_surface.get_width(),page_height+league_height))
        new_page_surface.blit(page_surface,(0,0))
        new_page_surface.blit(league_surface,(0,page_height))
        page_surface = new_page_surface
        page_surfaces.append(page_surface)

        if game.start_page > num_pages:
            game.start_page = num_pages

        yesterdays_result_surface.blit(page_surfaces[game.start_page-1],(0,35))

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

def draw_home(game,team) -> list[pygame.Rect]:
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    list_offset = (470,110)
    arrow_rects = []
    next_match_surface = draw_next_match(game,team)
    screen.blit(next_match_surface,(150,110))
    if game.isMatchesPlayed == True:
        yesterdays_result_surface, arrow_rects = draw_yesterday_results(game, team, list_offset)
        screen.blit(yesterdays_result_surface,list_offset)

    return arrow_rects


def draw_game_mainscreen(game: Game) -> tuple[list, list, list]:
    # Draw screen
    screen.fill(WHITE)
    title = font.render("Bandymanager - Main screen", True, BLACK)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 40))
    screen.blit(title, title_rect)

    rectlist_1 = []
    rectlist_2 = []
    rectlist_3 = []

    manager_name = game.manager.return_name()
    manager_team_name = game.manager.return_team()
    manager_team = game.teams[manager_team_name]
    manager_club = get_club_from_team(game, manager_team)
    if(manager_club == None):
        return rectlist_1, rectlist_2, rectlist_3
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
    media_button.draw(screen)
    senior_squad_button.draw(screen)
    lineup_button.draw(screen)
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

    if(game.inspected_league is not None):
        inspected_league = game.inspected_league
    else:
        inspected_league = leagues[0].name

    #print(f"League 0: {leagues[0].name}")
    #print(f"Inspected League - Game: {game.inspected_league}")
    #print(f"Inspected League: {inspected_league}")

    if (game.game_page == "home"):
        rectlist_1 = draw_home(game,manager_team_name)
    if (game.game_page == "player_list"):
        if game.inspected_team is not None:
            team_viewed = game.inspected_team
        else:
            team_viewed = manager_team
        rectlist_1 = draw_squad(game,team_viewed)
    if (game.game_page == "lineup"):
        rectlist_1, rectlist_2 = draw_lineup(game,manager_team)
    if (game.game_page == "tactics"):
        rectlist_1, rectlist_2, rectlist_3 = draw_tactics(game,manager_team)
    if (game.game_page == "media"):
        rectlist_1 = draw_media(game)
    if (game.game_page == "schedule"):
        print(f"Inspected League again: {inspected_league}")
        rectlist_1, rectlist_2 = draw_schedule(game,screen, inspected_league, manager_team)
    if (game.game_page == "competition"):
        rectlist_1, rectlist_2 = draw_league(game,screen, manager_team)
        #league_table_surface, rectlist_1 = draw_league_table(game, manager_team)
        #screen.blit(league_table_surface,(140,110))
    if (game.game_page == "player_list_u19"):
        rectlist_1 = draw_squad(game,manager_u19team)
    # Update display
    pygame.display.flip()

    return rectlist_1, rectlist_2, rectlist_3
