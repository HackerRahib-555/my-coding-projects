import pygame
import random

Width = 900
Height = 500
pygame.init()

# Initialize score and game variables
score = 0
x = 250
y = 470
player = pygame.Rect(x, y, 70, 70)
player_speed = 5

# Set up the display
display = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()

# Function to spawn random blocks
def spawn_enemies():
    num_enemies = random.randint(4, 10)  # Random number of enemies between 2 and 6
    enemies = []
    global places
    places = [0, 25, 100, 200, 300, 400, 500, 600, 700, 800, 900]
    for _ in range(num_enemies):
        
        enemy_x = random.choice(places)
        enemy_y = 0  # Start off-screen above the window
        
        enemies.append(pygame.Rect(enemy_x, enemy_y, 50, 50))
    return enemies

# Initialize the enemies
enemies = spawn_enemies()
enemy_speed = 1

# Initialize game state
running = True
game_over = False

while running:
    display.fill((0, 0, 255))  # Background color
    keys = pygame.key.get_pressed()

    # Player movement
    if not game_over:
        if keys[pygame.K_LEFT]:
            player.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player.x += player_speed
        if keys[pygame.K_a]:
            player.x -= player_speed
        if keys[pygame.K_d]:
            player.x += player_speed

        # Move enemies down
        for enemy in enemies:
            enemy.y += enemy_speed
        
        # Check for collisions
        for enemy in enemies:
            if enemy.colliderect(player):
                game_over = True
                break  # Stop checking for collisions after game over

        # Respawn enemies when they reach the bottom of the screen
        for enemy in enemies:
            if enemy.y >= Height:
                enemy.y = 0
                enemy.x = random.choice(places)
                spawn_enemies()

        # Increase score
        score += 1

        # Display score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        display.blit(score_text, (10, 10))

    # Game over screen
    if game_over:
        game_over_text = pygame.font.Font(None, 30)
        game_over_message = game_over_text.render(f'Game Over! Score: {score} Press Q to restart!', True, (255, 0, 0))
        display.blit(game_over_message, (100, 100))

        # Wait for 'Q' to restart
        if keys[pygame.K_q]:
            game_over = False
            score = 0
            enemies = spawn_enemies()  # Respawn enemies
            player.x = 250  # Reset player position
            player.y = 470  # Reset player position
        
        if player.x <= 0:
            player.x = 0  # Prevent moving past the left edge
        if player.x >= 900:
            player.x = 900 

    # Draw player and enemies
    pygame.draw.rect(display, (0, 255, 0), player)
    for enemy in enemies:
        pygame.draw.rect(display, (255, 0, 0), enemy)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(240)
    pygame.display.flip()

pygame.quit()
