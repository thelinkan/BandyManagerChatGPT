import pygame
import time
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,WHITE,BLACK,GRAY,FONTSIZE_LARGE,FONTSIZE_MEDIUM,FONTSIZE_SMALL,FONTSIZE_VERY_SMALL
from constants import TABLE_HEADER_COLOR, TABLE_ROW_ODD_COLOR, TABLE_ROW_EVEN_COLOR
from guielements import font, medium_font, small_font,very_small_font ,very_small_bold_font , button_width, button_height, button_x, button_spacing
from matchcode.matchengine import MatchEngine
from matchcode.matchcontroller import MatchController

import pdb

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def draw_view_match(game,match_to_view):

    engine = MatchEngine(match_to_view)
    controller = MatchController(match_to_view, engine)

    #pdb.set_trace()

    while not match_to_view.is_over:
        clock = pygame.time.Clock()
        #print("test")
        # Listen for user input
        #user_input = get_user_input()
        # Draw screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        title = font.render("Bandymanager - Play match", True, BLACK)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 40))
        screen.blit(title, title_rect)
        engine.tick()

        text = font.render(f"Tid: {engine.get_current_time()}",True,BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(text, text_rect)

        #print(engine.get_current_time())

        text = font.render(f"{match_to_view.home_team.name} - {match_to_view.away_team.name}",True,BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 160))
        screen.blit(text, text_rect)

        text = font.render(f"{match_to_view.home_goals} - {match_to_view.away_goals}",True,BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 300))
        screen.blit(text, text_rect)


        pygame.display.flip()
        time.sleep(0.1)
        if engine.game_time>60*90:
            match_to_view.is_over = True
    #print("Match ended")
    #game.match_manager.play_viewed_match(match_to_view)
    #print("view match")