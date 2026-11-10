import random
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Coin Collector")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

player = pygame.Rect(100, 100, 50, 50)
player_speed = 5
coin = pygame.Rect(400, 300, 30, 30)
score = 0
running = True


def place_coin():
    global coin
    coin = pygame.Rect(
        random.randint(0, SCREEN_WIDTH - 30),
        random.randint(0, SCREEN_HEIGHT - 30),
        30,
        30,
    )


def move_player():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += player_speed

    player.x = max(0, min(SCREEN_WIDTH - player.width, player.x))
    player.y = max(0, min(SCREEN_HEIGHT - player.height, player.y))


def draw_game():
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.ellipse(screen, (255, 215, 0), coin)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))

    pygame.display.flip()


def main():
    global running, score

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        move_player()

        if player.colliderect(coin):
            score += 1
            place_coin()

        draw_game()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()