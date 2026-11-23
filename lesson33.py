import pygame


class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)


enemies = []
for row in range(3):
    for col in range(8):
        enemies.append(Enemy(80 + col * 70, 60 + row * 60))