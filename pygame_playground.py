import pygame
import random
import math

pygame.init()


WIDTH, HEIGHT = 700, 700
display = pygame.display.set_mode((WIDTH, HEIGHT))
global score
score = 0


koolNPC = pygame.image.load('/home/rahib/Pictures/Screenshots/NPC.png').convert()
koolNPC = pygame.transform.scale(koolNPC, (int(koolNPC.get_width() / 3), int(koolNPC.get_height() / 3)))

npc_img = pygame.image.load('/home/rahib/Pictures/Screenshots/GoofySonic.png').convert_alpha()
npc_img = pygame.transform.scale(npc_img, (int(npc_img.get_width() / 3), int(npc_img.get_height() / 3)))

follow_img = pygame.image.load('/home/rahib/Pictures/FallGuy.png').convert_alpha()
follow_width = follow_img.get_width() // 4 
follow_height = follow_img.get_height() // 4 
follow_img = pygame.transform.scale(follow_img, (follow_width, follow_height))


npc_x, npc_y = random.randint(0, WIDTH - npc_img.get_width()), random.randint(0, HEIGHT - npc_img.get_height())
npc_img = pygame.transform.scale(npc_img, (int(npc_img.get_width() / 3), int(npc_img.get_height() / 3)))

npc_speed = 3
move_timer = 0
direction = random.choice(["left", "right", "up", "down"])

follow_speed = 4
follow_x, follow_y = 700, 700

coin_img = pygame.Surface((20, 20)) 
coin_img.fill((255, 255, 0))

def coin_position():
    global coin_positionS
    coin_positionS = [(random.randint(0, WIDTH - 20), random.randint(0, HEIGHT - 20)) for _ in range(random.randint(1,12))]

coin_position()


x, y = 0, 0
player_speed = 6


pygame.mixer.init()
my_sound = pygame.mixer.Sound("/home/rahib/Music/Error.mp3")
coin_sound = pygame.mixer.Sound("/home/rahib/Music/Coin.mp3")
hit_sound = pygame.mixer.Sound("/home/rahib/Music/Metal.mp3")
sound = pygame.mixer.Sound('/home/rahib/Music/Wooo.mp3')

clock = pygame.time.Clock()
running = True

while running:
    display.fill((120, 190, 185))  
    
    mose = pygame.mouse.get_pos()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    move_timer += 1
    if move_timer > 60:
        direction = random.choice(["left", "right", "up", "down"])
        move_timer = 0

    if direction == "left" and npc_x > 0:
        npc_x -= npc_speed
    elif direction == "right" and npc_x < WIDTH - npc_img.get_width():
        npc_x += npc_speed
    elif direction == "up" and npc_y > 0:
        npc_y -= npc_speed
    elif direction == "down" and npc_y < HEIGHT - npc_img.get_height():
        npc_y += npc_speed

    dx = x - follow_x
    dy = y - follow_y
    distance = math.sqrt(dx**2 + dy**2)
    
    
    if distance != 0:
        dx /= distance
        dy /= distance

    
    follow_x += dx * follow_speed
    follow_y += dy * follow_speed

    
    
    display.blit(follow_img, (follow_x - follow_img.get_width() // 2, follow_y - follow_img.get_height() // 2))

  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= player_speed
    if keys[pygame.K_RIGHT]:
        x += player_speed
    if keys[pygame.K_UP]:
        y -= player_speed
    if keys[pygame.K_DOWN]:
        y += player_speed
        
    if keys[pygame.K_a]:
        x -= player_speed
    if keys[pygame.K_d]:
        x += player_speed
    if keys[pygame.K_w]:
        y -= player_speed
    if keys[pygame.K_s]:
        y += player_speed

    
    hitbox = pygame.Rect(x, y, koolNPC.get_width(), koolNPC.get_height())
    target = pygame.Rect(300, 0, 160, 280)
    target2 = pygame.Rect(300, 300, 60, 255)
    npc = pygame.Rect(npc_x, npc_y, npc_img.get_width() / 3,npc_img.get_height() / 3)
    Follow = pygame.Rect(follow_x, follow_y, follow_width, follow_height)

    
    collision = hitbox.colliderect(target)
    collision2 = hitbox.colliderect(target2)
    npc_collide = hitbox.colliderect(npc)
    follow_colide = hitbox.colliderect(Follow)
    mouse = target.collidepoint(mose)
    mouse2 = target2.collidepoint(mose)

    
    display.blit(koolNPC, (x, y))  
    display.blit(npc_img, (npc_x, npc_y)) 

    pygame.draw.rect(display, (255, 0, 0), target)
    pygame.draw.rect(display, (255, 0, 0), target2)

   
    if any([collision, collision2, mouse, mouse2]):
        pygame.draw.rect(display, (255, 255, 155), target)
        pygame.draw.rect(display, (55, 25, 155), target2)
        if not pygame.mixer.get_busy():  
            my_sound.play()
    elif npc_collide:
        score -=1
        hit_sound.play()
    elif follow_colide:
        sound.play()
        player_speed = 0
        pygame.time.set_timer(pygame.USEREVENT, 5000)
        player_speed = 6
        follow_speed = 0
        pygame.time.set_timer(pygame.USEREVENT, 8000)
        follow_speed = 4
        x -= random.randint(50, 75)
        y -= random.randint(10, 25)

    else:
        pygame.draw.rect(display, (0, 0, 0), target)
        pygame.draw.rect(display, (255, 0, 0), target2)

   
    for pos in coin_positionS[:]:  
        coin_rect = pygame.Rect(pos[0], pos[1], 20, 20)  
        if hitbox.colliderect(coin_rect):  
            coin_positionS.remove(pos)  
            score += 1  
            
            coin_sound.play()

    
    for pos in coin_positionS:
        display.blit(coin_img, pos)

    
    if not coin_positionS:
        coin_position()  

    
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    display.blit(score_text, (10, 10))

    
    pygame.display.flip()
    clock.tick(60) 

pygame.quit()
