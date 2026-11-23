import pygame
from lesson33 import enemies

direction = 1
enemy_speed = 2

for enemy in enemies:
    enemy.rect.x += enemy_speed * direction