import time
import sys
import os
import random

def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    except (OSError, AttributeError):
        return 80

def main():
    # Terminal width (columns)
    width = get_terminal_width()
    max_position = width - 2  # Leave space to prevent going off-screen
    
    # RGB color tuples for vibrant colors
    colors = [
        (255, 0, 0),       # Red
        (0, 255, 0),       # Green
        (0, 0, 255),       # Blue
        (255, 255, 0),     # Yellow
        (255, 0, 255),     # Magenta
        (0, 255, 255),     # Cyan
    ]
    
    current_pos = 0
    direction = 1  # 1=right, -1=left
    color_index = 0
    animation_delay = 0.1  # seconds between frames
    
    try:
        while True:
            # Prepare next position and handle boundaries
            new_pos = current_pos + direction
            if new_pos < 0 or new_pos > max_position:
                direction *= -1
                new_pos = current_pos + direction  # Apply corrected position
            
            current_pos = new_pos
            selected_color = colors[color_index % len(colors)]
            r, g, b = selected_color
            
            # Construct frame with color-coded ball
            sys.stdout.write('\r')  # Move cursor to start of line
            sys.stdout.write(' ' * width)  # Clear the line by overwriting with spaces
            sys.stdout.write('\r')  # Reset cursor
            
            # Apply color and draw ball
            color_code = f"\x1b[38;2;{r};{g};{b}m"
            frame = ' ' * current_pos + f"{color_code}RGBO\x1b[0m"  # 'RGBO' as a stroboscopic effect
            sys.stdout.write(frame)
            sys.stdout.flush()
            
            color_index +=1
            time.sleep(animation_delay)
    except KeyboardInterrupt:
        print("\nAnimation stopped by user.")
    
if __name__ == "__main__":
    main()