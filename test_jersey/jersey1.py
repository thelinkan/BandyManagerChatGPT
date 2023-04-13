import pygame

pygame.init()

# Load image
image = pygame.image.load("jersey1.png")

# Create new surface for drawing boundaries
boundary_surface = pygame.Surface(image.get_size(), pygame.SRCALPHA)

# Draw boundaries in white
boundary_color = (255, 255, 255)
for x in range(image.get_width()):
    for y in range(image.get_height()):
        if tuple(image.get_at((x, y))) < (32, 32, 32):
            if x == 0 or y == 0 or x == image.get_width() - 1 or y == image.get_height() - 1:
                boundary_surface.set_at((x, y), boundary_color)
            else:
                neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                if all(tuple(image.get_at(n)) < (32, 32, 32) for n in neighbors):
                    boundary_surface.set_at((x, y), boundary_color)

# Get subsurfaces for enclosed areas
areas = []
for x in range(image.get_width()):
    for y in range(image.get_height()):
        if boundary_surface.get_at((x, y)) == boundary_color:
            subsurface_rect = pygame.Rect(x, y, 1, 1)
            while subsurface_rect.bottomright not in [(0, 0), (image.get_width(), image.get_height())]:
                subsurface_rect.width += 1
                subsurface_rect.height += 1
                if boundary_surface.subsurface(subsurface_rect).get_at((0, 0)) != boundary_color:
                    break
            areas.append(image.subsurface(subsurface_rect))

# Get surface values for each enclosed area
for area in areas:
    for x in range(area.get_width()):
        for y in range(area.get_height()):
            surface_value = area.get_at((x, y))
            # Do something with the surface value here
            print(surface_value)

# Display result
screen = pygame.display.set_mode((image.get_width(), image.get_height()))
screen.blit(image, (0, 0))
pygame.display.flip()

# Wait for user to close window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
