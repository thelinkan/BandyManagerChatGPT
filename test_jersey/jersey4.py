import pygame

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((1000, 600))

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (200, 200, 200)
RED = (200,0,0)
GREEN = (0,200,0)


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

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(GRAY)
    jersey_colors = [(106,63,32),(106,63,32),(106,63,32),(0,0,0),(255,255,255)]
    jersey_surface = draw_jersey(jersey_colors,"5")
    screen.blit(jersey_surface,(50,150))
    jersey_colors = [(249,220,59),(249,220,59),(249,220,59),(0,0,0),(26,62,27)]
    jersey_surface = draw_jersey(jersey_colors,"17")
    screen.blit(jersey_surface,(550,150))
    # Keep the program running at a consistent speed
    pygame.time.delay(10)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
