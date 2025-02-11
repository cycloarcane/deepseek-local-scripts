import random
import sys
import time
from shutil import get_terminal_size
from os import system

# ANSI color codes (FG)
colors = [
    '31',  # red
    '32',  # green
    '33',  # yellow
    '34',  # blue
    '35',  # magenta
    '36',  # cyan
    '37',  # white
]

# Terminal colors constants
ANSI_RESET = '\033[0m'
ANSI_COLOR = '\033[{}m'

# ASCII characters for art
ascii_chars = list('`~=-_+;><}{][)(|\\/?.,!@#$%^&*') 

def clear_screen():
    # Clear screen based on OS
    if sys.platform == 'win32':
        system('cls')
    else:
        system('clear')
        print('\033[2J', end='')  # Clear screen using ANSI

def get_random_color():
    return ANSI_COLOR.format(random.choice(colors))

def main():
    # Get terminal dimensions
    cols, _ = get_terminal_size()
    
    # Initialize grid - list of lists
    grid = []
    for _ in range(cols):
        # Random initial character
        grid.append([random.choice(ascii_chars) for _ in range(2)])
    
    try:
        while True:
            # Randomly generate each frame
            frame = []
            for i in range(cols):
                # Alternate between two layers
                if i % 2 == 0:
                    # First layer
                    char = random.choice(ascii_chars)
                    color_code = get_random_color()
                else:
                    # Second layer
                    char = random.choice(ascii_chars)
                    color_code = get_random_color()
                
                # Add to frame with color
                frame.append(f"{color_code}{char}{ANSI_RESET}")
            
            # Combine frame into a string and print
            print(''.join(frame))
            
            # Add slight delay for animation speed
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\nExiting ASCII art flow...")

if __name__ == "__main__":
    main()