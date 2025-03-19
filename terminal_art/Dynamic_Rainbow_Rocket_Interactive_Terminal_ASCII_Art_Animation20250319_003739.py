import time
import shutil
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

COLORS = [
    "\033[91m",    # Red
    "\033[92m",    # Green
    "\033[93m",    # Yellow
    "\033[94m",    # Blue
    "\033[95m",    # Magenta
    "\033[96m",    # Cyan
    "\033[0m"      # Reset
]

rocket_art = [
    r"     ^..^",
    r"    /(o o)\",
    r"    \\\>  <",   # Needs proper escaping
    r"  /)     (\  =",  # More \
    r"   \"\"\"\"\""
]

def main():
    columns = shutil.get_terminal_size().columns
    idx = 0
    shift = 0
    try:
        while True:
            clear_screen()
            for i, line in enumerate(rocket_art):
                color = COLORS[(idx + i) % len(COLORS)]
                # Apply color to line only, not the leading spaces
                print(' ' * shift + color + line.strip() + '\033[0m')
            # Update parameters
            shift = (shift +1) % (columns - 20)  # Arbitrary buffer
            idx = (idx +1) % (len(COLORS)*2)      # cycle slower
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()