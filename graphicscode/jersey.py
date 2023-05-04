import pygame

def draw_jersey(jersey_colors,jersey_decorations,jersey_number):
    jersey_surface = pygame.Surface((250,250), pygame.SRCALPHA)
    #jersey_surface.fill(WHITE)
    #Draw arms and chest
    pygame.draw.polygon(jersey_surface,jersey_colors[0],[(3,65),(3,200),(50,200),(50,95),(60,3)])
    pygame.draw.polygon(jersey_surface,jersey_colors[1],[(50,245),(50,95),(60,3),(100,3),(115,15),(135,15),(150,3),(190,3),(200,95),(200,245)])
    pygame.draw.polygon(jersey_surface,jersey_colors[2],[(190,3),(200,95),(200,200),(247,200),(247,65)])
    #Draw decorations
    for decoration in jersey_decorations:
        #print(decoration[0])
        if(decoration[0]==100):
            pygame.draw.line(jersey_surface, decoration[1], [100, 8], [115, 20], 15)
            pygame.draw.line(jersey_surface, decoration[1], [115, 20], [135, 20], 15)
            pygame.draw.line(jersey_surface, decoration[1], [135, 20], [150, 8], 15)
        if(decoration[0]==200):
            pygame.draw.rect(jersey_surface,decoration[1],(3,185,47,15))
        if(decoration[0]==300):
            pygame.draw.rect(jersey_surface,decoration[1],(200,185,47,15))
        if(decoration[0]==400):
            pygame.draw.rect(jersey_surface,decoration[1],(50,215,150,30))
        if(decoration[0]==401):
            pygame.draw.rect(jersey_surface,decoration[1],(50,215,150,30))
            pygame.draw.polygon(jersey_surface,decoration[1],[(60,215),(70,200),(75,200),(70,210),(75,215)])
    #Draw outline
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
    pygame.draw.line(jersey_surface, jersey_colors[3], [115, 15], [135, 15], 5)
    pygame.draw.line(jersey_surface, jersey_colors[3], [135, 15], [150, 3], 5)

    # Draw number
    number_font = pygame.font.Font(None, 160)
    number_text = number_font.render(jersey_number, True, jersey_colors[4])
    number_rect = number_text.get_rect(center=(125, 125))
    jersey_surface.blit(number_text, number_rect)

    return jersey_surface