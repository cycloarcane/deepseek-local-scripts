import sys
import time
import random
from curses import wrapper

# Load your ASCII art here
ascii_art = [
    "███████╗███████╗███████╗████████╗    ██╗     ██╗     ███╗   ███╗",
    "██╔════╝██╔════╝██╔════╝╚══██╔══╝    ██║     ██║     ████╗ ████║",
    "█████╗  █████╗  ███████╗   ██║       ██║     ██║     ██╔████╔██║",
    "██╔══╝  ██╔══╝  ╚════██║   ██║       ██║     ██║     ██║╚██╔╝██║",
    "███████╗███████╗███████║   ██║       ███████╗███████╗██║ ╚═╝ ██║",
    "╚══════╝╚══════╝╚══════╝   ╚═╝       ╚══════╝╚══════╝╚═╝     ╚═╝"
]

character_colors = {
    '█': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
    ' ': (0, 0, 0)
}

def main(stdscr):
    stdscr.nodelay(True)
    stdscr.timeout(100)
    
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.bkgd(curses.color_pair(1))
    
    while True:
        try:
            stdscr.clear()
            
            # Center the art horizontally and vertically
            max_y, max_x = stdscr.getmaxyx()
            art_height = len(ascii_art)
            art_width = max(len(line) for line in ascii_art) if art_height > 0 else 0
            
            # Generate color pairs
            for i, line in enumerate(ascii_art):
                y = int(max_y/2 - art_height/2) + i
                for j, char in enumerate(line):
                    x = int(max_x/2 - art_width/2) + j
                    if char == ' ':
                        stdscr.addstr(y, x, char)
                        continue
                    color = character_colors.get(char, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                    # Convert RGB to curses-compatible color
                    # ...
                    stdscr.addstr(y, x, char)
                    
            stdscr.refresh()
            time.sleep(0.1)
        except KeyboardInterrupt:
            break
        except:
            pass
            
    curses.endwin()

if __name__ == "__main__":
    wrapper(main)