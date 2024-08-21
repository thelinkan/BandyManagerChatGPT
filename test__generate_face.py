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
            if event.key == pygame.K_s:
                face.skin_tone=face.skin_tone+1
                if(face.skin_tone>5): 
                    face.skin_tone=0
                print(face.to_dict())
            if event.key == pygame.K_h:
                face.hair['shape'] = face.hair['shape'] + 1
                if(face.hair['shape']>4): 
                    face.hair['shape']=1
                print(face.to_dict())
            if event.key == pygame.K_j:
                face.hair['color'] = face.hair['color'] + 1
                if(face.hair['color']>6): 
                    face.hair['color']=0
                print(face.to_dict())
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(f"x= {pos[0]-65} -- y= {pos[1]-60}")
    # Keep the program running at a consistent speed
    pygame.display.flip()
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()