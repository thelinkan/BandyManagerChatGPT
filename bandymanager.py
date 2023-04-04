import pygame
import json
from country import Country
from team import Team

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bandy Manager")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load the teams and countries from the JSON files
with open('teams.json') as f:
    teams_data = json.load(f)

with open('countries.json') as f:
    countries_data = json.load(f)


# Create the country objects
countries = {}
for country_data in countries_data:
    name = country_data['name']
    bandy_knowledge = country_data['bandy_knowledge']
    population = country_data['population']
    flag_path = country_data['flag_path']
    male_proficiency = country_data['male_proficiency']
    female_proficiency = country_data['female_proficiency']
    countries[name] = Country(name, flag_path, bandy_knowledge, population, male_proficiency, female_proficiency)

# Create the team objects
teams = []
for team_data in teams_data:
    name = team_data['name']
    country_name = team_data['country']
    male = team_data['male']
    female = team_data['female']
    country = countries[country_name]
    team = Team(name, country, male, female)
    teams.append(team)

# Sort the teams by their total proficiency
teams.sort(key=lambda team: team.total_proficiency, reverse=True)

# Set up font
FONT_SIZE = 30
font = pygame.font.SysFont(None, FONT_SIZE)

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the teams
    x = 100
    y = 100
    for team in teams:
        text = f"{team.name} ({team.country.name}): {team.total_proficiency}"
        text_surface = font.render(text, True, (0, 0, 0))
        screen.blit(text_surface, (x, y))
        y += 30

    # Update the display
    pygame.display.flip()
# Quit Pygame
pygame.quit()
