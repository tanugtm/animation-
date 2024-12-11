import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and constants
WIDTH, HEIGHT = 1200, 800  # Fullscreen size
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption("Solar System Animation")

# Constants
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2  # Center of the screen
SUN_RADIUS = 50  # Radius of the sun
FPS = 60

# Colors
BLACK = (0, 0, 0)
SUN_COLOR = (255, 255, 0)
PLANET_COLORS = [
    (255, 165, 0),   # Mercury (orange-brown)
    (255, 255, 255), # Venus (white)
    (0, 0, 255),     # Earth (blue)
    (255, 0, 0),     # Mars (red)
    (255, 255, 0),   # Jupiter (yellow)
    (0, 255, 255),   # Saturn (cyan)
    (0, 255, 0),     # Uranus (green)
    (128, 0, 128)    # Neptune (purple)
]
PLANET_SIZES = [8, 10, 12, 10, 18, 16, 14, 12]  # Sizes of the planets
ORBITAL_SPEEDS = [0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.02, 0.015]  # Orbital speeds for each planet

# Initialize the clock
clock = pygame.time.Clock()

# Function to create a starry background
def create_starry_background(screen, num_stars=200):
    for _ in range(num_stars):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)

# Function to calculate planet positions
def calculate_position(angle, radius):
    x = CENTER_X + int(radius * math.cos(math.radians(angle)))
    y = CENTER_Y + int(radius * math.sin(math.radians(angle)))
    return x, y

# Main loop
running = True
angle = [0] * len(PLANET_COLORS)  # Starting angles for each planet

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with the starry background
    screen.fill(BLACK)
    create_starry_background(screen)

    # Draw the sun
    pygame.draw.circle(screen, SUN_COLOR, (CENTER_X, CENTER_Y), SUN_RADIUS)

    # Update and draw the planets
    for i in range(len(PLANET_COLORS)):
        angle[i] += ORBITAL_SPEEDS[i]  # Increase the angle to simulate orbital movement
        if angle[i] >= 360:
            angle[i] = 0

        # Calculate the radius with increased gap
        radius = (i + 1) * 70  # Different radii with more space between orbits

        # Calculate position for each planet
        x, y = calculate_position(angle[i], radius)

        # Draw the planet
        pygame.draw.circle(screen, PLANET_COLORS[i], (x, y), PLANET_SIZES[i])

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
