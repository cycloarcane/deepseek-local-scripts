import sys
import random
import time
from colorama import init, Fore, Back, Style

# Initialize colorama
init()

# Define the ASCII art (Smiley face)
ASCII_ART = [
    "   \\o/",
    "   :D",
    "   /o\\"
]

def clear_screen():
    """Clear the terminal screen."""
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

def random_color():
    """Return a random color from the available colors."""
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    return random.choice(colors)

def main():
    try:
        while True:
            # Clear screen
            clear_screen()
            
            # Randomize position
            x = random.randint(0, 30)
            y = random.randint(0, 30)
            
            # Randomize rotation
            rotation = random.choice([0, 1, 2])
            if rotation == 1:
                art = [" ".join(line[::-1]) for line in ASCII_ART]
            elif rotation == 2:
                art = [" ".join(line[::-1]) for line in reversed(ASCII_ART)]
            else:
                art = ASCII_ART
            
            # Apply random color
            color = random_color()
            
            # Print the art with colors
            print(Back.BLACK + color)
            for line in art:
                print(' ' * x + line)
            print(Style.RESET_ALL)
            
            # Control frame rate
            time.sleep(0.3)
            
    except KeyboardInterrupt:
        # Exit gracefully
        print("\nExiting the ASCII art generator. See you!")
        clear_screen()

if __name__ == "__main__":
    main()