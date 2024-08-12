import pygame
import random

from graphicscode.face import Face
from miscfunctions import get_weighted_random_number, randomize_face

BLACK = (0,0,0)

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 400))


face = Face(randomize_face())


print(face.to_dict())
running = True
while running:
    # Handle events
    screen.fill(BLACK)
    drawnface = face.draw_face()
    drawnface_rect = drawnface.get_rect()
    drawnface_rect.top = 60
    drawnface_rect.left = 65
    screen.blit(drawnface,drawnface_rect)
  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                face = Face(randomize_face())
                print(face.to_dict())
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(f"x= {pos[0]-65} -- y= {pos[1]-60}")
    # Keep the program running at a consistent speed
    pygame.display.flip()
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()