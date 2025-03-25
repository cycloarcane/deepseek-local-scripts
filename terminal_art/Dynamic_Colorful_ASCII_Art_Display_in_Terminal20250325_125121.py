import sys
import random
import time
import argparse
from pyfiglet import Figlet
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def colorize_chars(text, dynamic=True):
    result = []
    for c in text:
        if dynamic:
            color = random.randint(16, 255)
        else:
            color = random.randint(16, 255)
        colored_char = f"\x1b[38;5;{color}m{c}\x1b[0m"
        result.append(colored_char)
    return ''.join(result)

def main():
    parser = argparse.ArgumentParser(description="Generate colorful dynamic ASCII art.")
    parser.add_argument("text", help="The text to convert to ASCII art.")
    parser.add_argument("--dynamic", action="store_true", help="Enable animation.")
    parser.add_argument("--font", default="slant", help="Font style for the ASCII art.")
    args = parser.parse_args()
    
    text = args.text
    font_name = args.font
    dynamic = args.dynamic
    figlet = Figlet(font=font_name)
    
    if dynamic:
        try:
            while True:
                clear_screen()
                ascii_art = figlet.renderText(text)
                colored_art = colorize_chars(ascii_art, dynamic=True)
                print(colored_art)
                time.sleep(0.15)
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit()
    else:
        ascii_art = figlet.renderText(text)
        colored_art = colorize_chars(ascii_art, dynamic=False)
        print(colored_art)

if __name__ == "__main__":
    main()