import datetime
import time
import pygame

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

def draw_calendar(year, month, day, x_pos, y_pos):
    
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

    return calendar_surface




pygame.init()

# Set up the Pygame display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Calendar Example")
screen.fill(WHITE)

# Draw the calendar
draw_calendar(2023, 4, 1, 50, 50)

# Update the Pygame display
pygame.display.flip()

# Wait for the user to close the window
day = 1
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the calendar
    calendar_surface = draw_calendar(2023, 4, day, 50, 50)
    border_surface = pygame.Surface((calendar_surface.get_width() + 4, calendar_surface.get_height() + 4))
    border_surface.fill((0, 0, 0))
    border_surface.blit(calendar_surface, (2, 2))
    screen.blit(border_surface, (150,150))
    #screen.blit(calendar_surface, (0, 0))

    # Update the display
    pygame.display.flip()

    time.sleep(3)
    day +=1
    


    