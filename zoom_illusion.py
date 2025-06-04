import pygame
import sys
import random

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Zoom Tunnel Illusion")
clock = pygame.time.Clock()

# Colors and center
white = (255, 255, 255)
black = (0, 0, 0)
center = (width // 2, height // 2)

# Circle settings
circles = []
max_radius = 800
speed = 5

# Main loop
while True:
    screen.fill(black)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Add new circle occasionally
    if random.random() < 0.1:
        circles.append(10)  # Start small

    # Update and draw circles
    new_circles = []
    for radius in circles:
        if radius < max_radius:
            pygame.draw.circle(screen, white, center, radius, 1)
            new_circles.append(radius + speed)
    circles = new_circles

    # Update display
    pygame.display.flip()
    clock.tick(60)
