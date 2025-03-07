import time
import random
import sys

# ANSI escape codes for colors
COLORS = [
    '\x1b[31m',  # Red
    '\x1b[32m',  # Green
    '\x1b[33m',  # Yellow
    '\x1b[34m',  # Blue
    '\x1b[35m',  # Magenta
    '\x1b[36m',  # Cyan
    '\x1b[91m',  # Bright Red
    '\x1b[92m',  # Bright Green
    '\x1b[93m',  # Bright Yellow
    '\x1b[94m',  # Bright Blue
    '\x1b[95m',  # Bright Magenta
    '\x1b[96m'   # Bright Cyan
]

# Reset color
RESET = '\x1b[0m'

def clear_screen():
    """Clear the terminal screen"""
    print('\x1b[2J\x1b[H', end='')

def create_flower():
    """Create a colorful flower pattern"""
    # Use different parts of the flower with varying colors
    colors = random.sample(COLORS, 5)
    
    art = [
        f"{colors[0]}     *     {RESET}",
        f"{colors[1]}   *   *   {RESET}",
        f"{colors[2]}  *     *  {RESET}",
        f"{colors[3]} *       * {RESET}",
        f"{colors[4]}***********{RESET}",
        f"{colors[0]}   *****    {RESET}",
        f"     Stem{colors[1]}||||    {RESET}",
        f"     Leaves{colors[2]} arb  {RESET}",
        f"           {RESET}"
    ]
    return art

def main():
    while True:
        clear_screen()
        
        # Generate and print the flower
        flower = create_flower()
        for line in flower:
            print(line)
        
        # Add some dynamic elements
        print(f"{random.choice(COLORS)}Bloom!{RESET}")
        
        # Pause before next iteration
        time.sleep(0.3)

if __name__ == "__main__":
    main()