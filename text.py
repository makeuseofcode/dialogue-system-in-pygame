# Import necessary libraries
import pygame
from pygame.locals import *
import pygame_gui

pygame.init()

# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Player properties
player_x = 400
player_y = 500
player_speed = 5

# Enemy properties
enemy_x = 400
enemy_y = 100
enemy_speed = 3

dialogue_box_width = 400
dialogue_box_height = 200
dialogue_box_x = (screen_width - dialogue_box_width) // 2
dialogue_box_y = (screen_height - dialogue_box_height) // 2
dialogue_box = False

# Initialize Pygame GUI manager
manager = pygame_gui.UIManager((screen_width, screen_height))

# Define font properties
font = pygame.font.Font(None, 24)
text_color = BLACK


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[K_RIGHT] and player_x < screen_width - player_speed:
        player_x += player_speed

    # Update enemy position
    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_y = -50

    # Check collision
    if pygame.Rect(player_x, player_y, 50, 50).colliderect(pygame.Rect(enemy_x, enemy_y, 50, 50)):
        dialogue_box = True

    screen.fill(BLACK)

    if dialogue_box:
        pygame.draw.rect(screen, GRAY, (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height))


        # Add text to the dialog box
        text = "Hello, welcome to the game!"
        rendered_text = font.render(text, True, text_color)
        text_rect = rendered_text.get_rect(center=(dialogue_box_x + dialogue_box_width // 2,
                                                   dialogue_box_y + dialogue_box_height // 2))

        screen.blit(rendered_text, text_rect)

        manager.process_events(event)
    else:
        pygame.draw.rect(screen, WHITE, (player_x, player_y, 50, 50))
        pygame.draw.rect(screen, WHITE, (enemy_x, enemy_y, 50, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
