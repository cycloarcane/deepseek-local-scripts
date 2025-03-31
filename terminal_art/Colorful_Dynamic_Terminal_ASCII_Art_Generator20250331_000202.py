import random
import shutil
import os
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Get the terminal size
terminal_size = shutil.get_terminal_size()
WIDTH, HEIGHT = terminal_size.columns, terminal_size.lines - 2  # Reserving a line for user interaction

def generate_color():
    """Generate a random color from colorama library."""
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    return random.choice(colors)

def generate_shape():
    """Generate a random shape."""
    shapes = ['square', 'triangle', 'circle']
    return random.choice(shapes)

def draw_square(size):
    """Draw a colorful square."""
    color = generate_color()
    for i in range(size):
        print(color + '█' * size)

def draw_triangle(height):
    """Draw a colorful triangle."""
    color = generate_color()
    for i in range(height):
        print((color + '█') * (i + 1))

def draw_circle(radius):
    """Draw a colorful circle using ASCII art."""
    color = generate_color()
    diameter = radius * 2
    for y in range(-radius, radius):
        for x in range(-radius, radius):
            if (x**2 + y**2) <= radius**2:
                print(color + '█', end='')
            else:
                print(' ', end='')
        print()

def get_user_input():
    """Get user input for shape type, color, and size."""
    # Display available options to the user
    print("Available Shapes: square, triangle, circle")
    shape = input(f"Enter shape type ('{', '.join(['square', 'triangle', 'circle'])}'): ").strip().lower()
    if shape not in ['square', 'triangle', 'circle']:
        print("Invalid shape entered. Defaulting to random shape.")
        shape = generate_shape()

    size = input(f"Enter size (1-{max(WIDTH, HEIGHT)-1}) or 'random': ").strip().lower()
    try:
        size = int(size)
        if size < 1 or size > max(WIDTH, HEIGHT) - 1:
            size = random.randint(1, max(WIDTH, HEIGHT) - 1)
    except ValueError:
        size = random.randint(1, max(WIDTH, HEIGHT) - 1)

    # Generate and draw the selected shape
    if shape == 'square':
        draw_square(size)
    elif shape == 'triangle':
        draw_triangle(size)
    elif shape == 'circle':
        draw_circle(size)

def main():
    print(f"Colorful Dynamic Terminal ASCII Art Generator - Terminal Size: {WIDTH}x{HEIGHT}")
    print("Press Enter to continue...")
    input()  # Wait for user input to start
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
    get_user_input()

if __name__ == "__main__":
    main()