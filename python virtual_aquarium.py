import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and fullscreen mode
INFO = pygame.display.Info()
WIDTH, HEIGHT = INFO.current_w, INFO.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Virtual Aquarium")

# Colors
# Corrected Colors
WATER_BLUE = (0, 105, 148)  # No changes, it's valid
BUBBLE_COLOR = (173, 216, 230)  # No changes, it's valid
FISH_COLORS = [(255, 178, 0), (255, 68, 0), (255, 215, 0), (34, 139, 34), (70, 130, 180)]  # Valid RGB values
PLANT_COLOR = (34, 139, 34)  # No changes
PLANT_COLOR = (67, 186, 78)  # Corrected from (67, 986, 78)
GOLDFISH_COLOR = (255, 140, 0)  # No changes
STATE_FISH_COLOR = (50, 205, 50)  # No changes


# Fish and bubble parameters
FISH_COUNT = 50
GOLDFISH_COUNT = 9
BUBBLE_COUNT = 25
FPS = 70

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Draw plants
def draw_plants():
    for i in range(5):  # 5 plants across the screen
        plant_x = i * (WIDTH // 5) + random.randint(-50, 50)
        plant_y = HEIGHT - 50
        for j in range(5):  # 5 layers of plant leaves
            pygame.draw.ellipse(screen, PLANT_COLOR, (plant_x, plant_y - j * 20, 20, 40))

# Fish class
class Fish:
    def __init__(self, x=None, y=None, color=None, size=None, stationary=False):
        self.x = random.randint(50, WIDTH - 50) if x is None else x
        self.y = random.randint(50, HEIGHT - 50) if y is None else y
        self.size = random.randint(20, 50) if size is None else size
        self.color = random.choice(FISH_COLORS) if color is None else color
        self.speed_x = random.choice([-2, -1, 1, 2]) if not stationary else 0
        self.speed_y = random.choice([-2, -1, 1, 2]) if not stationary else 0
        self.direction = 1 if self.speed_x > 0 else -1  # 1 for right, -1 for left

    def move(self):
        if self.speed_x == 0 and self.speed_y == 0:  # Skip movement for stationary fish
            return
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off walls
        if self.x - self.size < 0 or self.x + self.size > WIDTH:
            self.speed_x *= -1
            self.direction *= -1  # Flip direction
        if self.y - self.size < 0 or self.y + self.size > HEIGHT:
            self.speed_y *= -1

    def draw(self, screen):
        # Draw the body of the fish
        pygame.draw.ellipse(screen, self.color, (self.x - self.size, self.y - self.size // 2, self.size * 2, self.size))
        # Draw the tail
        tail_x = self.x - self.size * self.direction
        tail_y = self.y
        pygame.draw.polygon(screen, self.color, [
            (tail_x, tail_y),
            (tail_x - self.size * self.direction, tail_y - self.size // 2),
            (tail_x - self.size * self.direction, tail_y + self.size // 2)
        ])

# Bubble class
class Bubble:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(HEIGHT, HEIGHT + 200)
        self.radius = random.randint(5, 15)
        self.speed = random.uniform(1, 3)

    def move(self):
        self.y -= self.speed
        # Reset bubble position if it goes off-screen
        if self.y + self.radius < 0:
            self.y = random.randint(HEIGHT, HEIGHT + 200)
            self.x = random.randint(0, WIDTH)

    def draw(self, screen):
        pygame.draw.circle(screen, BUBBLE_COLOR, (self.x, int(self.y)), self.radius, 1)

# Create fish and bubbles
fishes = [Fish() for _ in range(FISH_COUNT)]
goldfishes = [Fish(color=GOLDFISH_COLOR, size=random.randint(25, 40)) for _ in range(GOLDFISH_COUNT)]
state_fish = Fish(x=WIDTH // 2, y=HEIGHT - 120, color=STATE_FISH_COLOR, size=50, stationary=True)
bubbles = [Bubble() for _ in range(BUBBLE_COUNT)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Clear screen
    screen.fill(WATER_BLUE)

    # Draw plants
    draw_plants()

    # Move and draw bubbles
    for bubble in bubbles:
        bubble.move()
        bubble.draw(screen)

    # Move and draw fish
    for fish in fishes:
        fish.move()
        fish.draw(screen)

    # Draw goldfish
    for goldfish in goldfishes:
        goldfish.move()
        goldfish.draw(screen)

    # Draw state fish
    state_fish.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
