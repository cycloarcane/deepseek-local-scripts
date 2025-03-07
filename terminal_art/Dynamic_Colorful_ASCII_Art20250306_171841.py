import os
import time
from blessed import Terminal

def main():
    term = Terminal()
    os.system('clear')  # Clear terminal

    # Define ASCII art (change this to any ASCII art pattern you like)
    ascii_art = [
        "      ______      ",
        "    /      \\    ",
        "   /        \\   ",
        "  /          \\  ",
        " /            \\ ",
        "   ___      ___   ",
        "  /   |    |   \\  ",
        "  \\___|____|___/  ",
        "                  "
    ]

    # Define colors for each character (extend as needed)
    color_map = {
        ' ': 'white',
        '_': 'blue',
        '/': 'cyan',
        '\\': 'cyan',
        '[': 'yellow',
        ']': 'yellow',
        '-': 'green',
        '+': 'white',
        '=': 'red',
        'x': 'magenta'
    }

    # Function to draw ASCII art with colors
    def draw_art(rows, x=0, y=0):
        term.move(y, x)
        for row in rows:
            for char in row:
                color = color_map.get(char, 'white')
                term.color(color)
                print(char, end='')
            print()

    # Animation variables
    x = 0
    y = 5  # Starting vertical position
    direction = 1  # 1 for right, -1 for left
    speed = 0.05
    max_x = term.width - len(ascii_art[0])

    try:
        while True:
            term.clear()  # Clear screen
            draw_art(ascii_art, x, y)
            term.present()  # Update screen

            # Move art
            x += direction
            if x >= max_x or x <= 0:
                direction *= -1

            # Change colors (simple animation)
            color_map[' '] = 'bright_cyan' if time.time() % 1 < 0.5 else 'white'

            time.sleep(speed)

    except (KeyboardInterrupt, EOFError):
        print("\nExiting...")

    finally:
        term.exit()  # Clean up terminal

if __name__ == "__main__":
    main()