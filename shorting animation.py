import pygame
import time
import random  # Import the random module

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Constants
FPS = 60
NUMBERS = list(range(1, 11))  # Numbers 1 to 10
BAR_WIDTH = WIDTH // len(NUMBERS)  # Width of each bar
FONT = pygame.font.Font(None, 50)

# Draw bars
def draw_bars(array, color_positions=None, algorithm_name=""):
    screen.fill(BLACK)

    max_height = max(array)  # Max value in the array for scaling heights
    for i, value in enumerate(array):
        bar_height = (value / max_height) * (HEIGHT - 100)  # Scale height
        color = BLUE
        if color_positions and i in color_positions:
            color = RED if color_positions[i] == "red" else GREEN
        pygame.draw.rect(
            screen,
            color,
            (i * BAR_WIDTH, HEIGHT - bar_height, BAR_WIDTH - 5, bar_height),
        )

    # Display the algorithm name
    text = FONT.render(algorithm_name, True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()

# Bubble Sort
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            draw_bars(array, {j: "red", j + 1: "red"}, "Bubble Sort")
            pygame.time.delay(200)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

# Insertion Sort
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            draw_bars(array, {j: "red", j + 1: "green"}, "Insertion Sort")
            pygame.time.delay(200)
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

# Selection Sort
def selection_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            draw_bars(array, {j: "red", min_idx: "green"}, "Selection Sort")
            pygame.time.delay(200)
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

# Merge Sort
def merge_sort(array):
    merge_sort_helper(array, 0, len(array) - 1)

def merge_sort_helper(array, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort_helper(array, left, mid)
        merge_sort_helper(array, mid + 1, right)
        merge(array, left, mid, right)

def merge(array, left, mid, right):
    left_part = array[left:mid + 1]
    right_part = array[mid + 1:right + 1]
    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        draw_bars(array, {k: "red"}, "Merge Sort")
        pygame.time.delay(200)
        if left_part[i] < right_part[j]:
            array[k] = left_part[i]
            i += 1
        else:
            array[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        draw_bars(array, {k: "red"}, "Merge Sort")
        pygame.time.delay(200)
        array[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        draw_bars(array, {k: "red"}, "Merge Sort")
        pygame.time.delay(200)
        array[k] = right_part[j]
        j += 1
        k += 1

# Quick Sort
def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)

def quick_sort_helper(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort_helper(array, low, pivot_index - 1)
        quick_sort_helper(array, pivot_index + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        draw_bars(array, {j: "red", high: "green"}, "Quick Sort")
        pygame.time.delay(200)
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

# Main function
def main():
    running = True

    while running:
        array = NUMBERS[:]  # Use numbers 1 to 10
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Sort using different algorithms
        algorithms = [bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort]
        for algorithm in algorithms:
            random.shuffle(array)  # Shuffle the array for each algorithm
            algorithm(array)
            time.sleep(1)  # Pause between algorithms

    pygame.quit()

if __name__ == "__main__":
    main()
