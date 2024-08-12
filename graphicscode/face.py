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
MOUTH_COLORS = [(255, 0, 0), (200, 100, 100), (170, 100,120)]

class Face:
    #def __init__(self, shape: int, skin_tone: int, hair: dict, eyes: dict) -> None:
    def __init__(self, face_dict: dict) -> None: 
        self.shape:int = face_dict.get('shape')
        self.skin_tone: int = face_dict.get('skin_tone')
        self.hair: dict = face_dict.get('hair')
        self.eyes: dict = face_dict.get('eyes')
        self.nose: int = face_dict.get('nose')
        self.mouth: dict = face_dict.get('mouth')
        

    def draw_face(self) -> pygame.Surface:
        face_surface = pygame.Surface((300,300), pygame.SRCALPHA)
        face_surface.fill(WHITE)
        skin_tones = SKIN_TONES[self.skin_tone]
        match self.shape:
            case 1:
                pygame.draw.ellipse(face_surface, skin_tones[1], [50, 53, 200, 200], 0)
                pygame.draw.ellipse(face_surface, skin_tones[0], [50, 50, 200, 200], 0)
            case 2:
                pygame.draw.ellipse(face_surface, skin_tones[1], [50, 33, 200, 250], 0)
                pygame.draw.ellipse(face_surface, skin_tones[0], [50, 30, 200, 250], 0)
            case 3:
                pygame.draw.ellipse(face_surface, skin_tones[1], [50, 53, 200, 200], 0)
                pygame.draw.ellipse(face_surface, skin_tones[1], [110, 193, 75, 75], 0)
                pygame.draw.ellipse(face_surface, skin_tones[0], [50, 50, 200, 200], 0)
                pygame.draw.ellipse(face_surface, skin_tones[0], [110, 190, 75, 75], 0)
            case _:
                pygame.draw.ellipse(face_surface, skin_tones[0], [50, 50, 200, 200], 0)
        face_surface = self.draw_eyes(face_surface)
        face_surface = self.draw_eyebrows(face_surface)
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
                pygame.draw.polygon(face_surface, hair_colors[0], [(150,20+vertical_offset),
                                                        (200,30+vertical_offset),(230,50+vertical_offset),
                                                        (245,80+vertical_offset),(255,90+vertical_offset),
                                                        (240,95+vertical_offset),(230,100+vertical_offset),
                                                        (220,80+vertical_offset),(190,95+vertical_offset),
                                                        (160,55+vertical_offset),
                                                        (145,80+vertical_offset),(125,50+vertical_offset),
                                                        (105,100+vertical_offset),(90,75+vertical_offset),
                                                        (85,90+vertical_offset),(80,80+vertical_offset),
                                                        (80,95+vertical_offset),(70,80+vertical_offset),
                                                        (55,120+vertical_offset),(50,100+vertical_offset),
                                                        (55,90+vertical_offset),(45,110+vertical_offset),
                                                        (70,50+vertical_offset),(100,30+vertical_offset)])
                pygame.draw.polygon(face_surface, hair_colors[1],[(145,25+vertical_offset),(190, 40+vertical_offset), (210, 60+vertical_offset)])
                pygame.draw.polygon(face_surface, hair_colors[1],[(226,68+vertical_offset),(238, 89+vertical_offset), (235, 65+vertical_offset)])
                pygame.draw.polygon(face_surface, hair_colors[1],[(130,42+vertical_offset),(143, 63+vertical_offset), (154, 46+vertical_offset), (144, 57+vertical_offset)])
                pygame.draw.polygon(face_surface, hair_colors[1],[(171,55+vertical_offset),(190, 83+vertical_offset), (213, 73+vertical_offset), (195, 76+vertical_offset), (193, 59+vertical_offset), (182, 72+vertical_offset)])
                pygame.draw.polygon(face_surface, hair_colors[1],[(90,67+vertical_offset),(86, 84+vertical_offset), (79, 77+vertical_offset), (70, 93+vertical_offset), (60, 90+vertical_offset), (80, 58+vertical_offset)])
            case 2:       
                pygame.draw.polygon(face_surface, hair_colors[0], [(43,52+vertical_offset),
                                                        (54,50+vertical_offset),
                                                        (56,57+vertical_offset),
                                                        (47,66+vertical_offset),
                                                        (50,76+vertical_offset),
                                                        (57,82+vertical_offset),
                                                        (56,103+vertical_offset),
                                                        (48,112+vertical_offset),
                                                        (46,199+vertical_offset),
                                                        (52,173+vertical_offset),
                                                        (64,137+vertical_offset),
                                                        (65,106+vertical_offset),
                                                        (76,89+vertical_offset),
                                                        (135,80+vertical_offset),
                                                        (154,82+vertical_offset),
                                                        (164,92+vertical_offset),
                                                        (200,87+vertical_offset),
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
                pygame.draw.polygon(face_surface, hair_colors[1], [
                                                        (135,70+vertical_offset),
                                                        (154,72+vertical_offset),
                                                        (164,82+vertical_offset),
                                                        (200,77+vertical_offset),
                                                        (180,70+vertical_offset)])
                pygame.draw.polygon(face_surface, hair_colors[1], [
                                                        (105,60+vertical_offset),
                                                        (104,72+vertical_offset),
                                                        (124,82+vertical_offset),
                                                        (100,77+vertical_offset),
                                                        (120,65+vertical_offset)])
                pygame.draw.polygon(face_surface, hair_colors[1], [
                                                        (56,53+vertical_offset),
                                                        (60,60+vertical_offset),
                                                        (52,68+vertical_offset),
                                                        (62,70+vertical_offset),
                                                        (50,50+vertical_offset)])
                pygame.draw.polygon(face_surface, hair_colors[1], [
                                                        (237,95+vertical_offset),
                                                        (249,122+vertical_offset),
                                                        (263,179+vertical_offset),
                                                        (264,129+vertical_offset),
                                                        (251,94+vertical_offset)])
                pygame.draw.polygon(face_surface, hair_colors[1], [
                                                        (112,39+vertical_offset),
                                                        (174,22+vertical_offset),
                                                        (214,51+vertical_offset),
                                                        (171,36+vertical_offset),
                                                        (168,53+vertical_offset),
                                                        (157,34+vertical_offset),
                                                        (147,56+vertical_offset),
                                                        (140,39+vertical_offset)])
                pygame.draw.polygon(face_surface, hair_colors[1],[(84,30+vertical_offset),(78, 43+vertical_offset), (106, 22+vertical_offset)])
                pygame.draw.polygon(face_surface, hair_colors[1],[(54,117+vertical_offset),(53, 156+vertical_offset), (60, 123+vertical_offset)])
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
        skin_tones = SKIN_TONES[self.skin_tone]

        match self.eyes.get("shape"):
            case 1:
                pygame.draw.ellipse(face_surface, WHITE, [135-self.eyes.get("width"), 100+vertical_offset, 30, 30], 0)
                pygame.draw.ellipse(face_surface, eye_color, [140-self.eyes.get("width"), 105+vertical_offset, 20, 20], 0)
                pygame.draw.ellipse(face_surface, BLACK, [145-self.eyes.get("width"), 110+vertical_offset, 10, 10], 0)
                pygame.draw.arc(face_surface, skin_tones[1], [130-self.eyes.get("width"),100+vertical_offset,45,25], 0, pi, width=5)
                pygame.draw.arc(face_surface, skin_tones[1], [130-self.eyes.get("width"),105+vertical_offset,40,15], 0, pi, width=5)
                pygame.draw.arc(face_surface, skin_tones[0], [130-self.eyes.get("width"),117+vertical_offset,40,15], pi, 0, width=5)
                pygame.draw.ellipse(face_surface, WHITE, [135+self.eyes.get("width"), 100+vertical_offset, 30, 30], 0)
                pygame.draw.ellipse(face_surface, eye_color, [140+self.eyes.get("width"), 105+vertical_offset, 20, 20], 0)
                pygame.draw.ellipse(face_surface, BLACK, [145+self.eyes.get("width"), 110+vertical_offset, 10, 10], 0)
                pygame.draw.arc(face_surface, skin_tones[1], [130+self.eyes.get("width"),100+vertical_offset,45,25], 0, pi, width=5)
                pygame.draw.arc(face_surface, skin_tones[1], [130+self.eyes.get("width"),105+vertical_offset,40,15], 0, pi, width=5)
                pygame.draw.arc(face_surface, skin_tones[0], [130+self.eyes.get("width"),117+vertical_offset,40,15], pi, 0, width=5)
            case 2:
                pygame.draw.ellipse(face_surface, WHITE, [135-self.eyes.get("width"), 100+vertical_offset, 30, 40], 0)
                pygame.draw.ellipse(face_surface, eye_color, [140-self.eyes.get("width"), 105+vertical_offset, 20, 30], 0)
                pygame.draw.ellipse(face_surface, BLACK, [145-self.eyes.get("width"), 115+vertical_offset, 10, 10], 0)
                pygame.draw.ellipse(face_surface, WHITE, [135+self.eyes.get("width"), 100+vertical_offset, 30, 40], 0)
                pygame.draw.ellipse(face_surface, eye_color, [140+self.eyes.get("width"), 105+vertical_offset, 20, 30], 0)
                pygame.draw.ellipse(face_surface, BLACK, [145+self.eyes.get("width"), 115+vertical_offset, 10, 10], 0)
            case 3:
                pygame.draw.ellipse(face_surface, WHITE, [130-self.eyes.get("width"), 100+vertical_offset, 40, 30], 0)
                pygame.draw.ellipse(face_surface, eye_color, [140-self.eyes.get("width"), 105+vertical_offset, 20, 20], 0)
                pygame.draw.ellipse(face_surface, BLACK, [145-self.eyes.get("width"), 110+vertical_offset, 10, 10], 0)
                pygame.draw.arc(face_surface, skin_tones[1], [130-self.eyes.get("width"),100+vertical_offset,45,25], 0, pi, width=5)
                pygame.draw.arc(face_surface, skin_tones[0], [130-self.eyes.get("width"),117+vertical_offset,40,15], pi, 0, width=3)
                pygame.draw.ellipse(face_surface, WHITE, [130+self.eyes.get("width"), 100+vertical_offset, 40, 30], 0)
                pygame.draw.ellipse(face_surface, eye_color, [140+self.eyes.get("width"), 105+vertical_offset, 20, 20], 0)
                pygame.draw.ellipse(face_surface, BLACK, [145+self.eyes.get("width"), 110+vertical_offset, 10, 10], 0)
                pygame.draw.arc(face_surface, skin_tones[1], [130+self.eyes.get("width"),100+vertical_offset,45,25], 0, pi, width=5)
                pygame.draw.arc(face_surface, skin_tones[0], [130-self.eyes.get("width"),117+vertical_offset,40,15], pi, 0, width=3)
        return face_surface

    def draw_eyebrows(self, face_surface: pygame.Surface) -> pygame.Surface:
        hair_colors = HAIR_COLORS[self.hair.get("color")]
        match self.shape:
            case 1:
                vertical_offset=20
            case 2:
                vertical_offset=0       
            case _:
                vertical_offset=0
        match self.eyes.get("brow"):
            case 1:
                pygame.draw.arc(face_surface, hair_colors[0], [125-self.eyes.get("width"), 92+vertical_offset,50,25], 2*pi, pi, width=5)
                pygame.draw.arc(face_surface, hair_colors[0], [125+self.eyes.get("width"), 92+vertical_offset,50,25], 2*pi, pi, width=5)
            case 2:
                pygame.draw.arc(face_surface, hair_colors[1], [125-self.eyes.get("width"), 92+vertical_offset,50,25], 2*pi, pi, width=5)
                pygame.draw.arc(face_surface, hair_colors[1], [125+self.eyes.get("width"), 92+vertical_offset,50,25], 2*pi, pi, width=5)
            case 3:
                pygame.draw.arc(face_surface, hair_colors[0], [135-self.eyes.get("width"), 92+vertical_offset,40,15], 0.1, pi-0.1, width=5)
                pygame.draw.arc(face_surface, hair_colors[0], [125+self.eyes.get("width"), 92+vertical_offset,40,15], 0.1, pi-0.1, width=5)
            case 4:
                pygame.draw.arc(face_surface, hair_colors[1], [135-self.eyes.get("width"), 92+vertical_offset,40,15], 0.1, pi-0.1, width=5)
                pygame.draw.arc(face_surface, hair_colors[1], [125+self.eyes.get("width"), 92+vertical_offset,40,15], 0.1, pi-0.1, width=5)



        return face_surface

    def draw_nose(self, face_surface: pygame.Surface) -> pygame.Surface:
        skin_tones = SKIN_TONES[self.skin_tone]
        match self.shape:
            case 1:        
                pygame.draw.arc(face_surface, skin_tones[1], [160,130,25,55], pi, 3*pi/2, width=3)
                pygame.draw.arc(face_surface, skin_tones[1], [120,130,25,55], 3*pi/2, 0, width=3)
                pygame.draw.arc(face_surface, skin_tones[1], [130,175,45,15], 0, pi, width=3)
                pygame.draw.ellipse(face_surface, skin_tones[1], [145,180,5,5], 0)
                pygame.draw.ellipse(face_surface, skin_tones[1], [155,180,5,5], 0)
            case 2:
                pygame.draw.arc(face_surface, skin_tones[1], [120,130,15,55], 3*pi/2, 0, width=3)
                pygame.draw.arc(face_surface, skin_tones[1], [130,175,30,15], pi, 0, width=3)
            case _:
                pygame.draw.arc(face_surface, skin_tones[1], [160,130,25,55], pi, 3*pi/2, width=3)
                pygame.draw.arc(face_surface, skin_tones[1], [120,130,25,55], 3*pi/2, 0, width=3)
                pygame.draw.arc(face_surface, skin_tones[1], [130,175,45,15], 0, pi, width=3)
                pygame.draw.ellipse(face_surface, skin_tones[1], [145,180,5,5], 0)
                pygame.draw.ellipse(face_surface, skin_tones[1], [155,180,5,5], 0)

        return face_surface

    def draw_mouth(self, face_surface: pygame.Surface) -> pygame.Surface:
        match self.shape:
            case 1:
                vertical_offset=-20
            case 2:
                vertical_offset=0
            case _:
                vertical_offset=0

        mouth_color = MOUTH_COLORS[self.hair.get("color")]
        match self.mouth.get("shape"):
            case 1:
                pygame.draw.arc(face_surface, mouth_color, [130,210+vertical_offset,45,25], pi, 0, width=3)
            case 2:
                pygame.draw.arc(face_surface, mouth_color, [130,210+vertical_offset,45,25], pi, 0, width=6)
                pygame.draw.arc(face_surface, mouth_color, [130,220+vertical_offset,25,15], 0, pi, width=6)
                pygame.draw.arc(face_surface, mouth_color, [150,220+vertical_offset,25,15], 0, pi, width=6)
            case 3:
                pygame.draw.arc(face_surface, mouth_color, [120,210+vertical_offset,65,25], pi, 0, width=10)
            case 4:
                pygame.draw.arc(face_surface, WHITE, [120,210+vertical_offset,65,25], pi, 0, width=12)
                pygame.draw.arc(face_surface, mouth_color, [120,220+vertical_offset,65,5], pi, 0, width=8)
                pygame.draw.arc(face_surface, mouth_color, [120,215+vertical_offset,65,25], pi, 0, width=3)
            case _:
                pygame.draw.arc(face_surface, mouth_color, [130,210+vertical_offset,45,25], pi, 0, width=3)

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
                'color': self.eyes.get('color'),
                'brow': self.eyes.get('brow')
            },
            'nose': self.nose,
            'mouth': {
                'shape': self.mouth.get('shape'),
                'color': self.mouth.get('color')
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

