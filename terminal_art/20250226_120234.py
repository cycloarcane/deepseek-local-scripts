import os
import sys
import time
from colorama import Fore, Back, Style, init
from random import randint

# Initialize colorama
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class ColorCycle:
    def __init__(self):
        self.colors = [
            Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, 
            Fore.MAGENTA, Fore.CYAN, Fore.WHITE
        ]
        self.current = 0
        
    def next(self):
        self.current = (self.current + 1) % len(self.colors)
        return self.colors[self.current]

def main():
    try:
        clear_screen()
        color_cycle = ColorCycle()
        ascii_art = [
            "         ___________         ",
            "        /         \\        ",
            "       |           |       ",
            "       |           |       ",
            "       |           |       ",
            "       \\___________/       ",
            "          \\     /          ",
            "           \\___/           ",
            "            /\    \\        ",
            "           /  \    /        ",
            "          /    \  /         ",
            "         /      \/          "
        ]
        
        while True:
            # Clear screen but keep the last frame for transition
            clear_screen()
            
            # Create color variations
            for i in range(len(ascii_art)):
                if i == len(ascii_art)-1:
                    # Last line changes color fully
                    current_color = color_cycle.next()
                    line = current_color + ascii_art[i] + Style.RESET_ALL
                else:
                    # Mix colors for other lines
                    part1 = Fore.RED + ascii_art[i][:len(ascii_art[i])//2]
                    part2 = Back.GREEN + ascii_art[i][len(ascii_art[i])//2:]
                    line = part1 + part2 + Style.RESET_ALL
                    
                print(line)
                time.sleep(0.1)
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nExiting gracefully...")
    finally:
        # Reset terminal colors
        print(Style.RESET_ALL)
        clear_screen()

if __name__ == "__main__":
    main()