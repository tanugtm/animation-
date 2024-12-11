import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Explosion Effect")

# Colors
BLACK = (0, 0, 0)

# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(2, 5)  # Random size for particles
        self.color = [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)]  # Random colors
        self.angle = random.uniform(0, 2 * math.pi)  # Random direction
        self.speed = random.uniform(2, 6)  # Random speed
        self.lifetime = 255  # Lifetime for fading effect

    def update(self):
        # Update position based on speed and direction
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        # Slow down the particle
        self.speed *= 0.95
        # Reduce lifetime for fading effect
        self.lifetime -= 5
        if self.lifetime < 0:
            self.lifetime = 0
        # Adjust color to fade out
        self.color[0] = max(0, self.color[0] - 5)
        self.color[1] = max(0, self.color[1] - 5)
        self.color[2] = max(0, self.color[2] - 5)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

# Create particles
def create_particles(x, y, num_particles=100):
    return [Particle(x, y) for _ in range(num_particles)]

# Simulation variables
particles = []
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Trigger explosion on spacebar press
                particles.extend(create_particles(random.randint(100, WIDTH-100), random.randint(100, HEIGHT-100)))  # Random explosion point.

    # Update particles
    for particle in particles:
        particle.update()

    # Remove particles that have faded out
    particles = [p for p in particles if p.lifetime > 0]

    # Clear screen
    screen.fill(BLACK)

    # Draw particles
    for particle in particles:
        particle.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
