import sys
import time
import random
import shutil
from colorama import Fore, Back, Style, init
from figletpy import Figlet

init(autoreset=True)

def get_terminal_width():
    return shutil.get_terminal_size().columns

def generate_ascii_art(text):
    f = Figlet()
    return f.renderText(text).split('\n')

def apply_color_cycle(text_lines):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    colored_lines = []
    color_index = 0
    for line in text_lines:
        line = line.strip()
        if line:
            line_length = len(line) 
            color = colors[color_index % len(colors)]
            colored_line = color + line.ljust(get_terminal_width(), ' ')
            colored_lines.append(colored_line)
            color_index += 1
    return colored_lines

def display_dynamic_ascii(ascii_lines):
    terminal_width = get_terminal_width()
    offset = 0
    while True:
        try:
            # Generate random colors for each frame
            text_color = random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])
            back_color = random.choice([Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN])
            
            # Clear screen
            print(Style.RESET_ALL)
            
            # Generate randomly offset lines
            randomized_lines = []
            for line in ascii_lines:
                line = line.strip()
                if line:
                    # Add random offset to each line
                    random_offset = random.randint(0, terminal_width)
                    randomized_line = ' ' * random_offset + text_color + line
                    randomized_lines.append(randomized_line)
            
            # Display lines with backgrounds
            for line in randomized_lines:
                print(back_color + line)
            
            time.sleep(0.5)
        
        except KeyboardInterrupt:
            print(Style.RESET_ALL)
            break

def main():
    text = "ASCII ART"
    ascii_lines = generate_ascii_art(text)
    display_dynamic_ascii(ascii_lines)

if __name__ == "__main__":
    main()
</script_title>
Colorful Dynamic Terminal ASCII Art