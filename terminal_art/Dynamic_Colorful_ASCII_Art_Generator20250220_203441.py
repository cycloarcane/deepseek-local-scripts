import random
import time
import sys
from itertools import cycle
from threading import Thread, Event

class ASCIIArtGenerator:
    def __init__(self):
        self._running = True
        self.ascii_chars = "@#%$&!?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.ascii_art = [
            " ██████  ",
            " ██  ██  ",
            " ██████  ",
            " ██      ",
            " ██      ",
            " ███████",
            " ███████",
            "          "
        ]
        
    def generate_color_code(self, r=None, g=None, b=None):
        return f"\033[38;2;{'255' if r is None else r};{'255' if g is None else g};{'255' if b is None else b}m"

    def clear_screen(self):
        print("\033[2J\033[H", end='')

    def print_ascii(self):
        colors = cycle(random.sample(range(256), 16))
        
        for line in self.ascii_art:
            print(self.generate_color_code(next(colors)), end='')
            print(''.join([random.choice(self.ascii_chars) for _ in range(8)]), end='')
            print("\033[0m")
        print("\033[0m")

def ascii_art_demo():
    art_generator = ASCIIArtGenerator()
    
    try:
        while True:
            art_generator.clear_screen()
            art_generator.print_ascii()
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
        
if __name__ == "__main__":
    ascii_art_demo()