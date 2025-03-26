import os
import sys
import time
import random

def clear_screen():
    """Clear the terminal screen based on OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_ascii_art(ascii_lines, colors, delay=0.3):
    """
    Display an animated ASCII art with shifting colors.
    
    :param ascii_lines: List of strings for each line of the art
    :param colors: List of ANSI color codes
    :param delay: Frame delay in seconds
    """
    try:
        frame = 0
        while True:
            clear_screen()
            for idx, line in enumerate(ascii_lines):
                # Cycle colors using current frame + line index
                color_idx = (frame + idx) % len(colors)
                color = colors[color_idx]
                # Apply color to the line and reset after
                print(f"{color}{line}\x1b[0m")
            sys.stdout.flush()
            time.sleep(delay)
            frame += 1
    except KeyboardInterrupt:
        clear_screen()
        print("Animation stopped.")

# Example ASCII art: Christmas Tree
ASCII_TREE = [
    "         *         ",
    "        ***        ",
    "       *****       ",
    "      *******      ",
    "     *********     ",
    "    ***********    ",
    "   *************   ",
    "    ***********    ",
    "       ###TRUNK### "
]

# Color palette using vibrant RGB values
COLORS = [
    "\x1b[38;2;255;0;0m",    # Red
    "\x1b[38;2;255;255;0m",  # Yellow
    "\x1b[38;2;0;255;0m",    # Green
    "\x1b[38;2;0;0;255m",    # Blue
    "\x1b[38;2;128;0;128m",  # Purple
    "\x1b[38;2;0;255;255m"   # Cyan
]

if __name__ == "__main__":
    print("Starting colorful ASCII animation. Press Ctrl+C to stop.")
    animate_ascii_art(ASCII_TREE, COLORS)