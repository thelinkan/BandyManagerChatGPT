import pygame

# Define button class
class Button:
    def __init__(self, x, y, width, height, text, font, text_color, button_color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.text_color = text_color
        self.button_color = button_color
        self.hover_color = hover_color
        self.action = action

    def draw(self, surface):
        color = self.button_color
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            color = self.hover_color
        pygame.draw.rect(surface, color, self.rect)
        text = self.font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def do_action(self):
        if self.action:
            self.action()   