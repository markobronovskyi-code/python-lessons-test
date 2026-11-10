import pygame as py

py.init()
screen = py.display.set_mode((800, 600))
clock = py.time.Clock()

player_x = 100
player_y = 300
speed_x = 2
speed_y = 2
speed_x = 4
speed_y = 3

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
    # update position (horizontal + vertical)
    player_x += speed_x
    player_y += speed_y

    # clamp and reverse horizontal direction at left/right edges
    if player_x > 750:
        player_x = 750
        speed_x = -speed_x   # тепер летить уліво
    if player_x < 0:
        player_x = 0
        speed_x = -speed_x

    # clamp and reverse vertical direction at top/bottom edges
    if player_y > 550:
        player_y = 550
        speed_y = -speed_y
    if player_y < 0:
        player_y = 0
        speed_y = -speed_y

    screen.fill((30, 30, 30))
    py.draw.rect(screen, (0, 200, 100), (player_x, player_y, 50, 50))
    py.display.flip()
    clock.tick(60)

py.quit()