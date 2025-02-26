import sys
import time
import os
from colorama import init, Fore, Back

# Initialize colorama
init()

# Define ANSI colors for text and background
text_colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.YELLOW]
bg_colors = [Back.BLACK, Back.WHITE, Back.GREEN, Back.BLUE, Back.YELLOW]

# Get terminal size
rows, cols = os.get_terminal_size()

# Initialize position and movement variables
x, y = 0, 0
dx, dy = 1, 1  # Direction of movement
color_index = 0

try:
    while True:
        # Clear the terminal screen
        sys.stdout.write('\033[2J')
        sys.stdout.flush()
        
        # Calculate new color
        current_text_color = text_colors[color_index % len(text_colors)]
        current_bg_color = bg_colors[color_index % len(bg_colors)]
        
        # Create the ASCII art pattern
        # Example: Moving '@' symbol
        art = '@'  # You can make this more complex if needed
        row = current_text_color + current_bg_color + art
        
        # Calculate the position
        x_pos = x % cols
        y_pos = y % rows
        
        # Move the cursor to the new position
        sys.stdout.write(f'\033[{y_pos+1};{x_pos+1}H')
        sys.stdout.write(row)
        sys.stdout.flush()
        
        # Update position and color
        x += dx
        y += dy
        
        # Reverse direction if boundaries are hit
        if x >= cols - 1 or x <= 0:
            dx *= -1
        if y >= rows - 1 or y <= 0:
            dy *= -1
            
        color_index += 1
        
        # Wait before next iteration
        time.sleep(0.1)
        
except KeyboardInterrupt:
    # Cleanup on Ctrl+C
    print("\033[2J", end="")
    pass