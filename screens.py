import pygame
from button import Button
from inputbox import InputBox
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,WHITE,BLACK,GRAY
from guielements import font, small_font, button_width, button_height, button_x, button_spacing, new_game_button, load_game_button, credits_button, quit_button, new_game_ok_button, input_name, input_age, quit_game

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
    credits1 = small_font.render("Programmer: Torbjorn Lindquist", False, BLACK)    
    screen.blit(credits1, (40, 250))
    credits2 = small_font.render("AI help: Chat-GPT", False, BLACK)    
    screen.blit(credits2, (40, 285))
    screen.blit(flag, (375, 242))
    pygame.display.flip()

def draw_newgame_menu():
    # Draw screen
    screen.fill(WHITE)
    title = font.render("Bandymanager - New game", True, BLACK)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(title, title_rect)
    text_name = small_font.render("Name",False, BLACK)
    screen.blit(text_name, (40, 200))
    input_name.draw(screen)
    text_age = small_font.render("Age",False, BLACK)
    screen.blit(text_age, (40, 300))
    input_age.draw(screen)
    new_game_ok_button.draw(screen)    
    pygame.display.flip()