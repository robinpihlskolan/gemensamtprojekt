import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 165, 0), (128, 0, 128)]

class Ball:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        self.x = random.randint(radius, WIDTH - radius)
        self.y = random.randint(radius, HEIGHT - radius)
        self.speed_x = random.choice([-3, -2, 2, 3])
        self.speed_y = random.choice([-3, -2, 2, 3])



score = 0
font = pygame.font.SysFont(None, 40)

clock = pygame.time.Clock()


running = True
while running:
    screen.fill(WHITE)



    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if ball.is_clicked(pygame.mouse.get_pos()):
                    score += 1
                    ball.relocate()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()