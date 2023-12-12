import pygame
import sys
import random

# Inicijalizacija Pygame-a
pygame.init()

# Postavke prozora i kutije
width, height = 800, 600
box_size = 100

# Postavke kuglica
ball_radius = 10
balls = [{'x': random.randint(ball_radius, width - ball_radius),
          'y': random.randint(ball_radius, height - ball_radius),
          'dx': random.choice([-1, 1]),
          'dy': random.choice([-1, 1])}]

# Boje
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Postavljanje prozora
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulacija")

# Glavna petlja
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)

    for ball in balls:
        pygame.draw.circle(screen, black, (ball['x'], ball['y']), ball_radius)

    pygame.display.flip()

    # Provjera kolizija s rubom kutije
    for ball in balls:
        if ball['x'] - ball_radius <= 0 or ball['x'] + ball_radius >= width:
            balls.append({'x': ball['x'], 'y': ball['y'], 'dx': -ball['dx'], 'dy': ball['dy']})
        if ball['y'] - ball_radius <= 0 or ball['y'] + ball_radius >= height:
            balls.append({'x': ball['x'], 'y': ball['y'], 'dx': ball['dx'], 'dy': -ball['dy']})

    # Provjera kolizija među kuglicama
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            dist = ((balls[i]['x'] - balls[j]['x']) ** 2 + (balls[i]['y'] - balls[j]['y']) ** 2) ** 0.5
            if dist <= 2 * ball_radius:
                balls.pop(j)
                balls.pop(i)
                balls.append({'x': random.randint(ball_radius, width - ball_radius),
                              'y': random.randint(ball_radius, height - ball_radius),
                              'dx': random.choice([-1, 1]),
                              'dy': random.choice([-1, 1])})

    # Kretanje kuglica
    for ball in balls:
        ball['x'] += ball['dx']
        ball['y'] += ball['dy']

    # Postavljanje brzine simulacije
    pygame.time.Clock().tick(60)
