import time
import sys
import os

def main():
    colors = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 208, 226]  # List of terminal color codes
    color_index = 0

    try:
        while True:
            # Get terminal width dynamically
            width = os.get_terminal_size().columns
            max_x = width - 1

            # Bounce parameters
            x = 0
            direction = 1

            while True:
                # Clear current line and set position at the start
                sys.stdout.write('\r\033[K')

                # Format the ball's color and position
                current_color = colors[color_index % len(colors)]
                position_line = ' ' * x + f'\033[38;5;{current_color}mO\033[0m'
                position_line += ' ' * (max_x - x)

                # Write to terminal without newline
                sys.stdout.write(position_line)
                sys.stdout.flush()

                # Update position and direction
                x += direction
                if x == 0 or x == max_x:
                    direction *= -1
                    color_index += 1  # Next color on direction reversal

                time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nAnimation stopped. Exiting gracefully.")
        sys.exit(0)

if __name__ == "__main__":
    main()