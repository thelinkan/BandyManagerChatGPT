import datetime
import time
import pygame
import random
from club import Club
from team import Team
from constants import WHITE,BLACK,GRAY

from graphicscode.jersey import draw_jersey


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

    print(f"teams: {num_teams}, || numrounds_ {num_rounds}")
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
        schedulea = [[(1,2),(8,10),(9,0),(7,11),(3,15),(6,12),(4,14),(5,13)],[(10,9),(3,1),(11,8),(0,2),(12,7),(15,4),(13,6),(14,5)],[(2,3),(9,11),(1,4),(8,12),(10,0),(7,13),(5,15),(6,14)],[(11,10),(4,2),(12,9),(5,1),(13,8),(0,3),(14,7),(15,6)],[(3,4),(10,12),(2,5),(9,13),(1,6),(8,14),(11,0),(7,15)]]
        scheduleb = [[(12,11),(5,3),(13,10),(6,2),(14,9),(7,1),(15,8),(0,4)],[(4,5),(11,13),(3,6),(10,14),(2,7),(9,15),(1,8),(12,0)],[(13,12),(6,4),(14,11),(7,3),(15,10),(8,2),(0,5),(9,1)],[(5,6),(12,14),(4,7),(11,15),(3,8),(13,0),(2,9),(1,10)],[(14,13),(7,5),(15,12),(8,4),(0,6),(9,3),(11,1),(10,2)]]
        schedulec = [[(6,7),(13,15),(5,8),(14,0),(4,9),(1,12),(3,10),(2,11)],[(15,14),(8,6),(0,7),(9,5),(13,1),(10,4),(12,2),(11,3)],[(7,8),(15,0),(6,9),(1,14),(5,10),(2,13),(4,11),(3,12)],[(0,8),(9,7),(15,1),(10,6),(14,2),(11,5),(13,3),(12,4)],[(8,9),(1,0),(7,10),(2,15),(6,11),(3,14),(5,12),(4,13)]]
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

def adddays(year, month, day, days_to_add):
    day += days_to_add
    if month in [4, 6, 9, 11]:
        month_days = 30
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            month_days = 29
        else:
            month_days = 28
    else:
        month_days = 31

    if day > month_days:
        day = day - month_days
        month += 1

    if month > 12:
        month = 1
        year += 1
    return year, month, day

def yesterday(year, month, day):
    if day == 1:
        month -= 1
        if month == 0:
            year -= 1
            month = 12
        if month in [4, 6, 9, 11]:
            day = 30
        elif month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                day = 29
            else:
                day = 28
        else:
            day = 31
    else:
        day -= 1
    return year, month, day


def get_weekdays(start_date, end_date, weekday):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_idx = weekdays.index(weekday)

    start_date = datetime.date(*start_date)
    end_date = datetime.date(*end_date)

    days = (end_date - start_date).days + 1
    weekdays_list = [start_date + datetime.timedelta(days=x) for x in range(days) if (start_date + datetime.timedelta(days=x)).weekday() == weekday_idx]

    return [(d.year, d.month, d.day) for d in weekdays_list]


def get_k_integers(n, k):
    if k > n:
        raise ValueError("k cannot be greater than n")
    elif k == n:
        return list(range(n))
    elif k > n/2:
        excluded = set(get_k_integers(n - k, n - k))
        result = set()
        while len(result) < k:
            num = random.randint(0, n-1)
            if num not in excluded:
                result.add(num)
        return list(result)
    else:
        result = set()
        while len(result) < k:
            num = random.randint(0, n-1)
            result.add(num)
        return list(result)

def get_num_rounds(num_teams,num_rounds):
    match_per_round = num_teams//2

    rounds_per_page = 28//(match_per_round+2)
    num_pages = -(-num_rounds//rounds_per_page)

    return rounds_per_page,num_pages    