import os
import sys
import time
import math
from random import randint

# Color utility functions
def color_code(r, g, b):
    """Convert RGB values to ANSI color code."""
    return f"\033[38;2;{r};{g};{b}m"

def sine_wave(phase, amplitude=100, frequency=0.01, offset=0):
    """Generate sine wave values for color transitions."""
    return math.sin(phase * frequency + offset) * amplitude + amplitude

# Terminal and animation configuration
TERMINAL_WIDTH = os.get_terminal_size().columns
TERMINAL_HEIGHT = os.get_terminal_size().height - 2  # Account for status line
GRID_SIZE = 20  # Width and height of the art grid
SPEED = 0.1  # Animation speed
BRIGHTNESS = 80  # Color intensity

# Initialize grid
grid = [[str(i) for i in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def main():
    """Main animation loop."""
    phase = 0
    while True:
        os.system('clear')  # Clear terminal
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                # Calculate color values using sine waves
                r = int(sine_wave(phase + x))
                g = int(sine_wave(phase + y + GRID_SIZE))
                b = int(sine_wave(phase + x + y + GRID_SIZE*2))
                
                # Ensure colors stay within valid range
                r = max(0, min(255, r + BRIGHTNESS))
                g = max(0, min(255, g + BRIGHTNESS))
                b = max(0, min(255, b + BRIGHTNESS))
                
                # Print colored character
                print(f"{color_code(r, g, b)}{grid[y][x]}", end='')
            print("\033[0m\n", end='')  # Reset color and new line
        phase += 1
        time.sleep(SPEED)

if __name__ == "__main__":
    main()