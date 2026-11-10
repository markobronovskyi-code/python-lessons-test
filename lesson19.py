import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = pygame.Rect(400, 300, 50, 50)
coin = pygame.Rect(100, 100, 30, 30)
score = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    if player.colliderect(coin):
        score += 1
        print("Score:", score)
        coin.x = random.randint(0, 770)
        coin.y = random.randint(0, 570)

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 200, 100), player)
    pygame.draw.rect(screen, (255, 215, 0), coin)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()