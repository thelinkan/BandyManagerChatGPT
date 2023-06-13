import pygame

pygame.init()

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 30)


class InputBox:

    def __init__(self, x, y, w, h, type = 'alpha', text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.type = type

    def handle_event(self, event, is_active, next):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                # self.active = not self.active
                self.active = True
                self.color = COLOR_ACTIVE
            else:
                self.active = False
                self.color = COLOR_INACTIVE
            # Change the current color of the input box.
            #self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if is_active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    #self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_TAB:
                    self.active = False
                    self.color = COLOR_INACTIVE
                    next.active = True
                    next.color = COLOR_ACTIVE
                    print(f"self: {self.text}, next: {next.text}")
                elif event.unicode.isnumeric() and self.type == 'numeric':
                    self.text += event.unicode
                elif event.unicode.isalnum() and self.type == 'alpha':
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def return_text(self):
        return self.text
