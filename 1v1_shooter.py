import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1v1 Shooting Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
player_size = 50
player1 = pygame.Rect(100, HEIGHT//2, player_size, player_size)
player2 = pygame.Rect(WIDTH - 150, HEIGHT//2, player_size, player_size)

# Bullet settings
bullets = []
bullet_speed = 7

# Clock
clock = pygame.time.Clock()
FPS = 60

# Score
score1 = 0
score2 = 0

font = pygame.font.SysFont(None, 36)

def draw_window():
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player1)
    pygame.draw.rect(screen, BLUE, player2)
    
    for bullet in bullets:
        pygame.draw.rect(screen, BLACK, bullet)
    
    score_text = font.render(f"P1: {score1}  P2: {score2}", True, BLACK)
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))
    
    pygame.display.update()

# Main loop
run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                bullet = pygame.Rect(player1.x + player_size, player1.y + player_size//2 - 5, 10, 10)
                bullets.append((bullet, 1))
            if event.key == pygame.K_LEFT:
                bullet = pygame.Rect(player2.x - 10, player2.y + player_size//2 - 5, 10, 10)
                bullets.append((bullet, -1))

    keys = pygame.key.get_pressed()
    # Player 1 controls
    if keys[pygame.K_w] and player1.y - 5 > 0:
        player1.y -= 5
    if keys[pygame.K_s] and player1.y + player_size + 5 < HEIGHT:
        player1.y += 5
    # Player 2 controls
    if keys[pygame.K_UP] and player2.y - 5 > 0:
        player2.y -= 5
    if keys[pygame.K_DOWN] and player2.y + player_size + 5 < HEIGHT:
        player2.y += 5

    # Bullet movement
    for bullet in bullets[:]:
        rect, direction = bullet
        rect.x += bullet_speed * direction

        if rect.colliderect(player1) and direction == -1:
            score2 += 1
            bullets.remove(bullet)
        elif rect.colliderect(player2) and direction == 1:
            score1 += 1
            bullets.remove(bullet)
        elif rect.x < 0 or rect.x > WIDTH:
            bullets.remove(bullet)

    draw_window()

pygame.quit()
