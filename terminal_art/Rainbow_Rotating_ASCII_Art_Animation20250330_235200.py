import sys
import time
import os
from colorsys import hsv_to_rgb

def get_ansi_color(r: int, g: int, b: int) -> str:
    return f"\x1b[38;2;{r};{g};{b}m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

ASCII_ART = r"""
   @ @
 @@@@@@ 
 @@@@@@@ 
 @@@@@@@   
 @@@@@@@
 @@@@@@
  @@@@
"""

def main():
    delay = 0.05  # Seconds between frames; smaller for faster animation
    art = ASCII_ART.strip().split('\n')
    rows = len(art)
    angle_step_per_row = 360.0 / rows
    try:
        current_angle = 0.0
        while True:
            clear_screen()
            out_lines = []
            for row_idx in range(rows):
                row = art[row_idx]
                # Calculate hue for this row
                row_angle = (current_angle + row_idx * angle_step_per_row) % 360.0
                hue = row_angle / 360.0
                # Convert to RGB (full saturation and value)
                r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]
                color_code = get_ansi_color(r, g, b)
                out_line = f"{color_code}{row}\x1b[0m"  # Reset color after row
                out_lines.append(out_line)
            print('\n'.join(out_lines))
            current_angle = (current_angle + 1.0) % 360.0  # Increment angle
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nAnimation stopped.")
        sys.exit(0)

if __name__ == "__main__":
    main()