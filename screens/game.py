import pygame
from button import Button
from inputbox import InputBox
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,WHITE,BLACK,GRAY,FONTSIZE_LARGE,FONTSIZE_MEDIUM,FONTSIZE_SMALL,FONTSIZE_VERY_SMALL
from constants import TABLE_HEADER_COLOR, TABLE_ROW_ODD_COLOR, TABLE_ROW_EVEN_COLOR
from guielements import font, medium_font, small_font, button_width, button_height, button_x, button_spacing
from guielements import new_game_button, load_game_button, credits_button, quit_button, new_game_ok_button, input_name, input_age, quit_game, choose_team_button
from guielements import home_button, inbox_button, newspaper_button, senior_squad_button, tactics_button, training_button, schedule_button, competition_button
from guielements import u19_squad_button,forward_time_button, save_game_button, quit_game_button
from miscfunctions import get_club_from_team, draw_calendar

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

x_offset = 150

def draw_playerlist(game,team):
    #team = game.teams[team_name]
    # Draw player table
    header_rect = pygame.Rect(10+x_offset, 100, 600, 30)

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
        row_rect = pygame.Rect(10+x_offset, 130 + i * row_height, 600, row_height)
        pygame.draw.rect(screen, row_color, row_rect)

        text = player_font.render(str(player[1]) + ") " + player[2] + " " + player[3], True, BLACK)
        text_rect = text.get_rect(left=row_rect.left + 10, centery=row_rect.centery)
        screen.blit(text, text_rect)

        text = player_font.render(str(player[4]), True, BLACK)
        text_rect = text.get_rect(centerx=row_rect.centerx, centery=row_rect.centery)
        screen.blit(text, text_rect)

        text = player_font.render(player[5], True, BLACK)
        text_rect = text.get_rect(right=row_rect.right - 10, centery=row_rect.centery)
        screen.blit(text, text_rect)

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

def draw_game_mainscreen(game, game_page):
    # Draw screen
    screen.fill(WHITE)
    title = font.render("Bandymanager - Main screen", True, BLACK)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 40))
    screen.blit(title, title_rect)

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
        draw_playerlist(game,manager_team)
    if (game_page == "player_list_u19"):
        draw_playerlist(game,manager_u19team)
    # Update display
    pygame.display.flip()
