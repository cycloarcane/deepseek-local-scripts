import time
import sys
import os
from colorsys import hls_to_rgb

def main():
    current_x = 0
    direction = 1  # moving right initially
    while True:
        cols, rows = os.get_terminal_size()
        y = rows // 2

        sys.stdout.write("\033[H\033[J")  # Clear screen

        # Compute color based on current position
        h = current_x / (cols - 1) if cols > 1 else 0.0
        h %= 1.0  # Ensure within 0-1 range
        r, g, b = hls_to_rgb(h, 0.5, 1.0)
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)
        color = f"\033[38;2;{r};{g};{b}m"

        # Draw the star
        sys.stdout.write(f"\033[{y};{current_x}H{color}*")
        sys.stdout.write(f"\033[0m")  # Reset color
        sys.stdout.flush()

        # Update position for next frame
        new_x = current_x + direction

        if new_x <= 0 or new_x >= cols:
            direction *= -1
            new_x = current_x + direction  # recalculate with new direction
        current_x = new_x

        # Wait before next frame
        time.sleep(0.1)

if __name__ == "__main__":
    main()