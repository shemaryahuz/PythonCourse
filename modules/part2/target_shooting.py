import pygame
import random

# Defining constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 10
TARGET_RADIUS = 20
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Pygame startup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooting game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Creating the ball and the target
ball_x = 400
ball_y = 550
target_x = random.randint(50, 750)
target_y = random.randint(50, 450)
score = 0

#The game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.MOUSEMOTION:
        ball_x, ball_y = pygame.mouse.get_pos()

    #Collision test
    distance = ((ball_x - target_x)**2 + (ball_y - target_y)**2)**0.5
    if distance <= BALL_RADIUS + TARGET_RADIUS:
        score += 1
        target_x = random.randint(50, 750)
        target_y = random.randint(50, 450)

    #Screen drawing
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)
    pygame.draw.circle(screen, GREEN, (target_x, target_y), TARGET_RADIUS)

    #Displaying the score
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()