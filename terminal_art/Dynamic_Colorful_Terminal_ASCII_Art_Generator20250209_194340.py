import sys
import time
import random
import math
from shutil import get_terminal_size

# Color codes for ANSI
colors = [
    '\033[31m',  # Red
    '\033[32m',  # Green
    '\033[33m',  # Yellow
    '\033[34m',  # Blue
    '\033[35m',  # Magenta
    '\033[36m',  # Cyan
    '\033[91m',  # Bright Red
    '\033[92m',  # Bright Green
    '\033[93m',  # Bright Yellow
    '\033[94m',  # Bright Blue
    '\033[95m',  # Bright Magenta
    '\033[96m'   # Bright Cyan
]

# Colors for the ASCII art
art_colors = ['\033[31m', '\033[33m', '\033[34m', '\033[35m']

# Get terminal size
cols, rows = get_terminal_size()

# Simple smiley face ASCII art
ascii_art = [
    "  ⢀⣀⣀⣀⣀⣀⣀⣀  ",
    " ⡴⠟⠻⠿⣿⡿⠛⠛⠛ ",
    " ⠄⢡⡅⡇⠀⠡⡇⠀ ",
    " ⡇⠉⠉⠉⢹⠇⠉⠉ ",
    " ⡇⠀⠀⠀⠂⠀⠈⠁ "
]

# Calculate the size of ASCII art
art_height = len(ascii_art)
art_width = max(len(line) for line in ascii_art)

def clear_screen():
    """Clear terminal screen"""
    sys.stdout.write('\033[2J\033[H')

def get_random_color():
    """Return a random ANSI color code"""
    return random.choice(colors)

def get_position(angle):
    """Calculate the position using sine wave"""
    return int(math.sin(angle) * (cols // 2 - art_width // 2)) + (cols // 2 - art_width // 2)

def print_frame(angle):
    """Print a single frame"""
    y_offset = get_position(angle)
    # Traverse each row of the screen
    for row in range(rows):
        # Build each row
        screen_row = []
        for col in range(cols):
            # Check if position is part of the ASCII art
            art_row = row - (rows // 2 - art_height // 2)
            art_col = col - y_offset
            if 0 <= art_row < art_height and 0 <= art_col < art_width:
                char = ascii_art[art_row][art_col]
                if char != ' ':
                    # Colorize the character
                    color = random.choice(art_colors)
                    screen_row.append(f"{color}{char}\033[0m")
                    continue
            # Background effect
            if random.random() < 0.3:
                screen_row.append(f"{get_random_color()}* \033[0m")
            else:
                screen_row.append('  ')
        # Print the row
        sys.stdout.write(''.join(screen_row))
        sys.stdout.write('\n')
    # Flush the output
    sys.stdout.flush()

def main():
    angle = 0
    while True:
        clear_screen()
        print_frame(angle)
        angle += 0.1  # Adjust speed here
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        sys.stdout.write('\033[0m')  # Reset colors
        print("Animation stopped.")