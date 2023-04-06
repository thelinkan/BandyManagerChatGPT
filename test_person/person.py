import random
import pygame

class Person:
    def __init__(self):
        # Set up the colors
        self.skin_tone = (255, 204, 153)
        self.dark_skin_tone = (204, 153, 102)
        self.hair_color = (255, 0, 0)
        self.eye_color = (0, 0, 255)
        self.mouth_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

        # Randomize the features
        self.mouth_color = random.choice(self.mouth_colors)
        if random.random() < 0.5:
            self.nose_color = self.skin_tone
        else:
            self.nose_color = self.dark_skin_tone
        self.nose_style = random.randint(0, 1)
        self.mouth_style = random.randint(0, 2)

    def generate_image(self):
        # Create a new surface with the same size as the screen surface
        surface = pygame.Surface((400, 400))

        # Draw the face
        pygame.draw.ellipse(surface, self.skin_tone, [100, 100, 200, 200], 0)

        # Draw the hair
        pygame.draw.polygon(surface, self.hair_color, [(150, 60), (190, 30), (230, 60), (190, 75)])
        pygame.draw.ellipse(surface, self.hair_color, [120, 60, 160, 120], 0)

        # Draw the eyes
        pygame.draw.ellipse(surface, self.eye_color, [150, 150, 30, 30], 0)
        pygame.draw.ellipse(surface, self.eye_color, [220, 150, 30, 30], 0)

        # Draw the nose
        if self.nose_style == 0:
            pygame.draw.line(surface, self.nose_color, [185, 200], [215, 200], 5)
            pygame.draw.line(surface, self.nose_color, [185, 200], [200, 220], 5)
            pygame.draw.line(surface, self.nose_color, [215, 200], [200, 220], 5)
        else:
            pygame.draw.ellipse(surface, self.nose_color, [180, 190, 40, 40], 0)

        # Draw the mouth
        if self.mouth_style == 0:
            pygame.draw.rect(surface, self.mouth_color, [170, 250, 60, 20], 0)
        elif self.mouth_style == 1:
            pygame.draw.polygon(surface, self.mouth_color, [(180, 260), (200, 270), (220, 260), (200, 275)])
        else:
            pygame.draw.rect(surface, self.mouth_color, [170, 250, 60, 10], 0)

        # Return the generated surface as an image variable
        return surface.convert_alpha()
