import os
import time

def main():
    cols = os.get_terminal_size().columns
    rows = os.get_terminal_size().lines

    # Ball initial position and velocity
    x, y = cols // 2, rows // 2
    vx, vy = 1, 1

    # Color palette using ANSI escape codes
    colors = [
        "\033[31m",  # Red
        "\033[32m",  # Green
        "\033[33m",  # Yellow
        "\033[34m",  # Blue
        "\033[35m",  # Magenta
        "\033[36m",  # Cyan
    ]
    color_index = 0

    try:
        while True:
            # Clear screen and reset cursor position
            print('\033[2J\033[H', end='')
            
            # Calculate next position
            new_x = x + vx
            new_y = y + vy

            # Handle horizontal boundaries
            if new_x < 0:
                new_x = 0
                vx = -vx
            elif new_x >= cols - 1:
                new_x = cols - 1
                vx = -vx

            # Handle vertical boundaries
            if new_y < 0:
                new_y = 0
                vy = -vy
            elif new_y >= rows - 1:
                new_y = rows - 1
                vy = -vy

            # Update coordinates
            x, y = new_x, new_y

            # Select color and render the ball
            current_color = colors[color_index % len(colors)]
            color_index += 1
            cursor_position = f"\x1b[{new_y+1};{new_x+1}H"
            print(f"{cursor_position}{current_color}●\033[0m", end='')

            # Pause for next frame (adjust speed here)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nAnimation stopped.")

if __name__ == "__main__":
    main()