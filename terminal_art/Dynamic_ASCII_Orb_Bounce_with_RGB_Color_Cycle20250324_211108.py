import sys
import time
import os

def get_terminal_width():
    """Get terminal width or default to 80 columns"""
    try:
        return os.get_terminal_size().columns
    except:
        return 80

def main():
    max_width = get_terminal_width()
    current_x = 0
    direction = 1  # Start moving right
    step = 0

    try:
        while True:
            # Calculate color values
            r = (step * 10) % 256
            g = (step * 17) % 256
            b = (step * 3) % 256

            # Create color codes
            color_code = f"\033[38;2;{r};{g};{b}m"
            reset_code = "\033[0m"
            ball = f"{color_code}O{reset_code}"

            # Clear current line
            sys.stdout.write('\033[2K\r')

            # Build frame
            frame = " " * current_x + ball + " " * (max_width - current_x - 1)
            sys.stdout.write(frame)
            sys.stdout.flush()

            # Update position and direction
            current_x += direction
            if current_x >= max_width - 1 or current_x <= 0:
                direction *= -1  # Reverse direction
            
            step += 1
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nStopping animation...")

if __name__ == "__main__":
    main()