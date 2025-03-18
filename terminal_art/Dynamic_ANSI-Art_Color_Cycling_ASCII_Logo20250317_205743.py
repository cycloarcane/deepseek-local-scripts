import sys
import time
import random
import os
import colorsys
from colorama import init, Fore, Style
from pyfiglet import Figlet

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def random_font_selector(figlet_fonts):
    return random.choice(figlet_fonts)

def create_colorful_ascii_art():
    init()
    try:
        text = input("Enter your ASCII message: ").strip() or "Hello"
        available_fonts = Figlet().getFonts()
        while True:
            current_time = time.time() * 1.5  # Speed control

            # Font switch every 3 seconds
            font_change_interval = 3
            random_font = random_font_selector(available_fonts) if int(current_time) % int(font_change_interval) == 0 else None

            # Use consistent font across cycles but change occasionally
            current_font = random_font or "slant"
            figlet = Figlet(font=current_font)
            art = figlet.renderText(text)
            lines = art.split('\n')

            clear_terminal()
            base_hue = (current_time % 360)  # 0-360 hue cycle
            
            for line_num, line in enumerate(lines):
                if not line.strip():
                    continue  # Skip empty lines
                # Per-line colorization with shifted hue
                hue_offset = (line_num * 36) % 360
                final_hue = (base_hue + hue_offset) % 360
                
                # Convert to RGB values
                h = final_hue / 360
                r, g, b = [int(x*255) for x in colorsys.hsv_to_rgb(h, 1.0, 1.0)]

                color_code = f"\033[38;2;{r};{g};{b}m"
                reset_code = Style.RESET_ALL
                
                sys.stdout.write(color_code + line + reset_code + '\n')
            
            sys.stdout.flush()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nGoodbye! Aborted animation gracefully.")
    except Exception as e:
        print(f"Error: {str(e)}. Ensure you have 'pyfiglet' installed with: pip install pyfiglet")

if __name__ == "__main__":
    try:
        import pyfiglet
        create_colorful_ascii_art()
    except ImportError:
        print("Please install required package first:\n pip install pyfiglet")