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
        if(num_rounds == 3):
            schedule = [[(1,2),(3,0)],[(2,3),(0,1)],[(1,3),(2,0)]]
            random.shuffle(schedule)
        if(num_rounds == 6):
            schedule1 = [[(1,2),(3,0)],[(2,3),(0,1)],[(1,3),(2,0)]]
            schedule2 = [[(2,1),(0,3)],[(3,2),(1,0)],[(3,1),(0,2)]]
            random.shuffle(schedule1)
            random.shuffle(schedule2)
            schedule = schedule1 + schedule2
    if(num_teams == 6):
        if(num_rounds == 5):
            schedule = [[(5,3),(4,2),(1,0)],[(3,2),(0,5),(1,4)],[(0,3),(2,1),(5,4)],[(3,1),(4,0),(5,2)],[(4,3),(1,5),(0,2)]]
            random.shuffle(schedule)
    if(num_teams == 8):
        if(num_rounds == 7):
            schedule = [[(7,5),(6,2),(0,1),(4,3)],[(5,2),(1,7),(3,6),(4,0)],[(1,5),(2,3),(7,4),(6,0)],[(5,3),(4,1),(0,2),(6,7)],[(4,5),(3,0),(1,6),(2,7)],[(5,0),(6,4),(7,3),(2,1)],[(6,5),(0,7),(4,2),(3,1)]]
            random.shuffle(schedule)
    if(num_teams == 10):
        if(num_rounds == 9):
            schedule = [[(3,8),(2,6),(0,5),(9,1),(7,4)],[(8,6),(5,3),(1,2),(4,0),(7,9)],[(5,8),(6,1),(3,4),(2,7),(0,9)],[(8,1),(4,5),(7,6),(9,3),(0,2)],[(4,8),(1,7),(5,9),(6,0),(3,2)],[(8,7),(9,4),(0,1),(2,5),(3,6)],[(9,8),(7,0),(4,2),(1,3),(5,6)],[(8,0),(2,9),(3,7),(6,4),(5,1)],[(2,8),(0,3),(9,6),(7,5),(4,1)]]
            random.shuffle(schedule)

    return schedule

