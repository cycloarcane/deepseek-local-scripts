import time
from colorama import Fore, Back, Style, init
import sys

init(autoreset=True, wrap=True)

# Define the ASCII art (a star in this example)
ascii_art = """
         *****
      *           *
    *               *
  *                   *
  *                   *
   *               *
    *           *
      *     *
         *
"""

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

def main():
    current_frame = 0
    try:
        while True:
            # Clear the terminal and reset cursor position
            print('\033[2J\033[0;0H', end='')
            lines = ascii_art.splitlines()
            for line in lines:
                # Skip empty lines (e.g., empty strings from splitlines)
                if not line:
                    continue
                # Generate a colorful version of the current line
                colorful_line = []
                for i, char in enumerate(line):
                    # Calculate the color index based on position and frame
                    color_index = (i + current_frame) % len(colors)
                    colorful_line.append(colors[color_index] + char)
                # Print the line with a reset to avoid color bleed
                print(''.join(colorful_line) + Style.RESET_ALL)
            # Update frame counter and pause briefly for animation
            current_frame += 1
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(Style.RESET_ALL + "\nAnimation stopped.")
        sys.exit()

if __name__ == "__main__":
    main()