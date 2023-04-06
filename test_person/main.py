import pygame
import time
from person import Person

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 400, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Random Persons")

# Create 3 person objects with randomized features
persons = [Person() for _ in range(3)]

# Iterate through each person and display their face for 5 seconds
for person in persons:
    # Generate the person's face as an image variable
    image_variable = person.generate_image()

    # Display the image on the screen
    screen.blit(image_variable, (0, 0))
    pygame.display.flip()

    # Wait for 5 seconds
    time.sleep(5)

# Quit Pygame
pygame.quit()
