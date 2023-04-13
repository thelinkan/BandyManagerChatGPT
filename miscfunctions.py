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
            schedule = [[(5,3),(4,2),(1,0)],[(3,2),(0,5),(1,4)],[(0,3),(2,1),(5,4)],[(0,3),(2,1),(5,4)]]
            random.shuffle(schedule)
    return schedule