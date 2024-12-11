import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Fullscreen setup
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()

# Colors and fonts
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
FONT = pygame.font.Font(None, 60)

# Typing practice lines
PRACTICE_LINES = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "Waltz, nymph, for quick jigs vex Bud.",
    "Jack quietly moved up front and seized the big ball of wax.",
    "The five boxing wizards jump quickly.",
    "Python programming improves typing speed.",
    "Always practice to enhance your skills."
]

def render_text(screen, target_text, typed_text):
    """
    Render the typing line with user input:
    - Correctly typed text is displayed in green.
    - Incorrectly typed text is displayed in yellow.
    - Remaining text is displayed in white.
    """
    screen.fill(BLACK)
    x, y = WIDTH // 2 - 400, HEIGHT // 2  # Centered starting position for text
    for i, char in enumerate(target_text):
        if i < len(typed_text):  # User has typed this character
            if typed_text[i] == char:
                color = GREEN  # Correct
            else:
                color = YELLOW  # Incorrect
        else:
            color = WHITE  # Not yet typed
        char_surface = FONT.render(char, True, color)
        screen.blit(char_surface, (x, y))
        x += char_surface.get_width()  # Move position for the next character

    pygame.display.flip()

def typing_practice(screen, lines):
    """Interactive typing practice."""
    current_line = 0
    total_lines = len(lines)

    while current_line < total_lines:
        target_text = lines[current_line]
        typed_text = ""  # Initialize user input for the line
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:  # Handle backspace
                        typed_text = typed_text[:-1]
                    elif event.key == pygame.K_RETURN:  # Enter key moves to next line
                        if typed_text == target_text:  # Only proceed if the line is complete
                            running = False
                    else:
                        typed_text += event.unicode  # Add typed character

            # Render the current typing line
            render_text(screen, target_text, typed_text)

        # Move to the next line
        current_line += 1

        # Clear the screen for the next line
        screen.fill(BLACK)
        pygame.display.flip()

    # Display completion message
    render_text(screen, "Typing practice completed! Press Esc to exit.", "")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()

def main():
    """Main function to run the typing practice."""
    random.shuffle(PRACTICE_LINES)  # Randomize the order of lines
    typing_practice(screen, PRACTICE_LINES)
    pygame.quit()

if __name__ == "__main__":
    main()
