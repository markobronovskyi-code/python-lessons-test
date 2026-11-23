import pygame

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 6, 15)
        self.speed = 8

    def update(self):
        self.rect.y -= self.speed
