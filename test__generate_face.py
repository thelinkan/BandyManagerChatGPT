import pygame
import random

from graphicscode.face import Face
from miscfunctions import get_weighted_random_number, randomize_face

BLACK = (0,0,0)
MAX_SKIN_TONES = 5
MAX_FACE_SHAPES = 5
MAX_NOSE = 3
MAX_EARS = 2
MAX_EYES = 3
MAX_EYE_COLOR = 2
MAX_EYE_BROW = 4
MAX_HAIR_COLOR = 8

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
            if event.key == pygame.K_a: #No shift
                if event.mod == 4097:
                    face.shape=face.shape+1
                    if(face.shape>MAX_FACE_SHAPES): 
                        face.shape=1
                if event.mod == 4096: #Shift
                    face.shape=face.shape-1
                    if(face.shape<1): 
                        face.shape=MAX_FACE_SHAPES
                print(face.to_dict())
            if event.key == pygame.K_s: #No shift
                if event.mod == 4097:
                    face.skin_tone=face.skin_tone+1
                    if(face.skin_tone>MAX_SKIN_TONES): 
                        face.skin_tone=0
                if event.mod == 4096: #Shift
                    face.skin_tone=face.skin_tone-1
                    if(face.skin_tone<0): 
                        face.skin_tone=MAX_SKIN_TONES
                print(face.to_dict())
            if event.key == pygame.K_n: #No shift
                if event.mod == 4097:
                    face.nose=face.nose+1
                    if(face.nose>MAX_NOSE): 
                        face.nose=1
                if event.mod == 4096: #Shift
                    face.nose=face.nose-1
                    if(face.nose<1): 
                        face.nose=MAX_NOSE
                print(face.to_dict())
            if event.key == pygame.K_e: #No shift
                if event.mod == 4097:
                    face.ears=face.ears+1
                    if(face.ears>MAX_EARS): 
                        face.ears=1
                if event.mod == 4096: #Shift
                    face.ears=face.ears-1
                    if(face.ears<1): 
                        face.ears=MAX_EARS
                print(face.to_dict())
            if event.key == pygame.K_y: #No shift
                if event.mod == 4097:
                    face.eyes['shape']=face.eyes['shape']+1
                    if(face.eyes['shape']>MAX_EYES): 
                        face.eyes['shape']=1
                if event.mod == 4096: #Shift
                    face.eyes['shape']=face.eyes['shape']-1
                    if(face.eyes['shape']<1): 
                        face.eyes['shape']=MAX_EYES
                if event.mod == 4160:
                    face.eyes['color']=face.eyes['color']+1
                    if(face.eyes['color']>MAX_EYE_COLOR): 
                        face.eyes['color']=0
                if event.mod == 4161: #Shift
                    face.eyes['color']=face.eyes['color']-1
                    if(face.eyes['color']<0): 
                        face.eyes['color']=MAX_EYE_COLOR
                if event.mod == 4352:
                    face.eyes['brow']=face.eyes['brow']+1
                    if(face.eyes['brow']>MAX_EYE_BROW): 
                        face.eyes['brow']=1
                if event.mod == 4353: #Shift
                    face.eyes['brow']=face.eyes['brow']-1
                    if(face.eyes['brow']<1): 
                        face.eyes['brow']=MAX_EYE_BROW
                print(event.mod)
                print(face.to_dict())
            if event.key == pygame.K_h:
                face.hair['shape'] = face.hair['shape'] + 1
                if(face.hair['shape']>4): 
                    face.hair['shape']=1
                print(face.to_dict())
            if event.key == pygame.K_j:
                if event.mod == 4096:
                    face.hair['color'] = face.hair['color'] + 1
                    if(face.hair['color']>MAX_HAIR_COLOR): 
                        face.hair['color']=0
                if event.mod == 4097:
                    face.hair['color'] = face.hair['color'] - 1
                    if(face.hair['color']<0): 
                        face.hair['color']=MAX_HAIR_COLOR
                print(face.to_dict())
            if event.key == pygame.K_PLUS:
                face.eyes['width'] = face.eyes['width'] + 1
                if(face.eyes['width']>55): 
                    face.eyes['width']=55
                print(face.to_dict())
            if event.key == pygame.K_MINUS:
                face.eyes['width'] = face.eyes['width'] - 1
                if(face.eyes['width']<30): 
                    face.eyes['width']=30
                print(face.to_dict())
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(f"x= {pos[0]-65} -- y= {pos[1]-60}")
    # Keep the program running at a consistent speed
    pygame.display.flip()
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()