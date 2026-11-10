import pygame

player_x = 100
player_y = 300
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Marko's Game")
player_x += 2

pygame.draw.rect(
    screen,
    (0, 200, 100),
    (player_x, player_y, 50, 50)
)
if player_x > 750:
    player_x = 750
running = True
clock = pygame.time.Clock()
while running:
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (50, 150, 255), (100, 100, 80, 80))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
clock.tick(60)
pygame.quit()
