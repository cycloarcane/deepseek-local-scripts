import time
import sys
import colorsys

# ASCII art (a simple rocket; customize this for different shapes)
ascii_art = r"""
    /\_/\  
   ( o o )
  / . . \ 
   \___/ 
    ^^ 
"""

def main():
    try:
        while True:
            elapsed_time = time.time()
            # Cycle hue every 1.5 seconds for smooth pulsation
            hue = (elapsed_time * 0.75) % 1.0
            # Convert hue to RGB with full saturation and brightness
            r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)
            
            # Clear screen and set color codes
            sys.stdout.write(f"\x1b[H\x1b[2J")  # ANSI clear screen command
            color_sequence = f"\x1b[38;2;{r};{g};{b}m"
            sys.stdout.write(color_sequence)
            sys.stdout.write(ascii_art)
            sys.stdout.write("\x1b[0m")  # Reset color
            sys.stdout.flush()
            time.sleep(0.05)  # Adjust speed here (smaller = faster)
    except KeyboardInterrupt:
        print("\x1b[0mAnimation Stopped: Press any key to exit...")
        sys.exit()

if __name__ == "__main__":
    main()