import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 200, 100), self.rect)

player = Player(175, 125)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    player.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()