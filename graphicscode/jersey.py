import pygame

def draw_jersey(jersey_colors,jersey_decorations,jersey_number, logo, is_front):
    jersey_surface = pygame.Surface((250,250), pygame.SRCALPHA)
    #jersey_surface.fill(WHITE)
    #Draw arms and chest
    pygame.draw.polygon(jersey_surface,jersey_colors[0],[(3,65),(3,200),(50,200),(50,95),(60,3)])
    pygame.draw.polygon(jersey_surface,jersey_colors[1],[(50,245),(50,95),(60,3),(100,3),(115,15),(135,15),(150,3),(190,3),(200,95),(200,245)])
    pygame.draw.polygon(jersey_surface,jersey_colors[2],[(190,3),(200,95),(200,200),(247,200),(247,65)])
    #Draw decorations
    #print(jersey_decorations)
    for decoration in jersey_decorations:
        #print(decoration[0])
        #print(decoration[0])
        if(decoration[0]==100):
            pygame.draw.line(jersey_surface, decoration[1], [100, 8], [115, 20], 15)
            pygame.draw.line(jersey_surface, decoration[1], [115, 20], [135, 20], 15)
            pygame.draw.line(jersey_surface, decoration[1], [135, 20], [150, 8], 15)
        if(decoration[0]==101):
            pygame.draw.polygon(jersey_surface,decoration[1],[(32,34),(60,3),(100,3),(115,15),(135,15),(150,3),(190,3),(219,34)])
        if(decoration[0]==102):
            pygame.draw.line(jersey_surface, decoration[1], [29, 37], [222, 37], 5)
        if(decoration[0]==103):
            pygame.draw.rect(jersey_surface,decoration[1],(50,25,150,30))
            pygame.draw.rect(jersey_surface,decoration[1],(50,120,150,45))
            pygame.draw.rect(jersey_surface,decoration[1],(50,210,150,40))
        if(decoration[0]==104 and not is_front):
            pygame.draw.rect(jersey_surface,decoration[1],(65,25,120,140))
        if(decoration[0]==105):
            pygame.draw.rect(jersey_surface,decoration[1],(60,3,20,242))
            pygame.draw.polygon(jersey_surface,decoration[1],[(100,3),(100,245),(117,245),(117,15),(115,15)])
            pygame.draw.polygon(jersey_surface,decoration[1],[(150,3),(150,245),(133,245),(133,15),(135,15)])
            pygame.draw.rect(jersey_surface,decoration[1],(170,3,20,242))
        if(decoration[0]==106):
            pygame.draw.rect(jersey_surface,decoration[1],(50,120,150,10))
            pygame.draw.rect(jersey_surface,decoration[1],(50,160,150,10))
        if(decoration[0]==107 and is_front):
            pygame.draw.rect(jersey_surface,decoration[1],(50,120,150,45))
        if(decoration[0]==108 and is_front):
            pygame.draw.rect(jersey_surface,decoration[1],(50,125,150,35))
        if(decoration[0]==150 and logo is not None and is_front):
            logo_file = pygame.image.load(f"images/logos/{logo}")
            logo_file = pygame.transform.scale(logo_file,(80,80))
            logo_rect = logo_file.get_rect(center=(125, 145))
            jersey_surface.blit(logo_file, logo_rect)
        if(decoration[0]==151 and logo is not None and is_front):
            logo_file = pygame.image.load(f"images/logos/{logo}")
            logo_file = pygame.transform.scale(logo_file,(40,40))
            logo_rect = logo_file.get_rect()
            logo_rect.top = 60
            logo_rect.left = 140
            jersey_surface.blit(logo_file, logo_rect)
        if(decoration[0]==200):
            pygame.draw.rect(jersey_surface,decoration[1],(3,185,47,15))
        if(decoration[0]==201):
            pygame.draw.rect(jersey_surface,decoration[1],(3,135,47,10))
            pygame.draw.rect(jersey_surface,decoration[1],(3,175,47,10))
        if(decoration[0]==202):
            pygame.draw.rect(jersey_surface,decoration[1],(3,145,47,55))
        if(decoration[0]==203):
            pygame.draw.rect(jersey_surface,decoration[1],(3,145,47,25))
        if(decoration[0]==300):
            pygame.draw.rect(jersey_surface,decoration[1],(200,185,47,15))
        if(decoration[0]==301):
            pygame.draw.rect(jersey_surface,decoration[1],(200,135,47,10))
            pygame.draw.rect(jersey_surface,decoration[1],(200,175,150,10))
        if(decoration[0]==302):
            pygame.draw.rect(jersey_surface,decoration[1],(200,145,47,55))
        if(decoration[0]==303):
            pygame.draw.rect(jersey_surface,decoration[1],(200,145,47,25))
        if(decoration[0]==400):
            pygame.draw.rect(jersey_surface,decoration[1],(50,215,150,30))
        if(decoration[0]==401):
            pygame.draw.polygon(jersey_surface,decoration[1],[(55,245),(70,190),(85,175),(75,200),(90,215),(100,200),(105,215),(120,245)])
            pygame.draw.polygon(jersey_surface,decoration[1],[(195,245),(180,190),(165,175),(175,200),(160,215),(150,200),(145,215),(130,245)])
        if(decoration[0]==402):
            pygame.draw.line(jersey_surface, decoration[1], [53, 245], [68, 192], 5)
            pygame.draw.line(jersey_surface, decoration[1], [68, 192], [88, 172], 5)
            pygame.draw.line(jersey_surface, decoration[1], [88, 172], [78, 200], 5)
            pygame.draw.line(jersey_surface, decoration[1], [78, 200], [90, 217], 5)
            pygame.draw.line(jersey_surface, decoration[1], [90, 217], [100, 202], 5)
            pygame.draw.line(jersey_surface, decoration[1], [100, 202], [107, 215], 5)
            pygame.draw.line(jersey_surface, decoration[1], [107, 215], [122, 245], 5)

            pygame.draw.line(jersey_surface, decoration[1], [197, 245], [182, 192], 5)
            pygame.draw.line(jersey_surface, decoration[1], [182, 192], [162, 172], 5)
            pygame.draw.line(jersey_surface, decoration[1], [162, 172], [172, 200], 5)
            pygame.draw.line(jersey_surface, decoration[1], [172, 200], [160, 217], 5)
            pygame.draw.line(jersey_surface, decoration[1], [160, 217], [150, 202], 5)
            pygame.draw.line(jersey_surface, decoration[1], [150, 202], [143, 215], 5)
            pygame.draw.line(jersey_surface, decoration[1], [143, 215], [128, 245], 5)

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
    if(not is_front):
        number_font = pygame.font.Font(None, 160)
        number_text = number_font.render(jersey_number, True, jersey_colors[4])
        number_rect = number_text.get_rect(center=(125, 125))
    else:
        number_font = pygame.font.Font(None, 50)
        number_text = number_font.render(jersey_number, True, jersey_colors[4])
        number_rect = number_text.get_rect()
        number_rect.top = 60
        number_rect.left = 65
    jersey_surface.blit(number_text, number_rect)

    return jersey_surface