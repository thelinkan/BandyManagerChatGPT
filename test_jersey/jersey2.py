import pygame

# Set up Pygame
pygame.init()
clock = pygame.time.Clock()

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up window
WINDOW_SIZE = (250, 250)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sports Jersey")

# Set up jersey colors
JERSEY_COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 255, 255) # White
]

# Set up jersey number
JERSEY_NUMBER = "42"

# Create surface for jersey
jersey_surface = pygame.Surface(WINDOW_SIZE)

# Draw jersey
jersey_points = [
    (50, 50),
    (200, 50),
    (200, 200),
    (50, 200)
]
pygame.draw.polygon(jersey_surface, JERSEY_COLORS[0], jersey_points)

# Draw sleeves
sleeve_points = [
    (50, 75),
    (50, 175),
    (125, 175),
    (125, 75)
]
pygame.draw.polygon(jersey_surface, JERSEY_COLORS[1], sleeve_points)

# Draw collar
collar_points = [
    (125, 50),
    (150, 50),
    (150, 35),
    (175, 35),
    (175, 50),
    (200, 50),
    (200, 75),
    (175, 75),
    (175, 60),
    (150, 60),
    (150, 75),
    (125, 75)
]
pygame.draw.polygon(jersey_surface, BLACK, collar_points)
pygame.draw.polygon(jersey_surface, JERSEY_COLORS[0], collar_points[:-1], 1)

# Draw number
number_font = pygame.font.Font(None, 60)
number_text = number_font.render(JERSEY_NUMBER, True, BLACK)
number_rect = number_text.get_rect(center=(125, 125))
jersey_surface.blit(number_text, number_rect)

# Blit jersey surface to screen
screen.blit(jersey_surface, (0, 0))

# Event handling loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update screen
    pygame.display.update()

    # Tick clock
    clock.tick(60)

# Quit Pygame
pygame.quit()
