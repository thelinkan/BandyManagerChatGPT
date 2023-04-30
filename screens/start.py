import pygame
from button import Button
from inputbox import InputBox
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,WHITE,BLACK,GRAY,FONTSIZE_LARGE,FONTSIZE_MEDIUM,FONTSIZE_SMALL,FONTSIZE_VERY_SMALL
from constants import TABLE_HEADER_COLOR, TABLE_ROW_ODD_COLOR, TABLE_ROW_EVEN_COLOR
from guielements import font, medium_font, small_font, button_width, button_height, button_x, button_spacing
from guielements import new_game_button, load_game_button, credits_button, quit_button, new_game_ok_button, input_name, input_age, quit_game, choose_team_button
from miscfunctions import get_club_from_team, draw_jersey

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def draw_start_menu():
    # Draw screen
    bg = pygame.image.load("images/background1.png")
    bg_rect = bg.get_rect()
    bg_rect.left=0
    bg_rect.top=0
    screen.fill(WHITE)
    screen.blit(bg,bg_rect)
    title = font.render("Bandymanager", True, BLACK)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(title, title_rect)
    new_game_button.draw(screen)
    load_game_button.draw(screen)
    credits_button.draw(screen)
    quit_button.draw(screen)
    pygame.display.flip()

def draw_credits():
    #print(game_state)
    screen.fill(WHITE)
    title = font.render("Bandymanager - Credits", True, BLACK)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(title, title_rect)
    credits1 = medium_font.render("Programmer: Torbjorn Lindquist", False, BLACK)
    screen.blit(credits1, (40, 250))
    credits2 = medium_font.render("AI help: Chat-GPT", False, BLACK)
    screen.blit(credits2, (40, 285))
    credits3 = medium_font.render("Flags: https://icons8.com/icon/set/flags/stickers", False, BLACK)
    screen.blit(credits3, (40, 320))
    pygame.display.flip()

def draw_newgame_menu():
    # Draw screen
    screen.fill(WHITE)
    title = font.render("Bandymanager - New game", True, BLACK)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(title, title_rect)
    text_name = medium_font.render("Name",False, BLACK)
    screen.blit(text_name, (40, 200))
    input_name.draw(screen)
    text_age = medium_font.render("Age",False, BLACK)
    screen.blit(text_age, (40, 300))
    input_age.draw(screen)
    new_game_ok_button.draw(screen)
    pygame.display.flip()

def draw_newgame2_menu(game,selected_country_index,selected_league_index,selected_team_index):
    mouse_pos = pygame.mouse.get_pos()
    # Draw screen
    screen.fill(WHITE)
    title = font.render("Bandymanager - New game", True, BLACK)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(title, title_rect)
    text_name = medium_font.render("Welcome "+game.return_managername(),False, BLACK)
    screen.blit(text_name, (40, 120))
    text_choose = medium_font.render("Choose country",False, BLACK)
    screen.blit(text_choose, (40, 155))
    countries = game.return_countries_with_leagues()
    y = 190
    country_rects = []
    country_num=0
    league_rects = []
    team_rects = []
    selected_team = ""
    for country in countries:
        flag = game.return_countryflag(country.return_name())
        text = small_font.render(country.return_name(), True, BLACK)
        combined_surf = pygame.Surface((130, max(flag.get_height(), text.get_height())))
        if country_num == selected_country_index:
            combined_surf.fill((200,200,200))
        else:
            combined_surf.fill(WHITE)
        combined_surf.blit(flag, (0, 0))
        combined_surf.blit(text, (flag.get_width() + 5, 2))
        rect = combined_surf.get_rect()
        rect.topleft = (70, y)
        if rect.collidepoint(mouse_pos):
            combined_surf.fill(GRAY)
            combined_surf.blit(flag, (0, 0))
            combined_surf.blit(text, (flag.get_width() + 5, 2))
        screen.blit(combined_surf, rect)
        country_rects.append(rect)
        y += max(flag.get_height(), text.get_height()) + 10
        country_num+=1
    if(selected_country_index>=0):
        selected_country = countries[selected_country_index].return_name()
        text_choose2 = medium_font.render("Choose league",False, BLACK)
        screen.blit(text_choose2, (340, 155))
        leagues = game.return_leagues_in_country(selected_country)
        y = 190
        league_num=0
        for league in leagues:
            if league_num == selected_league_index:
                league_name = league.name
            text = small_font.render(league.name,False, BLACK)
            combined_surf = pygame.Surface((130,text.get_height()))
            if league_num == selected_league_index:
                combined_surf.fill((200,200,200))
            else:
                combined_surf.fill(WHITE)
            combined_surf.blit(text, (0, 0))
            rect = combined_surf.get_rect()
            rect.topleft = (340, y)
            if rect.collidepoint(mouse_pos):
                combined_surf.fill(GRAY)
                combined_surf.blit(text, (0, 0))
            screen.blit(combined_surf, rect)
            league_rects.append(rect)
            y += text.get_height() + 10
            league_num += 1

        #text_test = medium_font.render(str(selected_country_index)+" "+countries[selected_country_index].return_name(),False, BLACK)
        #screen.blit(text_test, (340, 185))

    if(selected_league_index>=0):
        text_choose2 = medium_font.render("Choose team",False, BLACK)
        screen.blit(text_choose2, (640, 155))
        teams = game.return_teams_for_league(league_name)
        #teams = game.return_teamlist(selected_country, 'Men')
        y = 190
        team_num=0
        for team in teams:
            text = small_font.render(team.return_name(),False, BLACK)
            combined_surf = pygame.Surface((130,text.get_height()))
            if team_num == selected_team_index:
                combined_surf.fill((200,200,200))
            else:
                combined_surf.fill(WHITE)
            combined_surf.blit(text, (0, 0))
            rect = combined_surf.get_rect()
            rect.topleft = (640, y)
            if rect.collidepoint(mouse_pos):
                combined_surf.fill(GRAY)
                combined_surf.blit(text, (0, 0))
            screen.blit(combined_surf, rect)
            team_rects.append(rect)
            y += text.get_height() + 10
            team_num += 1
            #print("Test")
            #team_name = print(team.return_name())
            pass

    if(selected_team_index>=0):
        selected_team = teams[selected_team_index].return_name()
        text_team_name = medium_font.render(selected_team,False, BLACK)
        screen.blit(text_team_name, (940, 155))
        jersey_colors = teams[selected_team_index].return_jersey_colors()
        jersey = draw_jersey(jersey_colors,"17")
        screen.blit(jersey,(940,400))
        choose_team_button.draw(screen)
        #print(selected_team)
        pass
    pygame.display.flip()
    return country_rects, league_rects, team_rects, selected_team

