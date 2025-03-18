import sys
import time
import colorsys

# Customizable ASCII art with color markers ('@' and '*' in this example)
ascii_art = [
    "   @@@@   ",
    "  @   @  ",
    " @@ * @@ ",
    "@       @",
    " @     @  ",
    "  @___@   "  # Add more lines to your design
]

def clear_terminal():
    """Move cursor to top and clear terminal screen."""
    sys.stdout.write('\033[H\033[J')
    sys.stdout.flush()

def rgb_color_code(r, g, b):
    """Return ANSI escape code for the given RGB values."""
    return f'\033[38;2;{r};{g};{b}m'

def render_frame(hue):
    """Generate and display a single frame of the animation."""
    # Color1 for '@', Color2 for '*' using different hues
    color1_hue = (hue + 0.0) % 1.0  # Primary color
    color2_hue = (hue + 0.333) % 1.0  # Complementary color
    
    r1, g1, b1 = [int(255 * c) for c in colorsys.hsv_to_rgb(color1_hue, 1.0, 1.0)]
    r2, g2, b2 = [int(255 * c) for c in colorsys.hsv_to_rgb(color2_hue, 1.0, 1.0)]
    
    color_at_symbol = rgb_color_code(r1, g1, b1)
    color_asterisk = rgb_color_code(r2, g2, b2)
    
    clear_terminal()
    for line in ascii_art:
        output = []
        for char in line:
            if char == '@':
                output.append(f"{color_at_symbol}{char}")
            elif char == '*':
                output.append(f"{color_asterisk}{char}")
            else:
                output.append(f"\033[0m{char}")  # Reset color for non-marker characters
        print(''.join(output) + "\033[0m")  # Reset after line end

def main():
    try:
        while True:
            time_now = time.time()
            hue = (time_now * 0.5) % 1.0  # Controls color cycle speed
            render_frame(hue)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Animation terminated.")
        sys.exit()

if __name__ == "__main__":
    main()