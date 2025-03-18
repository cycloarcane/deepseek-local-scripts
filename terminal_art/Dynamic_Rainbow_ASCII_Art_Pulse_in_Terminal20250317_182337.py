import sys
import time
import math

ASCII_ART = r"""
   _\/_
  /    \
 /      \
 \      /
  \____/
  (o o)
  \_V_/
"""

def main():
    frame = 0
    while True:
        # Clear the terminal screen and move the cursor to the top-left
        sys.stdout.write('\x1b[2J\x1b[H')
        sys.stdout.flush()
        
        # Calculate RGB values for smooth color transitions
        angle = frame / 10.0  # Control the animation speed with division value
        r = int(127 * (math.sin(angle) + 1))
        g = int(127 * (math.sin(angle + 2 * math.pi / 3) + 1))
        b = int(127 * (math.sin(angle + 4 * math.pi / 3) + 1))
        
        # Apply color codes to the ASCII art and reset afterward
        colored_art = f"\x1b[38;2;{r};{g};{b}m{ASCII_ART}\x1b[0m"
        sys.stdout.write(colored_art)
        sys.stdout.flush()
        
        frame += 1
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write('\x1b[0m')  # Reset color before exit
        print("\nAnimation stopped.")
        sys.exit()