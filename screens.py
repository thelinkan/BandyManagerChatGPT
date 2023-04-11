import pygame
from button import Button
from inputbox import InputBox
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,WHITE,BLACK,GRAY,FONTSIZE_LARGE,FONTSIZE_MEDIUM,FONTSIZE_SMALL,FONTSIZE_VERY_SMALL
from constants import TABLE_HEADER_COLOR, TABLE_ROW_ODD_COLOR, TABLE_ROW_EVEN_COLOR
from guielements import font, medium_font, small_font, button_width, button_height, button_x, button_spacing
from guielements import new_game_button, load_game_button, credits_button, quit_button, new_game_ok_button, input_name, input_age, quit_game, choose_team_button
from guielements import senior_team_button
from miscfunctions import get_club_from_team

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

def draw_credits(flag):
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
    screen.blit(flag, (375, 242))
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

def draw_newgame2_menu(game,selected_country_index,selected_team_index):
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
    countries = game.return_countrylist()
    y = 190
    country_rects = []
    country_num=0
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
        #text_test = medium_font.render(str(selected_country_index)+" "+countries[selected_country_index].return_name(),False, BLACK)
        #screen.blit(text_test, (340, 185))

    if(selected_country_index>=0):
        text_choose2 = medium_font.render("Choose team",False, BLACK)
        screen.blit(text_choose2, (640, 155))
        teams = game.return_teamlist(selected_country, 'Men')
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
        choose_team_button.draw(screen)
        #print(selected_team)
        pass
    pygame.display.flip()
    return country_rects, team_rects, selected_team

def draw_game_mainscreen(game):
    # Draw screen
    screen.fill(WHITE)
    title = font.render("Bandymanager - Main screen", True, BLACK)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 40))
    screen.blit(title, title_rect)
    x_offset = 150

    manager_name = game.manager.return_name()
    manager_team_name = game.manager.return_team()
    manager_team = game.teams[manager_team_name]
    manager_club = get_club_from_team(game, manager_team)
    manager_club_name = manager_club.name

    toprow_font = pygame.font.Font(None, FONTSIZE_SMALL)
    text = toprow_font.render(f"Manager: {manager_name}    Club: {manager_club_name}", True, BLACK)
    text_rect = (10+x_offset,80,600,30)
    #text_rect = text.get_rect(left=header_rect.left + 10, centery=header_rect.centery)
    screen.blit(text, text_rect)

    senior_team_button.draw(screen)


    # Draw player table
    header_rect = pygame.Rect(10+x_offset, 100, 600, 30)
    team_players = manager_team.get_players()

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
    for i, player in enumerate(manager_team.get_players()):
        if i % 2 == 0:
            row_color = TABLE_ROW_EVEN_COLOR
        else:
            row_color = TABLE_ROW_ODD_COLOR
        row_rect = pygame.Rect(10+x_offset, 130 + i * row_height, 600, row_height)
        pygame.draw.rect(screen, row_color, row_rect)

        text = player_font.render(player[1] + " " + player[2], True, BLACK)
        text_rect = text.get_rect(left=row_rect.left + 10, centery=row_rect.centery)
        screen.blit(text, text_rect)

        text = player_font.render(str(player[3]), True, BLACK)
        text_rect = text.get_rect(centerx=row_rect.centerx, centery=row_rect.centery)
        screen.blit(text, text_rect)

        text = player_font.render(player[4], True, BLACK)
        text_rect = text.get_rect(right=row_rect.right - 10, centery=row_rect.centery)
        screen.blit(text, text_rect)

    # Update display
    pygame.display.flip()

