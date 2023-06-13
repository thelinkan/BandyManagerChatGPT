import pygame

def draw_arrow_left(color):
    arrow_surface = pygame.Surface((50,50), pygame.SRCALPHA)
    pygame.draw.polygon(arrow_surface,color,[(0,25),(25,49),(25,37),(49,37),(49,12),(25,12),(25,0)])
    return arrow_surface

def draw_arrow_right(color):
    arrow_surface = pygame.Surface((50,50), pygame.SRCALPHA)
    pygame.draw.polygon(arrow_surface,color,[(49,25),(25,49),(25,37),(0,37),(0,12),(25,12),(25,0)])
    return arrow_surface

def draw_arrow_up(color):
    arrow_surface = pygame.Surface((50,50), pygame.SRCALPHA)
    pygame.draw.polygon(arrow_surface,color,[(25,0),(49,25),(37,25),(37,49),(12,49),(12,25),(0,25)])
    return arrow_surface

def draw_arrow_down(color):
    arrow_surface = pygame.Surface((50,50), pygame.SRCALPHA)
    pygame.draw.polygon(arrow_surface,color,[(25,49),(49,25),(37,25),(37,0),(12,0),(12,25),(0,25)])
    return arrow_surface
