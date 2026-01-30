import pygame
pygame.init()
WIDTH, HEIGHT = 500, 500
display = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
x = 250
y = 250
while running:
    head = pygame.Rect(20, 20, 20, 20)
    head.fill(0, 0, 255)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    display.blit(display, (x, y))

pygame.quit()

