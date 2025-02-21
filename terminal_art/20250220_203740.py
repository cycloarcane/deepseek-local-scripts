import sys
import time
from random import randint
import curses

# Initialize the terminal and set up curses
def init_curses():
    stdscr = curses.initscr()
    curses.start_color()
    curses.use_default_colors()
    for i in range(curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    stdscr.nodelay(True)
    stdscr.clear()
    return stdscr

# Generate random color codes
def get_colors(count):
    colors = []
    for _ in range(count):
        colors.append(randint(0, curses.COLORS - 1))
    return colors

# Main animation loop
def animate(stdscr, ascii_art):
    rows, cols = stdscr.getmaxyx()
    color_cycle = 0
    max_color = 8

    while True:
        stdscr.clear()
        
        # Calculate color for each line
        colors = [(color_cycle + i) % max_color for i in range(len(ascii_art))]
        
        for i, line in enumerate(ascii_art):
            if i >= rows:
                break
            # Calculate offset based on animation progress
            offset = int((color_cycle % 20) * 2)
            displayed_line = line[offset:cols+offset]
            # Apply color
            stdscr.addstr(i, 0, displayed_line, curses.color_pair(colors[i] + 1))
        
        stdscr.refresh()
        time.sleep(0.1)
        color_cycle += 1
        
        # Check for exit condition
        if stdscr.getch() == ord('q'):
            break

# Clean up curses and restore terminal
def cleanup(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

# Define your ASCII art here
ascii_art = [
    "             _          ",
    "       _####  ####      ",
    "   _####          #### ",
    "  ####              ####",
    " ####                ####",
    "                    ####",
    "                    ####",
    "                    ####",
    "                    ####",
    "                    ####",
    "                    ####",
    "                    ####",
    "                    ####",
    "                    ####",
    "                    ####",
    "                    ####",
    "                    ####",
    "                    ####",
    "                    ####",
    "                      ####_       ",
    "                         ######    ",
    "                            ###    "
]

def main():
    stdscr = init_curses()
    try:
        animate(stdscr, ascii_art)
    except KeyboardInterrupt:
        pass
    finally:
        cleanup(stdscr)

if __name__ == "__main__":
    main()