import time, os, random
from colorama import init, Fore, Style

init(autoreset=True)

columns = os.get_terminal_size().columns
rows = os.get_terminal_size().rows

x, y = columns // 2, rows // 2
dx, dy = 1, 1
colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

try:
    while True:
        # Clear screen using ANSI escape code
        print('\033[2J', end='', flush=True)
        
        # Update position with boundary checks for x
        new_x = x + dx
        if new_x < 0 or new_x > columns - 1:
            dx *= -1
            new_x = x + dx  # Re-calculate after reversing direction
        # Vertical position
        new_y = y + dy
        if new_y < 0 or new_y > rows - 1:
            dy *= -1
            new_y = y + dy
        
        # Choose random color and update coordinates
        color = random.choice(colors)
        x, y = new_x, new_y
        
        # Position cursor and print character with styling
        print(f'\x1b[{y + 1};{x + 1}H{color}O{Style.RESET_ALL}', end='', flush=True)
        
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("Animation stopped.")