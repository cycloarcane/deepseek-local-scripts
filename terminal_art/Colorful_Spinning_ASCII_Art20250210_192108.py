import time
from colorama import Fore, init
import os
import keyboard

# Initialize colorama
init()

# List of colors to cycle through
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.WHITE]

# ASCII segments for the spinning wheel
wheel = [
    "         ▄ tank fasting fit         ",
    "        ▄▄            ▄         ",
    "       ▄▄▄        ▄▄      ▄      ",
    "      ▄▄▄▄      ▄▄      ▄▄      ",
    "     ▄▄▄▄▄    ▄▄        ▄▄      ",
    "    ▄▄▄▄▄▄  ▄▄          ▄▄     ",
    "   ▄▄▄▄▄▄▄ ▄▄            ▄▄    ",
    "  ▄▄▄▄▄▄▄▄▄             ▄▄    ",
    " ▄▄▄▄▄▄▄▄▄▄            ▄▄     ",
    " ▄▄▄▄▄▄▄▄▄▄            ▄▄     ",
    " ▄▄▄▄▄▄▄▄▄            ▄▄      ",
    " ▄▄▄▄▄▄▄            ▄      ",
    " ▄▄▄▄          ▄      ▄     ",
    " ▄▄        ▄          ▄    ",
    " ▄         ▄            ▄   ",
    "           ▄            ▄   ",
    "            ▄▄         ▄    ",
    "             ▄▄▄      ▄     ",
    "               ▄▄▄▄ ▄      ",
    "                 ▄⎡ МК ДЕТИ ⎣▄   ",
    "                          ▄▄  ",
    "                        ▄▄     ",
    "                      ▄▄        ",
    "                    ▄▄           ",
    "                  ▄              ",
    "                                  ",
    "                                  ",
    "                                  ",
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate():
    color_index = 0
    shift = 0
    while True:
        clear_screen()
        color = colors[color_index % len(colors)]
        for segment in wheel:
            # Add some shifting pattern
            shifted_segment = segment[shift:] + segment[:shift]
            print(color + shifted_segment)
        print(Fore.WHITE + " PRESS ESC TO EXIT ")  # Static text
        print(colors[color_index % len(colors)] + " (≧◡≦)" )  # Smiley face
        time.sleep(0.1)
        
        # Update variables for next frame
        color_index += 1
        shift = (shift + 1) % 20  # Length of the segments
        
        # Handle exit condition
        if keyboard.is_pressed('esc'):
            break

if __name__ == "__main__":
    try:
        print(Fore.WHITE + "Starting ASCII animation. Press ESC to exit...")
        animate()
    except KeyboardInterrupt:
        print(Fore.WHITE + "\nAnimation stopped.")
        exit()