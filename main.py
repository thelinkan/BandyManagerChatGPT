import pygame
import json
import pickle
#import classes for GUI
from inputbox import InputBox
from button import Button
pygame.init()
from game import Game

from constants import SCREEN_WIDTH,SCREEN_HEIGHT,WHITE,BLACK,GRAY
from screens import screen,draw_start_menu, draw_credits, draw_newgame_menu, draw_newgame2_menu
from guielements import font,medium_font, small_font, button_width, button_height, button_x, button_spacing
from guielements import new_game_button, load_game_button, credits_button, quit_button, new_game_ok_button, input_name, input_age, quit_game

game_state = "start_menu"

# Set the title of the window
pygame.display.set_caption("Bandymanager")

#Define swedish flag
swedish_flag = pygame.image.load("flags/sweden.png").convert_alpha()
swedish_flag_small = pygame.transform.scale(swedish_flag, (40, 40))

selected_country_index=-1

# Define game loop
running = True
while running:
    clock = pygame.time.Clock()
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "show_credits":
            	game_state = "start_menu"
            elif event.button == 1 and game_state == "start_menu":
                if new_game_button.rect.collidepoint(event.pos):
                    game_state="new_game"
                    print("New game click");
                    game = Game(2023,8,1)
                if load_game_button.rect.collidepoint(event.pos):
                    game_state="load_game"
                    game = Game(0,0,0)
                    game.load_game('')
                    print("Load game click");
                if credits_button.rect.collidepoint(event.pos):
                    game_state="show_credits"
                    print("Credits click");
                if quit_button.rect.collidepoint(event.pos):
                    quit_button.do_action()
            elif event.button == 1 and game_state == "new_game":
                if new_game_ok_button.rect.collidepoint(event.pos):
                    manager_name=input_name.return_text()
                    manager_age=int(input_age.return_text())
                    game.new_game(manager_name, manager_age)
                    game.save_game('c:\temp')
                    game_state="new_game_2"
            elif event.button == 1 and game_state == "new_game_2":
                for i, rect in enumerate(country_rects):
                    if rect.collidepoint(event.pos):
                        selected_country_index = i
                        break
                
        if game_state =="new_game":
            input_name.handle_event(event)
            input_age.handle_event(event)

    if game_state == "start_menu":
        draw_start_menu()
    if game_state == "show_credits":
        draw_credits(swedish_flag_small)
    if game_state == "new_game":
        draw_newgame_menu()
    if game_state == "new_game_2":
        country_rects=draw_newgame2_menu(game,selected_country_index)
    clock.tick(30)

pygame.quit()
quit()
