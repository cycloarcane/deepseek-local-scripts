import random
import time

# ASCII art design
ascii_art = [
    "      /\___/\\       ",
    "     (/._.) //       ",
    "    /_\  ___/        ",
    "   //\\\\ //\\\\      "
]

# ANSI color codes
colors = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
    "\033[91m",  # Bright Red
    "\033[92m",  # Bright Green
    "\033[93m",  # Bright Yellow
    "\033[94m",  # Bright Blue
    "\033[95m",  # Bright Magenta
    "\033[96m"   # Bright Cyan
]

def clear_line():
    print("\033[2K", end="")  # Clear current line
    print("\033[1G", end="")  # Move to start of line

def animate():
    while True:
        # Randomly select colors for each line
        line_colors = [random.choice(colors) for _ in range(len(ascii_art))]
        
        # Print each line with corresponding color
        for i, line in enumerate(ascii_art):
            print(f"{line_colors[i]}{line}\033[0m")
        
        # Small delay between frames
        time.sleep(0.1)
        
        # Clear the lines
        for _ in range(len(ascii_art)):
            clear_line()

if __name__ == "__main__":
    try:
        animate()
    except KeyboardInterrupt:
        # Reset terminal colors on exit
        print("\033[0m")
        print("\nAnimation stopped.")