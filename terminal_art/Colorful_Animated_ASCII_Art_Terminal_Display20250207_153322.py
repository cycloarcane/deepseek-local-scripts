import colorama
from colorama import Fore, Back, Style
import os
import time
import random

colorama.init(autoreset=True)

# List of available colors
colors = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE,
    Fore.MAGENTA, Fore.CYAN, Fore.WHITE
]

# ASCII art (replace with your own)
ascii_art = """
_________          ___.                  _________.____    __
\_   _____/ ______  \_ |__   ___________ \_   _____/__. \  |__|
 |    __)_ /  ___/   | __|  \_  __ \__  \ |    __)_|   |  |  |
 |        \\___ \    | \  |  | |  | | |  \ |        |   |  |  |
 /_______  /____  >  |___|  | |  | | |  / /_______  >   |  |__|
         \/     \/           \__| /____/          \/    \______
"""

def generate_color_art():
    lines = ascii_art.split('\n')
    for line in lines:
        # Randomly choose a color for each line
        color = random.choice(colors)
        print(f"{color}{line}")
        
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_terminal()
        generate_color_art()
        time.sleep(0.5)  # Adjust refresh rate here

if __name__ == "__main__":
    print("Starting colorful ASCII art animation...")
    print("Press Ctrl+C to stop")
    main()