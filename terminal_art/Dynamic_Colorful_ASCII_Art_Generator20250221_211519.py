import sys
import random
import time
from colorama import init, Fore, Back, Style

# Initialize colorama
init()

def print_colored_ascii(text, color=Fore.WHITE):
    """Print colored ASCII art with random color changes"""
    # Convert text to ASCII art
    try:
        ascii_art = art.text(text, font='big')
    except:
        print("Error: Invalid character or font")
        return
    
    # Add random color transitions
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    for line in ascii_art.split('\n'):
        # Randomize color for each line
        line_color = random.choice(colors)
        # Print line with color
        print(line_color + line)
        # Small delay for animation effect
        time.sleep(0.1)
    
    # Reset color
    print(Style.RESET_ALL)

def main():
    # Get user input
    while True:
        try:
            text = input("Enter text for ASCII art (or 'exit' to quit): ")
            if text.lower() == 'exit':
                break
            # Generate and print colored ASCII art
            print_colored_ascii(text)
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()