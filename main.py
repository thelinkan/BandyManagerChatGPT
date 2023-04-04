import pygame
import json
import pickle
from game import Game
from inputbox import InputBox

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
def quit_game():
    pygame.quit()
    quit()

# Define buttons
button_width = 230
button_height = 50
button_x = (SCREEN_WIDTH - button_width) // 2
button_spacing = 20
new_game_button = Button(button_x, 200, button_width, button_height, "New game", font, BLACK, WHITE, GRAY)
load_game_button = Button(button_x, new_game_button.rect.bottom + button_spacing, button_width, button_height, "Load game", font, BLACK, WHITE, GRAY)
credits_button = Button(button_x, load_game_button.rect.bottom + button_spacing, button_width, button_height, "Credits", font, BLACK, WHITE, GRAY)
quit_button = Button(button_x, credits_button.rect.bottom + button_spacing, button_width, button_height, "Quit game", font, BLACK, WHITE, GRAY, quit_game)

#Define Input
input_name = InputBox(100, 200, 140, 32)

def draw_start_menu():
    # Draw screen
    #print(game_state)
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
    #print(game_state)
    screen.fill(WHITE)
    title = font.render("Bandymanager - Credits", True, BLACK)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(title, title_rect)
    credits1 = small_font.render("Programmer: Torbjorn Lindquist", False, BLACK)
    
    screen.blit(credits1, (40, 250))
    pygame.display.flip()

def draw_newgame_menu():
    # Draw screen
    screen.fill(WHITE)
    title = font.render("Bandymanager - New game", True, BLACK)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(title, title_rect)

    input_name.draw(screen)
    #text_surface = small_font.render("Hello World!",False, BLACK)
    #screen.blit(text_surface, (40, 250))
    
    pygame.display.flip()

# Define game loop
running = True
while running:
    clock = pygame.time.Clock()
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "show_credits":
            	game_state = "start_menu"
            elif event.button == 1 and game_state == "start_menu":
                if new_game_button.rect.collidepoint(event.pos):
                    game_state="new_game"
                    print("New game click");
                    game = Game(2023,8,1)
                    with open('save_game.pickle', 'wb') as f:
                        pickle.dump(game, f)
                    f.close()
                    game.save_game('c:\temp')
                if load_game_button.rect.collidepoint(event.pos):
                    game_state="load_game"
                    game = Game(0,0,0)
                    game.load_game('')
                    print("Load game click");
                if credits_button.rect.collidepoint(event.pos):
                    game_state="show_credits"
                    print("Credits click");
                if quit_button.rect.collidepoint(event.pos):
                    quit_button.do_action()
        if game_state =="new_game":
            input_name.handle_event(event)

    if game_state == "start_menu":
        draw_start_menu()
    if game_state == "show_credits":
        draw_credits()
    if game_state == "new_game":
        draw_newgame_menu()
    clock.tick(30)

pygame.quit()
quit()
