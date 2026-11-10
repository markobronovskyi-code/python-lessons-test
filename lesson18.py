import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player_x = 400
player_y = 300
player_size = 50
player_speed=5
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_LSHIFT]:
        player_speed = 15
    
    player_x = max(0, min(player_x, 800 - player_size))
    player_y = max(0, min(player_y, 600 - player_size))

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 200, 100), (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, (10, 100, 200), (100, 100, 10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()