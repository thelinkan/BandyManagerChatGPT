import datetime
import time
import pygame
import random
from club import Club
from team import Team
from constants import WHITE,BLACK,GRAY

def get_club_from_team(game, team):
    for club in game.clubs:
        for club_team in club.teams:
            if club_team == team:
                return club
    return None

def draw_calendar(year, month, day):

    # Define fonts
    small_font = pygame.font.Font(None, 14)
    medium_font = pygame.font.Font(None, 18)
    large_font = pygame.font.Font(None, 30)

    # Define calendar date
    cal_date = datetime.date(year, month, day)

    # Define weekday name and abbreviation lists
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_abbrs = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # Define month name list
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # Define calendar surface
    calendar_surface = pygame.Surface((90, 120))
    calendar_surface.fill(WHITE)

    # Draw year in top left corner
    year_text = small_font.render(str(year), True, BLACK)
    year_rect = year_text.get_rect(left=5, top=5)
    calendar_surface.blit(year_text, year_rect)

    # Draw weekday in larger font below year
    weekday_text = medium_font.render(weekday_names[cal_date.weekday()], True, BLACK)
    weekday_rect = weekday_text.get_rect(centerx=calendar_surface.get_width() // 2, top=5 + year_rect.height + 10)
    calendar_surface.blit(weekday_text, weekday_rect)

    # Draw day in largest font below weekday
    day_text = large_font.render(str(day), True, BLACK)
    day_rect = day_text.get_rect(centerx=calendar_surface.get_width() // 2, top=weekday_rect.bottom + 10)
    calendar_surface.blit(day_text, day_rect)

    # Draw month below day in same font as weekday
    month_text = medium_font.render(month_names[month - 1], True, BLACK)
    month_rect = month_text.get_rect(centerx=calendar_surface.get_width() // 2, top=day_rect.bottom + 10)
    calendar_surface.blit(month_text, month_rect)

    # Draw "Week X" in top right corner
    week_number = cal_date.isocalendar()[1]
    week_text = small_font.render("Week " + str(week_number), True, GRAY)
    week_rect = week_text.get_rect(right=calendar_surface.get_width() -5, top=5)
    calendar_surface.blit(week_text, week_rect)

    border_surface = pygame.Surface((calendar_surface.get_width() + 4, calendar_surface.get_height() + 4))
    border_surface.fill(BLACK)
    border_surface.blit(calendar_surface, (2, 2))

    return border_surface

def draw_jersey(jersey_colors,jersey_number):
    jersey_surface = pygame.Surface((250,250), pygame.SRCALPHA)
    #jersey_surface.fill(WHITE)
    pygame.draw.polygon(jersey_surface,jersey_colors[0],[(3,65),(3,200),(50,200),(50,95),(60,3)])
    pygame.draw.polygon(jersey_surface,jersey_colors[1],[(50,245),(50,95),(60,3),(100,3),(115,15),(135,15),(150,3),(190,3),(200,95),(200,245)])
    pygame.draw.polygon(jersey_surface,jersey_colors[2],[(190,3),(200,95),(200,200),(247,200),(247,65)])
    pygame.draw.line(jersey_surface, jersey_colors[3], [3, 65], [3, 200], 5)
    pygame.draw.line(jersey_surface, jersey_colors[3], [3, 200], [50, 200], 5)
    pygame.draw.line(jersey_surface, jersey_colors[3], [50, 95], [50, 245], 5)
    pygame.draw.line(jersey_surface, jersey_colors[3], [50, 245], [200, 245], 5)
    pygame.draw.line(jersey_surface, jersey_colors[3], [200, 95], [200, 245], 5)
    pygame.draw.line(jersey_surface, jersey_colors[3], [200, 200], [247, 200], 5)
    pygame.draw.line(jersey_surface, jersey_colors[3], [247, 65], [247, 200], 5)
    pygame.draw.line(jersey_surface, jersey_colors[3], [3, 65], [60, 3], 5)
    pygame.draw.line(jersey_surface, jersey_colors[3], [190, 3], [247, 65], 5)
    pygame.draw.line(jersey_surface, jersey_colors[3], [60, 3], [100, 3], 5)
    pygame.draw.line(jersey_surface, jersey_colors[3], [150, 3], [190, 3], 5)
    pygame.draw.line(jersey_surface, jersey_colors[3], [100, 3], [115, 15], 5)
    pygame.draw.line(jersey_surface, jersey_colors[3], [135, 15], [150, 3], 5)
    pygame.draw.line(jersey_surface, jersey_colors[3], [115, 15], [135, 15], 5)

    # Draw number
    number_font = pygame.font.Font(None, 160)
    number_text = number_font.render(jersey_number, True, jersey_colors[4])
    number_rect = number_text.get_rect(center=(125, 125))
    jersey_surface.blit(number_text, number_rect)

    return jersey_surface


def return_schedule(num_teams,num_rounds):
    if(num_teams == 4):
        schedule1 = [[(1,2),(3,0)],[(2,3),(0,1)],[(1,3),(2,0)]]
        schedule2 = [[(game[1], game[0]) for game in round] for round in schedule1]
        if(num_rounds == 3):
            random.shuffle(schedule1)
            schedule = schedule1
        if(num_rounds == 6):
            random.shuffle(schedule1)
            random.shuffle(schedule2)
            schedule = schedule1 + schedule2
        if(num_rounds == 9):
            schedule3 = schedule1
            random.shuffle(schedule1)
            random.shuffle(schedule2)
            random.shuffle(schedule3)
            schedule = schedule1 + schedule2 + schedule3
    if(num_teams == 6):
        schedule1 = [[(5,3),(4,2),(1,0)],[(3,2),(0,5),(1,4)],[(0,3),(2,1),(5,4)],[(3,1),(4,0),(5,2)],[(4,3),(1,5),(0,2)]]
        schedule2 = [[(game[1], game[0]) for game in round] for round in schedule1]
        if(num_rounds == 5):
            random.shuffle(schedule1)
            schedule = schedule1
        if(num_rounds == 10):
            random.shuffle(schedule1)
            random.shuffle(schedule2)
            schedule = schedule1 + schedule2
        if(num_rounds == 15):
            schedule3 = schedule1
            random.shuffle(schedule1)
            random.shuffle(schedule2)
            random.shuffle(schedule3)
            schedule = schedule1 + schedule2 + schedule3
    if(num_teams == 8):
        schedule1 = [[(7,5),(6,2),(0,1),(4,3)],[(5,2),(1,7),(3,6),(4,0)],[(1,5),(2,3),(7,4),(6,0)],[(5,3),(4,1),(0,2),(6,7)],[(4,5),(3,0),(1,6),(2,7)],[(5,0),(6,4),(7,3),(2,1)],[(6,5),(0,7),(4,2),(3,1)]]
        schedule2 = [[(game[1], game[0]) for game in round] for round in schedule1]
        if(num_rounds == 7):
            random.shuffle(schedule1)
            schedule = schedule1
        if(num_rounds == 14):
            random.shuffle(schedule1)
            random.shuffle(schedule2)
            schedule = schedule1 + schedule2
        if(num_rounds == 21):
            schedule3 = schedule1
            random.shuffle(schedule1)
            random.shuffle(schedule2)
            random.shuffle(schedule3)
            schedule = schedule1 + schedule2 + schedule3
    if(num_teams == 10):
        schedule1 = [[(3,8),(2,6),(0,5),(9,1),(7,4)],[(8,6),(5,3),(1,2),(4,0),(7,9)],[(5,8),(6,1),(3,4),(2,7),(0,9)],[(8,1),(4,5),(7,6),(9,3),(0,2)],[(4,8),(1,7),(5,9),(6,0),(3,2)],[(8,7),(9,4),(0,1),(2,5),(3,6)],[(9,8),(7,0),(4,2),(1,3),(5,6)],[(8,0),(2,9),(3,7),(6,4),(5,1)],[(2,8),(0,3),(9,6),(7,5),(4,1)]]
        schedule2 = [[(game[1], game[0]) for game in round] for round in schedule1]
        if(num_rounds == 9):
            random.shuffle(schedule1)
            schedule = schedule1
        if(num_rounds == 18):
            random.shuffle(schedule1)
            random.shuffle(schedule2)
            schedule = schedule1 + schedule2
    if(num_teams == 12):
        schedule1 = [[(11,4),(8,0),(7,5),(3,2),(9,6),(10,1)],[(4,0),(5,11),(2,8),(6,7),(1,3),(10,9)],[(5,4),(0,2),(11,6),(8,1),(7,10),(3,9)],[(4,2),(6,5),(1,0),(10,11),(9,8),(3,7)],[(6,4),(2,1),(5,10),(0,9),(11,3),(8,7)],[(4,1),(10,6),(9,2),(3,5),(7,0),(8,11)],[(10,4),(1,9),(6,3),(2,7),(5,8),(0,11)],[(4,9),(3,10),(7,1),(8,6),(11,2),(0,5)],[(3,4),(9,7),(10,8),(1,11),(6,0),(2,5)],[(4,7),(8,3),(11,9),(0,10),(5,1),(2,6)],[(8,4),(7,11),(3,0),(9,5),(10,2),(1,6)]]
        schedule2 = [[(game[1], game[0]) for game in round] for round in schedule1]
        if(num_rounds == 11):
            random.shuffle(schedule1)
            schedule = schedule1
        if(num_rounds == 22):
            random.shuffle(schedule1)
            random.shuffle(schedule2)
            schedule = schedule1 + schedule2
    if(num_teams == 14):
        schedule1 = [[(0,10),(7,12),(13,9),(11,2),(5,6),(3,4),(1,8)],[(10,12),(9,0),(2,7),(6,13),(4,11),(8,5),(1,3)],[(9,10),(12,2),(0,6),(7,4),(13,8),(11,1),(5,3)],[(10,2),(6,9),(4,12),(8,0),(1,7),(3,13),(5,11)],[(6,10),(2,4),(9,8),(12,1),(0,3),(7,5),(13,11)],[(10,4),(8,6),(1,2),(3,9),(5,12),(11,0),(13,7)],[(8,10),(4,1),(6,3),(2,5),(9,11),(12,13),(0,7)],[(10,1),(3,8),(5,4),(11,6),(13,2),(7,9),(0,12)],[(3,10),(1,5),(8,11),(4,13),(6,7),(2,0),(9,12)],[(10,5),(11,3),(13,1),(7,8),(0,4),(12,6),(9,2)],[(11,10),(5,13),(3,7),(1,0),(8,12),(4,9),(6,2)],[(10,13),(7,11),(0,5),(12,3),(9,1),(2,8),(6,4)],[(7,10),(13,0),(11,12),(5,9),(3,2),(1,6),(8,4)]]
        schedule2 = [[(game[1], game[0]) for game in round] for round in schedule1]
        if(num_rounds == 13):
            random.shuffle(schedule1)
            schedule = schedule1
        if(num_rounds == 26):
            random.shuffle(schedule1)
            random.shuffle(schedule2)
            schedule = schedule1 + schedule2
    if(num_teams == 16):
        schedulea = [[(1,2),(8,10),(9,16),(7,11),(3,15),(6,12),(4,14),(5,13)],[(10,9),(3,1),(11,8),(16,2),(12,7),(15,4),(13,6),(14,5)],[(2,3),(9,11),(1,4),(8,12),(10,16),(7,13),(5,15),(6,14)],[(11,10),(4,2),(12,9),(5,1),(13,8),(16,3),(14,7),(15,6)],[(3,4),(10,12),(2,5),(9,13),(1,6),(8,14),(11,16),(7,15)]]
        scheduleb = [[(12,11),(5,3),(13,10),(6,2),(14,9),(7,1),(15,8),(16,4)],[(4,5),(11,13),(3,6),(10,14),(2,7),(9,15),(1,8),(12,16)],[(13,12),(6,4),(14,11),(7,3),(15,10),(8,2),(16,5),(9,1)],[(5,6),(12,14),(4,7),(11,15),(3,8),(13,16),(2,9),(1,10)],[(14,13),(7,5),(15,12),(8,4),(16,6),(9,3),(11,1),(10,2)]]
        schedulec = [[(6,7),(13,15),(5,8),(14,16),(4,9),(1,12),(3,10),(2,11)],[(15,14),(8,6),(16,7),(9,5),(13,1),(10,4),(12,2),(11,3)],[(7,8),(15,16),(6,9),(1,14),(5,10),(2,13),(4,11),(3,12)],[(16,8),(9,7),(15,1),(10,6),(14,2),(11,5),(13,3),(12,4)],[(8,9),(1,16),(7,10),(2,15),(6,11),(3,14),(5,12),(4,13)]]
        schedule1 = schedulea + scheduleb + schedulec
        schedule2 = [[(game[1], game[0]) for game in round] for round in schedule1]
        if(num_rounds == 15):
            random.shuffle(schedule1)
            schedule = schedule1
        if(num_rounds == 30):
            random.shuffle(schedule1)
            random.shuffle(schedule2)
            schedule = schedule1 + schedule2



    return schedule

