import time
import os
import math
from shutil import get_terminal_size

# Initialize terminal
os.system('')  # Enable ANSI colors
width, height = get_terminal_size()

# Color constants
COLORS = 16
PAUSE = 0.05

def get_color(r, g, b):
    """Convert RGB to ANSI escape code"""
    return f"\033[38;2;{r};{g};{b}m"

def animate():
    while True:
        t = time.time()
        frame = []
        for y in range(height-2):
            row = []
            for x in range(width):
                # Calculate color based on position and time
                hue = (x + y + t) * 0.1
                r = int(127 * math.sin(hue) + 128)
                g = int(127 * math.sin(hue + 2) + 128)
                b = int(127 * math.sin(hue + 4) + 128)
                
                # Create ANSI color code
                color = get_color(r, g, b)
                row.append(f"{color}█")
            frame.append(''.join(row))
        
        # Clear screen and print frame
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n'.join(frame), end='')
        
        time.sleep(PAUSE)

if __name__ == "__main__":
    try:
        print("Starting ASCII animation. Press Ctrl+C to stop.")
        animate()
    except KeyboardInterrupt:
        print("\033[0m\nAnimation stopped.")