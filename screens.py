import pygame
from button import Button
from inputbox import InputBox
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,WHITE,BLACK,GRAY,FONTSIZE_LARGE,FONTSIZE_MEDIUM,FONTSIZE_SMALL
from guielements import font, medium_font, small_font, button_width, button_height, button_x, button_spacing, new_game_button, load_game_button, credits_button, quit_button, new_game_ok_button, input_name, input_age, quit_game

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    
def draw_start_menu():
    # Draw screen
    #print(game_state)
    screen.fill(WHITE)
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
    
def draw_newgame2_menu(game,selected_country_index):
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
        text_choose2 = medium_font.render("Choose league",False, BLACK)
        screen.blit(text_choose2, (340, 155))
    pygame.display.flip()
    return country_rects