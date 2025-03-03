import sys
import time
from colorama import Fore, Style, init
import os

# Initialize colorama
init()

# Define terminal colors
colors = {
    'RED': Fore.RED,
    'GREEN': Fore.GREEN,
    'BLUE': Fore.BLUE,
    'CYAN': Fore.CYAN,
    'YELLOW': Fore.YELLOW,
    'WHITE': Fore.WHITE
}

def generate_ascii_art():
    """Generates rotating ASCII art"""
    ascii_art = [
        "  *", 
        " ***", 
        "*****",
        " ***", 
        "  *"
    ]
    return ascii_art

def clear_terminal():
    """Clears terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_ascii():
    """Handles the animation loop"""
    try:
        while True:
            # Get the ASCII art
            art = generate_ascii_art()
            
            # Cycle through colors
            for color in colors.values():
                # Clear screen
                clear_terminal()
                
                # Print with current color
                print(color)
                for line in art:
                    print(line.center(10))
                
                # Add delay
                time.sleep(0.1)
                
                # Reset style
                print(Style.RESET_ALL, end='')
                
            # Rotate the art
            art = art[1:] + [art[0]]
            
    except KeyboardInterrupt:
        print("\nExiting animation...")
        pass

def main():
    """Main execution function"""
    # Ensure terminal supports colors
    sys.stdout.reconfigure(encoding='utf-8')
    
    # Start animation
    animate_ascii()

if __name__ == "__main__":
    main()