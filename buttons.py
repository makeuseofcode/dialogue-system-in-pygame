import pygame
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

# Dialogue box properties
dialogue_box_width = 400
dialogue_box_height = 200
dialogue_box_x = (screen_width - dialogue_box_width) // 2
dialogue_box_y = (screen_height - dialogue_box_height) // 2
dialogue_box = False

# Pygame GUI manager
manager = pygame_gui.UIManager((screen_width, screen_height))

# Create a button
button_width = 100
button_height = 30
button_x = dialogue_box_x + (dialogue_box_width - button_width) // 2
button_y = dialogue_box_y + (dialogue_box_height - button_height) // 2
button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button_x, button_y, button_width, button_height),
                                      text='Click Me',
                                      manager=manager)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_speed:
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
        pygame.draw.rect(screen, GRAY, (dialogue_box_x, 
                                        dialogue_box_y, 
                                        dialogue_box_width, 
                                        dialogue_box_height))
        manager.update(pygame.time.get_ticks() / 1000.0)
        manager.draw_ui(screen)
    else:
        pygame.draw.rect(screen, WHITE, (player_x, player_y, 50, 50))
        pygame.draw.rect(screen, WHITE, (enemy_x, enemy_y, 50, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
