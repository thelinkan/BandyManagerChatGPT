import pygame

pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Set the dimensions of the screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

game_state = "start_menu"

# Set the title of the window
pygame.display.set_caption("Bandymanager")

# Create font objects
font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 30)

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

# Define button actions
def start_new_game():
    print("Starting new game")

def load_game():
    print("Loading game")

def show_credits():
    global game_state
    game_state="show_credits"
    print("Credits")

def quit_game():
    pygame.quit()
    quit()

# Define buttons
button_width = 230
button_height = 50
button_x = (SCREEN_WIDTH - button_width) // 2
button_spacing = 20
new_game_button = Button(button_x, 200, button_width, button_height, "New game", font, BLACK, WHITE, GRAY, start_new_game)
load_game_button = Button(button_x, new_game_button.rect.bottom + button_spacing, button_width, button_height, "Load game", font, BLACK, WHITE, GRAY, load_game)
credits_button = Button(button_x, load_game_button.rect.bottom + button_spacing, button_width, button_height, "Credits", font, BLACK, WHITE, GRAY, show_credits)
quit_button = Button(button_x, credits_button.rect.bottom + button_spacing, button_width, button_height, "Quit game", font, BLACK, WHITE, GRAY, quit_game)

def draw_start_menu():
    # Draw screen
    print(game_state)
    screen.fill(WHITE)
    title = font.render("Bandymanager", True, BLACK)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(title, title_rect)
    new_game_button.draw(screen)
    load_game_button.draw(screen)
    credits_button.draw(screen)
    quit_button.draw(screen)
    pygame.display.flip()

def draw_credits():
    print(game_state)
    screen.fill(WHITE)
    title = font.render("Bandymanager - Credits", True, BLACK)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(title, title_rect)
    pygame.display.flip()

# Define game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "show_credits":
            	game_state = "start_menu"
            if event.button == 1:
                for button in [new_game_button, load_game_button, credits_button, quit_button]:
                    if button.rect.collidepoint(event.pos):
                        button.do_action()
    if game_state == "start_menu":
        draw_start_menu()
    if game_state == "show_credits":
        draw_credits()


pygame.quit()
quit()
