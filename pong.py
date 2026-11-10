import pygame
import sys
from enum import Enum

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Clock for FPS
CLOCK = pygame.time.Clock()
FPS = 60

# Ball properties
BALL_SIZE = 15
BALL_SPEED_X = 7
BALL_SPEED_Y = 7
MAX_BALL_SPEED = 10

# Paddle properties
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7

class GameState(Enum):
    MENU = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off top and bottom
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y = -self.speed_y

        # Ball out of bounds
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            return False  # Ball is out
        return True

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)

    def reset(self, x, y):
        self.rect.center = (x, y)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y


class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED

    def update(self, keys, up_key, down_key):
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)


class PongGame:
    def __init__(self):
        self.state = GameState.MENU
        self.left_paddle = Paddle(20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.right_paddle = Paddle(SCREEN_WIDTH - 20 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.left_score = 0
        self.right_score = 0
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)

    def check_paddle_collision(self):
        # Left paddle collision
        if self.ball.rect.colliderect(self.left_paddle.rect):
            if self.ball.speed_x < 0:
                self.ball.speed_x = -self.ball.speed_x
                self.ball.rect.left = self.left_paddle.rect.right

        # Right paddle collision
        if self.ball.rect.colliderect(self.right_paddle.rect):
            if self.ball.speed_x > 0:
                self.ball.speed_x = -self.ball.speed_x
                self.ball.rect.right = self.right_paddle.rect.left

    def update(self):
        if self.state == GameState.PLAYING:
            keys = pygame.key.get_pressed()
            self.left_paddle.update(keys, pygame.K_w, pygame.K_s)
            self.right_paddle.update(keys, pygame.K_UP, pygame.K_DOWN)

            self.ball.update()
            self.check_paddle_collision()

            # Score points
            if self.ball.rect.left <= 0:
                self.right_score += 1
                self.ball.reset(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            elif self.ball.rect.right >= SCREEN_WIDTH:
                self.left_score += 1
                self.ball.reset(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def draw(self):
        SCREEN.fill(BLACK)

        if self.state == GameState.MENU:
            self.draw_menu()
        elif self.state == GameState.PLAYING:
            self.draw_game()
        elif self.state == GameState.PAUSED:
            self.draw_game()
            self.draw_paused()

        pygame.display.flip()

    def draw_menu(self):
        title = self.font.render("PONG", True, WHITE)
        start_text = self.small_font.render("Press SPACE to Start", True, WHITE)
        instructions = self.small_font.render("W/S - Left Paddle | UP/DOWN - Right Paddle", True, GRAY)
        
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        instructions_rect = instructions.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        
        SCREEN.blit(title, title_rect)
        SCREEN.blit(start_text, start_rect)
        SCREEN.blit(instructions, instructions_rect)

    def draw_game(self):
        # Draw center line
        for y in range(0, SCREEN_HEIGHT, 10):
            pygame.draw.line(SCREEN, GRAY, (SCREEN_WIDTH // 2, y), (SCREEN_WIDTH // 2, y + 5), 2)

        # Draw scores
        left_score_text = self.font.render(str(self.left_score), True, WHITE)
        right_score_text = self.font.render(str(self.right_score), True, WHITE)
        SCREEN.blit(left_score_text, (SCREEN_WIDTH // 4, 50))
        SCREEN.blit(right_score_text, (3 * SCREEN_WIDTH // 4 - 50, 50))

        # Draw game objects
        self.left_paddle.draw(SCREEN)
        self.right_paddle.draw(SCREEN)
        self.ball.draw(SCREEN)

    def draw_paused(self):
        pause_text = self.font.render("PAUSED", True, WHITE)
        resume_text = self.small_font.render("Press SPACE to Resume", True, GRAY)
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        SCREEN.blit(pause_text, pause_rect)
        SCREEN.blit(resume_text, resume_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.state == GameState.MENU:
                        self.state = GameState.PLAYING
                    elif self.state == GameState.PLAYING:
                        self.state = GameState.PAUSED
                    elif self.state == GameState.PAUSED:
                        self.state = GameState.PLAYING
                elif event.key == pygame.K_ESCAPE:
                    self.state = GameState.MENU
                    self.left_score = 0
                    self.right_score = 0
                    self.ball.reset(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        return True

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            CLOCK.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = PongGame()
    game.run()
