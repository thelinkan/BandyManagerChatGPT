import pygame
from math import pi
import random

SKIN_TONE = (255, 204, 153)
SKIN_TONES =    [((255, 204, 153),(204, 153, 102)),
    ((255, 207, 187),(244, 180, 146)),
    ((216, 122, 97),(149, 95, 79)),
    ((231, 189, 152),(229, 163, 121))]

DARK_SKIN_TONE = (204, 153, 102)
HAIR_COLORS = [((255, 0, 0),(240,50,50)), ((255, 204, 0),(240,150,0)), ((200, 200, 200),(140,140,140))]
EYE_COLORS = [(60, 60, 200), (86,70,55), (85,126,86)]
WHITE = (255,255,255)
BLACK = (0,0,0)
MOUTH_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

class Face:
    #def __init__(self, shape: int, skin_tone: int, hair: dict, eyes: dict) -> None:
    def __init__(self, face_dict: dict) -> None: 
        self.shape:int = face_dict.get('shape')
        self.skin_tone: int = face_dict.get('skin_tone')
        self.hair: dict = face_dict.get('hair')
        self.eyes: dict = face_dict.get('eyes')
        

    def draw_face(self) -> pygame.Surface:
        face_surface = pygame.Surface((300,300), pygame.SRCALPHA)
        face_surface.fill(WHITE)
        skin_tones = SKIN_TONES[self.skin_tone]
        match self.shape:
            case 1:
                pygame.draw.ellipse(face_surface, skin_tones[0], [50, 50, 200, 200], 0)
            case 2:
                pygame.draw.ellipse(face_surface, skin_tones[0], [50, 30, 200, 250], 0)
            case 3:
                pygame.draw.ellipse(face_surface, skin_tones[0], [50, 50, 200, 200], 0)
                pygame.draw.ellipse(face_surface, skin_tones[0], [110, 200, 75, 75], 0)
            case _:
                pygame.draw.ellipse(face_surface, skin_tones[0], [50, 50, 200, 200], 0)
        face_surface = self.draw_eyes(face_surface)
        face_surface = self.draw_hair(face_surface)
        face_surface = self.draw_nose(face_surface)
        face_surface = self.draw_mouth(face_surface)

        return face_surface

    def draw_hair(self, face_surface: pygame.Surface) -> pygame.Surface:
        hair_colors = HAIR_COLORS[self.hair.get("color")]
        match self.shape:
            case 1:
                vertical_offset=20
            case 2:
                vertical_offset=0
            case _:
                vertical_offset=0
        match self.hair.get("shape"):
            case 1:       
                pygame.draw.polygon(face_surface, hair_colors[0], [(150,20+vertical_offset),(200,30+vertical_offset),(230,50+vertical_offset),(245,80+vertical_offset),(255,90+vertical_offset),
                                                        (240,95+vertical_offset),(230,100+vertical_offset),(220,80+vertical_offset),(190,95+vertical_offset),(160,55+vertical_offset),
                                                        (145,80+vertical_offset),(125,50+vertical_offset),(105,100+vertical_offset),(90,60+vertical_offset),(85,80+vertical_offset),
                                                        (80,60+vertical_offset),(60,80+vertical_offset),(55,120+vertical_offset),(45,110+vertical_offset),(55,90+vertical_offset),
                                                        (70,50+vertical_offset),(100,30+vertical_offset)])
                pygame.draw.polygon(face_surface, hair_colors[1],[(145,25+vertical_offset),(190, 40+vertical_offset), (210, 60+vertical_offset)])
            case 2:       
                pygame.draw.polygon(face_surface, hair_colors[0], [(43,52+vertical_offset),
                                                        (54,50+vertical_offset),
                                                        (56,57+vertical_offset),
                                                        (47,66+vertical_offset),
                                                        (50,76+vertical_offset),
                                                        (57,82+vertical_offset),
                                                        (56,103+vertical_offset),
                                                        (64,137+vertical_offset),
                                                        (65,106+vertical_offset),
                                                        (76,89+vertical_offset),
                                                        (135,80+vertical_offset),
                                                        (174,82+vertical_offset),
                                                        (164,42+vertical_offset),
                                                        (200,77+vertical_offset),
                                                        (180,80+vertical_offset),
                                                        (210,83+vertical_offset),
                                                        (217,77+vertical_offset),
                                                        (241,108+vertical_offset),
                                                        (254,168+vertical_offset),
                                                        (267,199+vertical_offset),
                                                        (276,125+vertical_offset),
                                                        (270,102+vertical_offset),
                                                        (255,80+vertical_offset),
                                                        (249,75+vertical_offset),
                                                        (252,54+vertical_offset),
                                                        (245,63+vertical_offset),
                                                        (209,40+vertical_offset),
                                                        (196,30+vertical_offset),
                                                        (179,17+vertical_offset),
                                                        (159,14+vertical_offset),
                                                        (120,23+vertical_offset),
                                                        (104,16+vertical_offset),
                                                        (78,22+vertical_offset),
                                                        (74,33+vertical_offset),
                                                        (63,31+vertical_offset),
                                                        (44,41+vertical_offset)])
            case _:
                pygame.draw.polygon(face_surface, hair_colors[0], [(150,20+vertical_offset),(200,30+vertical_offset),(230,50+vertical_offset),(245,80+vertical_offset),(255,90+vertical_offset),
                                                        (240,95+vertical_offset),(230,100+vertical_offset),(220,80+vertical_offset),(190,95+vertical_offset),(160,55+vertical_offset),
                                                        (145,80+vertical_offset),(125,50+vertical_offset),(105,100+vertical_offset),(90,60+vertical_offset),(85,80+vertical_offset),
                                                        (80,60+vertical_offset),(60,80+vertical_offset),(55,120+vertical_offset),(45,110+vertical_offset),(55,90+vertical_offset),
                                                        (70,50+vertical_offset),(100,30+vertical_offset)])
        return face_surface

    def draw_eyes(self, face_surface: pygame.Surface) -> pygame.Surface:
        match self.shape:
            case 1:
                vertical_offset=20
            case 2:
                vertical_offset=0       
            case _:
                vertical_offset=0

        eye_color = EYE_COLORS[self.eyes.get("color")]
        match self.eyes.get("shape"):
            case 1:
                pygame.draw.ellipse(face_surface, WHITE, [135-self.eyes.get("width"), 100+vertical_offset, 30, 30], 0)
                pygame.draw.ellipse(face_surface, eye_color, [140-self.eyes.get("width"), 105+vertical_offset, 20, 20], 0)
                pygame.draw.ellipse(face_surface, BLACK, [145-self.eyes.get("width"), 110+vertical_offset, 10, 10], 0)
                pygame.draw.ellipse(face_surface, WHITE, [135+self.eyes.get("width"), 100+vertical_offset, 30, 30], 0)
                pygame.draw.ellipse(face_surface, eye_color, [140+self.eyes.get("width"), 105+vertical_offset, 20, 20], 0)
                pygame.draw.ellipse(face_surface, BLACK, [145+self.eyes.get("width"), 110+vertical_offset, 10, 10], 0)
            case 2:
                pygame.draw.ellipse(face_surface, WHITE, [135-self.eyes.get("width"), 100+vertical_offset, 30, 40], 0)
                pygame.draw.ellipse(face_surface, eye_color, [140-self.eyes.get("width"), 105+vertical_offset, 20, 30], 0)
                pygame.draw.ellipse(face_surface, BLACK, [145-self.eyes.get("width"), 115+vertical_offset, 10, 10], 0)
                pygame.draw.ellipse(face_surface, WHITE, [135+self.eyes.get("width"), 100+vertical_offset, 30, 40], 0)
                pygame.draw.ellipse(face_surface, eye_color, [140+self.eyes.get("width"), 105+vertical_offset, 20, 30], 0)
                pygame.draw.ellipse(face_surface, BLACK, [145+self.eyes.get("width"), 115+vertical_offset, 10, 10], 0)
            case 3:
                pygame.draw.ellipse(face_surface, WHITE, [125-self.eyes.get("width"), 100+vertical_offset, 40, 30], 0)
                pygame.draw.ellipse(face_surface, eye_color, [130-self.eyes.get("width"), 105+vertical_offset, 30, 20], 0)
                pygame.draw.ellipse(face_surface, BLACK, [140-self.eyes.get("width"), 110+vertical_offset, 10, 10], 0)
                pygame.draw.ellipse(face_surface, WHITE, [135+self.eyes.get("width"), 100+vertical_offset, 40, 30], 0)
                pygame.draw.ellipse(face_surface, eye_color, [140+self.eyes.get("width"), 105+vertical_offset, 30, 20], 0)
                pygame.draw.ellipse(face_surface, BLACK, [150+self.eyes.get("width"), 110+vertical_offset, 10, 10], 0)
        return face_surface

    def draw_nose(self, face_surface: pygame.Surface) -> pygame.Surface:
        skin_tones = SKIN_TONES[self.skin_tone]
        pygame.draw.arc(face_surface, skin_tones[1], [140,150,25,25], pi, pi/3, width=3)
        return face_surface

    def draw_mouth(self, face_surface: pygame.Surface) -> pygame.Surface:
        match self.shape:
            case 1:
                vertical_offset=-20
            case 2:
                vertical_offset=0
            case _:
                vertical_offset=0

        mouth_color = MOUTH_COLORS[0]
        pygame.draw.arc(face_surface, mouth_color, [140,210+vertical_offset,25,25], pi, pi/3, width=3)
        return face_surface

    def to_dict(self) -> dict:
        return {
            'shape': self.shape,
            'skin_tone': self.skin_tone,
            'hair': {
                'shape': self.hair.get('shape'),
                'color': self.hair.get('color')
            },
            'eyes': {
                'shape': self.eyes.get('shape'),
                'width': self.eyes.get('width'),
                'color': self.eyes.get('color')
            }
        }

'''
# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 400))
hair: dict = {'shape': 1, 'color': 2}
eyes: dict = {'shape': 2, 'width': 35, 'color': 1}
face = Face(2,3,hair, eyes)
print(f'{SKIN_TONES[1]=}')

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

    # Keep the program running at a consistent speed
    pygame.display.flip()
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()

'''

