import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 400))

# Set up the colors
SKIN_TONE = (255, 204, 153)
DARK_SKIN_TONE = (204, 153, 102)
HAIR_COLORS = [(255, 0, 0), (255, 204, 0), (200, 200, 200)]
EYE_COLORS = [(0, 0, 255), (0, 255, 0)]
WHITE = (255,255,255)
BLACK = (0,0,0)
MOUTH_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Choose random features
hair_color = random.choice(HAIR_COLORS)
eye_color = random.choice(EYE_COLORS)
mouth_color = random.choice(MOUTH_COLORS)
if random.random() < 0.5:
    nose_color = SKIN_TONE
else:
    nose_color = DARK_SKIN_TONE

# Draw the face
face_form: int = random.randint(0,3)
face_form = 2
mouth_offset_vert : int =0
eyes_offset_vert : int = 0
if face_form == 0:
    pygame.draw.ellipse(screen, SKIN_TONE, [100, 100, 200, 200], 0)
elif face_form == 1:
    pygame.draw.ellipse(screen, SKIN_TONE, [100, 100, 200, 250], 0)
    mouth_offset_vert = 30
    eyes_offset_vert = 10
elif face_form == 2:
    pygame.draw.ellipse(screen, SKIN_TONE, [100, 100, 200, 250], 0)
    pygame.draw.ellipse(screen, DARK_SKIN_TONE, [175, 325, 50, 50], 0)
    pygame.draw.ellipse(screen, SKIN_TONE, [178, 320, 45, 45], 0)
    mouth_offset_vert = 30
    eyes_offset_vert = 10
else:
    pygame.draw.ellipse(screen, SKIN_TONE, [100, 100, 200, 275], 0)
    mouth_offset_vert = 45
    eyes_offset_vert = 15


# Draw the eyes
eye_style = random.randint(0, 1)
if eye_style == 0:
    pygame.draw.ellipse(screen, WHITE, [150, 150, 30, 30], 0)
    pygame.draw.ellipse(screen, eye_color, [155, 155, 20, 20], 0)
    pygame.draw.ellipse(screen, BLACK, [160, 160, 10, 10], 0)
    pygame.draw.ellipse(screen, WHITE, [220, 150, 30, 30], 0)
    pygame.draw.ellipse(screen, eye_color, [225, 155, 20, 20], 0)
    pygame.draw.ellipse(screen, BLACK, [230, 160, 10, 10], 0)
else:
    pygame.draw.rect(screen, eye_color, [145, 145, 40, 40], 0)
    pygame.draw.rect(screen, eye_color, [215, 145, 40, 40], 0)

# Draw the hair
hair_style = random.randint(0, 2)
if hair_style == 0:
    pygame.draw.polygon(screen, hair_color, [(200,90),(250,100),(280,120),(295,150),(305,160),(290,165),(280,170),(270,150),(240,165),(210,125),(195,150),(175,120),(155,170),(140,130),(135,150),(130,130),(110,150),(105,190),(95,180),(105,160),(120,120),(150,100)])
    #pygame.draw.polygon(screen, hair_color, [(150, 60), (190, 30), (230, 60), (190, 75)])
    #pygame.draw.ellipse(screen, hair_color, [120, 60, 160, 120], 0)
elif hair_style == 1:
    pygame.draw.rect(screen, hair_color, [130, 60, 140, 120], 0)
    pygame.draw.ellipse(screen, hair_color, [130, 100, 40, 40], 0)
    pygame.draw.ellipse(screen, hair_color, [230, 100, 40, 40], 0)
else:
    pygame.draw.ellipse(screen, hair_color, [100, 80, 200, 100], 0)
    pygame.draw.ellipse(screen, hair_color, [120, 70, 60, 80], 0)
    pygame.draw.ellipse(screen, hair_color, [220, 70, 60, 80], 0)


# Draw the nose
nose_style = random.randint(0, 1)
if nose_style == 0:
    pygame.draw.line(screen, nose_color, [185, 200], [215, 200], 5)
    pygame.draw.line(screen, nose_color, [185, 200], [200, 220], 5)
    pygame.draw.line(screen, nose_color, [215, 200], [200, 220], 5)
else:
    pygame.draw.ellipse(screen, nose_color, [180, 190, 40, 40], 0)

# Draw the mouth
mouth_style = random.randint(0, 2)
if mouth_style == 0:
    pygame.draw.rect(screen, mouth_color, [170, 250+mouth_offset_vert, 60, 20], 0)
elif mouth_style == 1:
    pygame.draw.polygon(screen, mouth_color, [(180, 260+mouth_offset_vert), (200, 270+mouth_offset_vert), (220, 260+mouth_offset_vert), (200, 275+mouth_offset_vert)])
else:
    pygame.draw.rect(screen, mouth_color, [170, 250+mouth_offset_vert, 60, 10], 0)

# Update the display
pygame.display.flip()

face_dict:dict = {
    'face_form' : 1,
    'eye_style': 2,
    'mouth_style' : 1


}

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keep the program running at a consistent speed
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()
