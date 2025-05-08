import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 165, 0), (128, 0, 128)]

# Ball class
class Ball:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        self.x = random.randint(radius, WIDTH - radius)
        self.y = random.randint(radius, HEIGHT - radius)
        self.speed_x = random.choice([-3, -2, 2, 3])
        self.speed_y = random.choice([-3, -2, 2, 3])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.speed_x *= -1
        if self.y <= self.radius or self.y >= HEIGHT - self.radius:
            self.speed_y *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def is_clicked(self, mouse_pos):
        mx, my = mouse_pos
        dist = ((mx - self.x)**2 + (my - self.y)**2)**0.5
        return dist <= self.radius

    def speed_up(self, factor=1.5):
        self.speed_x *= factor
        self.speed_y *= factor

ball_sizes = [30, 40, 25, 35, 20]
balls = [Ball(radius, COLORS[i]) for i, radius in enumerate(ball_sizes)]

score = 0
font = pygame.font.SysFont(None, 40)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for ball in balls:
        ball.move()
        ball.draw(screen)

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls[:]:  # iterate over a copy
                if ball.is_clicked(pygame.mouse.get_pos()):
                    balls.remove(ball)
                    score += 1
                    # Speed up remaining balls
                    for other in balls:
                        other.speed_up()
                    break

    if not balls:
        end_text = font.render("All balls removed! Final Score: " + str(score), True, (0, 100, 0))
        screen.blit(end_text, (WIDTH // 2 - 200, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        break

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
