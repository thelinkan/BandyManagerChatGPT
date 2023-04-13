import pygame

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((1000, 600))

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (200, 200, 200)
RED = (200,0,0)
GREEN = (0,200,0)


def draw_jersey():
    jersey_surface = pygame.Surface((250,250))
    jersey_surface.fill(WHITE)
    pygame.draw.polygon(jersey_surface,GRAY,[(3,65),(3,200),(50,200),(50,95),(60,3)])
    pygame.draw.polygon(jersey_surface,RED,[(50,245),(50,95),(60,3),(100,3),(115,15),(135,15),(150,3),(190,3),(200,95),(200,245)])
    pygame.draw.line(jersey_surface, BLACK, [3, 65], [3, 200], 5)
    pygame.draw.line(jersey_surface, BLACK, [3, 200], [50, 200], 5)
    pygame.draw.line(jersey_surface, BLACK, [50, 95], [50, 245], 5)
    pygame.draw.line(jersey_surface, BLACK, [50, 245], [200, 245], 5)
    pygame.draw.line(jersey_surface, BLACK, [200, 95], [200, 245], 5)
    pygame.draw.line(jersey_surface, BLACK, [200, 200], [247, 200], 5)
    pygame.draw.line(jersey_surface, BLACK, [247, 65], [247, 200], 5)
    pygame.draw.line(jersey_surface, BLACK, [3, 65], [60, 3], 5)
    pygame.draw.line(jersey_surface, BLACK, [190, 3], [247, 65], 5)
    pygame.draw.line(jersey_surface, BLACK, [60, 3], [100, 3], 5)
    pygame.draw.line(jersey_surface, BLACK, [150, 3], [190, 3], 5)
    pygame.draw.line(jersey_surface, BLACK, [100, 3], [115, 15], 5)
    pygame.draw.line(jersey_surface, BLACK, [135, 15], [150, 3], 5)
    pygame.draw.line(jersey_surface, BLACK, [115, 15], [135, 15], 5)
    
    
    

    return jersey_surface

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    jersey_surface = draw_jersey()
    screen.blit(jersey_surface,(150,150))
    # Keep the program running at a consistent speed
    pygame.time.delay(10)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
