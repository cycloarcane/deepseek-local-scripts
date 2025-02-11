import os
import time

# ANSI color codes
colors = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
    "\033[37m"   # White
]

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows), int(columns)

def main():
    message = "WELCOME TO ASCII ART DEMO"
    rows, cols = get_terminal_size()
    x = 0
    color_index = 0
    animation_speed = 0.1  # Adjust speed as needed
    max_x = cols - len(message)
    max_y = rows - 3

    while True:
        clear_terminal()
        y = 0
        for line in range(3):
            print("\033c")  # Clear screen with ANSI
            for i, char in enumerate(message):
                # Calculate position
                current_x = (x + i) % cols
                # Create a gradient effect
                color = colors[color_index % len(colors)]
                print(f"\033[{y + 1};{current_x + 1}H{color}{char}\033[0m", end='')
            color_index += 1
            time.sleep(animation_speed)
            x += 1
            if x > max_x:
                x = 0
            y += 1

if __name__ == '__main__':
    main()