import random
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

def generate_random_color():
    """Generate a random ANSI color code."""
    colors = [
        Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE
    ]
    return random.choice(colors)

def generate_ascii_art(size=10, pattern='square'):
    """Generate a random ASCII art of a given pattern."""
    if pattern == 'square':
        art = ('*' * size + '\n') * size
    elif pattern == 'triangle':
        for i in range(1, size + 1):
            art += (' ' * (size - i) + '*' * (2 * i - 1) + '\n')
    elif pattern == 'diamond':
        size //= 2
        for i in range(1, size + 1):
            art += (' ' * (size - i) + '*' * (2 * i - 1) + '\n')
        for i in range(size - 1, 0, -1):
            art += (' ' * (size - i) + '*' * (2 * i - 1) + '\n')
    else:
        art = ('*' * size + '\n') * size

    return art

def apply_colors(text):
    """Randomly apply colors to the text."""
    lines = text.split('\n')
    colorized_lines = []
    for line in lines:
        if len(line) > 0:
            color = generate_random_color()
            colorized_lines.append(color + line)
        else:
            colorized_lines.append(line)
    return '\n'.join(colorized_lines)

def main():
    pattern_options = ['square', 'triangle', 'diamond']
    pattern = random.choice(pattern_options)
    size = random.randint(3, 10)
    
    ascii_art = generate_ascii_art(size, pattern)
    colored_ascii_art = apply_colors(ascii_art)
    
    print(colored_ascii_art)

if __name__ == "__main__":
    main()