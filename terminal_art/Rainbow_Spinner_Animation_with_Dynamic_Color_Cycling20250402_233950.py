import time
import sys

COLORS = [
    "\033[31m",  # Red
    "\033[33m",  # Yellow
    "\033[32m",  # Green
    "\033[36m",  # Cyan
    "\033[34m",  # Blue
    "\033[95m"   # Magenta
]
CHARACTERS = ['←', '↑', '→', '↓', ' guideline }

while True:
    for character in characters:
        print(f'\r{character_color_map[character]}', end='')
        sys.stdout.flush()
        time.sleep(0.5)  # Adjust animation speed
        
def print_line(char, color):
    sys.stdout.write(f'\r{color}{char}\033[0m')  # Reset color after printing
    sys.stdout.flush()

def main():
    try:
        frame = 0
        while True:
            for i in range(len(CHARACTERS)):
                char = CHARACTERS[i]
                color = COLORS[frame % len(COLORS)]
                sys.stdout.write(f'\r{color}{char}\033[0m')
                sys.stdout.flush()
                time.sleep(0.2)  # Adjust for animation speed
                frame += 1
    except KeyboardInterrupt:
        print("\nAnimation stopped.")
        
if __name__ == "__main__":
    main()