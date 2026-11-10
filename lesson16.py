import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Marko's Adventure")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((200, 200, 200))
    pygame.draw.rect(screen, (100, 212, 0), (300, 150, 100, 300, ))
    pygame.draw.circle(screen, (50, 50 , 100), (350, 110), 100 )
    pygame.draw.line(screen, (200, 0, 0), (10, 100), (400, 400), 10)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()