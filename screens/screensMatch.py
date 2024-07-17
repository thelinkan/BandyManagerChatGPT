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
    is_playoff = match_to_view.league.is_playoff
    engine = MatchEngine(match_to_view)
    controller = MatchController(match_to_view, engine)

    match_to_view.home_goals = 0
    match_to_view.away_goals = 0

    match_state = "Pre game"
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
                #sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and (match_state == "Pre game"):
                    if header_button_rect.collidepoint(event.pos):
                        match_state = "1st half"
                if event.button == 1 and (match_state == "Half time"):
                    if header_button_rect.collidepoint(event.pos):
                        match_state = "2nd half"
                if event.button == 1 and (match_state == "End of game"):
                    if header_button_rect.collidepoint(event.pos):
                        match_to_view.is_over = True

        screen.fill(WHITE)

        match_header_surface,header_button_rect = view_match_header(game,match_to_view,engine,match_state)
        screen.blit(match_header_surface,(0,0))

        match_event_surface = draw_events(match_to_view)
        screen.blit(match_event_surface,(100,100))

        if(match_state == "1st half" or match_state == "2nd half"):
            engine.tick()
        pygame.display.flip()
        time.sleep(0.01)
        if match_state == "1st half" and engine.game_time>60*45:
            engine.game_time = 60*45
            match_state = "Half time"
            event = {
                "type": "Half time",
                "time": "45:00"
            }
            match_to_view.events.append(event)
        if engine.game_time>60*90:
            engine.game_time = 60*90
            if(match_to_view.home_goals == match_to_view.away_goals and is_playoff):
                match_to_view.home_goals += 1
            match_state = "End of game"
            match_to_view.played = True
            event = {
                "type": "Match ended",
                "time": "90:00"
            }
            match_to_view.events.append(event)
            #print(match_to_view.events)
            #for event in match_to_view.events:
            #    print(f"Event: \n {event}")
            for league in game.leagues:
                league.calculate_table()

                print(f"View: {league.name} - is_completed: {league.is_completed()}")
                if(league.playoff_for_league is not None and league.is_completed()):
                    if(not league.playoff_for_league.is_started):
                        print(f"Time for playoff - {league.playoff_for_league.name} - is_started: {league.playoff_for_league.is_started}")
                        #league.print_table()
                        league.playoff_for_league.create_quarter_finals_schedule(league.get_playoff_teams())
                        for team in league.get_playoff_teams():
                            print(team.name)


    #print("Match ended")
    #game.match_manager.play_viewed_match(match_to_view)
    #print("view match")

def view_match_header(game,match_to_view,engine,match_state):
    match_header_surface = pygame.Surface((SCREEN_WIDTH,80), pygame.SRCALPHA)
    match_header_surface.fill((220,220,220))

    text = medium_font.render(f"{engine.get_current_time()}",True,BLACK)
    text_rect = pygame.Rect(10, 15, 50, 20)
    match_header_surface.blit(text,text_rect)
    text = very_small_font.render(f"{match_state}",True,BLACK)
    text_rect = pygame.Rect(10, 55, 50, 20)
    match_header_surface.blit(text,text_rect)

    text = small_font.render(f"{match_to_view.home_team.name}",True,BLACK)
    text_rect = pygame.Rect(75, 10, 150, 20)
    match_header_surface.blit(text,text_rect)
    text = small_font.render(f"{match_to_view.home_goals}",True,BLACK)
    text_rect = pygame.Rect(225, 10, 80, 20)
    match_header_surface.blit(text,text_rect)
    text = small_font.render(f"{match_to_view.away_team.name}",True,BLACK)
    text_rect = pygame.Rect(75, 40, 150, 20)
    match_header_surface.blit(text,text_rect)
    text = small_font.render(f"{match_to_view.away_goals}",True,BLACK)
    text_rect = pygame.Rect(225, 40, 80, 20)
    match_header_surface.blit(text,text_rect)

    header_button_surface = pygame.Surface((150,60), pygame.SRCALPHA)
    header_button_surface.fill((90,90,90))
    if match_state == "Pre game" or match_state == "Half time" or match_state == "End of game":
        header_text = medium_font.render(f"Continue",True,WHITE)
    else:
        header_text = medium_font.render(f"",True,WHITE)

    header_button_rect = pygame.Rect(SCREEN_WIDTH-150, 10, 150, 60)
    header_button_surface.blit(header_text,(10,15))

    match_header_surface.blit(header_button_surface,header_button_rect)

    return match_header_surface,header_button_rect

def draw_events(match_to_view):
    sorted_events = sorted(match_to_view.events, key = lambda x:x['time'] , reverse = True)

    event_surface = pygame.Surface((550,600), pygame.SRCALPHA)
    event_surface.fill(WHITE)
    y=10
    row_height = 20
    event_font = pygame.font.Font(None, FONTSIZE_VERY_SMALL)
    for i, event in enumerate(sorted_events):
        if i % 2 == 0:
            row_color = TABLE_ROW_EVEN_COLOR
        else:
            row_color = TABLE_ROW_ODD_COLOR
        row_rect = pygame.Rect(10,10+i*row_height,500,row_height)
        pygame.draw.rect(event_surface, row_color, row_rect)
        event_time = event["time"]
        event_type = event["type"]
        if event_type == "goal":
            goal_scorer = event["goal_scorer"]
            assisting_player = event["assisting_player"]
            goal_team = event["team"]
            if(assisting_player is not None):
                text = event_font.render(f"{event_time}: {goal_scorer.first_name} {goal_scorer.last_name} score for {goal_team}, assisted by {assisting_player.first_name} {assisting_player.last_name} .", True, BLACK)
            else:
                text = event_font.render(f"{event_time}: {goal_scorer.first_name} {goal_scorer.last_name} score for {goal_team}.", True, BLACK)
            text_rect = text.get_rect(left=row_rect.left + 10, centery = row_rect.centery)
        else:
            text = event_font.render(f"{event_time}: {event_type}.", True, BLACK)
            text_rect = text.get_rect(left=row_rect.left + 10, centery = row_rect.centery)
        event_surface.blit(text,text_rect)    
        #print(f"{event_time}: {event_type} {goal_scorer.first_name}")
    return event_surface