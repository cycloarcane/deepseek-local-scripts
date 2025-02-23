import sys
import random
import time
import shutil
import os
import keyboard

from colorama import init, Fore, Back

init()

# Terminal dimensions
ROWS, COLS = shutil.get_terminal_size()

# Colors
 COLORS = [
    Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE,
    Fore.MAGENTA, Fore.CYAN, Fore.WHITE,
    Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW,
    Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE
]

# Shapes
SHAPES = ['█', '▒', '▓', '*', '●', '■', '□', 'MessageType']

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def handle_resize(sig, frame):
    global ROWS, COLS
    ROWS, COLS = shutil.get_terminal_size()

def draw_shape(x, y, shape, color):
    sys.stdout.write(f"\033[{y};{x}H{color}{shape}")

def random_position():
    return random.randint(0, COLS-1), random.randint(0, ROWS-1)

def random_color():
    return random.choice(COLORS)

def main():
    clear_screen()
    print("Press any key to stop the animation...", end='')
    
    keyboard.start.listener()
    
    while True:
        if keyboard.is_pressed('any_key'):
            break
            
        # Generate random shapes
        for _ in range(100):
            x, y = random_position()
            color = random_color()
            shape = random.choice(SHAPES)
            
            draw_shape(x, y, shape, color)
        
        time.sleep(0.1)
    
    clear_screen()
    print("Animation stopped")

if __name__ == "__main__":
    main()