import os
import math
import time
from shutil import get_terminal_size

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    colors = [
        196,  # Bright Red
        202,  # Bright Green
        208,  # Bright Blue
        226,  # Pink
        45,   # Turquoise
        12    # Yellow
    ]
    term_size = get_terminal_size()
    screen_width = term_size.columns
    screen_height = term_size.lines

    # Center coordinates of the terminal
    cx = screen_width // 2
    cy = screen_height // 2
    rotation_angle = 0.0  # Initial rotation angle (in radians)

    while True:
        clear_screen()

        radius = 15  # Star size

        for theta in range(0, 360, 15):  # Generate 24 points for smoother rotation
            # Calculate the current star point's angle
            angle = math.radians(theta) + rotation_angle

            # Calculate coordinates
            x = int(cx + radius * math.cos(angle))
            y = int(cy + radius * math.sin(angle))

            # Check if the coordinates are within the terminal bounds
            if 0 <= y < screen_height and 0 <= x < screen_width:
                # Calculate color index using theta and rotation phase for dynamic colorflow
                index = (int((theta / 15) + (rotation_angle * 100))) % len(colors)
                color_code = colors[index]

                # Move cursor and set color for the character
                print(f'\x1b[{y+1};{x+1}H', end='')
                print(f'\x1b[38;5;{color_code}m*', end='')

        # Reset color after all characters have been displayed
        print('\x1b[0m', end='')

        # Update rotation angle and sleep for smooth animation
        rotation_angle += math.radians(0.5)
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...", end=' ')
        clear_screen()
        print("Goodbye!")