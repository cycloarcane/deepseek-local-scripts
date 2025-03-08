import time

# ASCII artwork to display (a simple box shape)
ascii_art = r"""
       _____
    ,-')
   /    \
  /______\
 /        \
 \________/
"""

# Function to convert hue (0-360) to RGB values for ANSI color codes
def hsl_to_rgb(h, s=100, l=50):
    h %= 360
    s /= 100.0
    l /= 100.0

    c = (1 - abs(2 * l - 1)) * s
    h_prime = h / 60
    x = c * (1 - abs(h_prime % 2 - 1))
    m = l - c / 2

    # Select RGB components based on hue sector
    if 0 <= h_prime < 1:
        r, g, b = c, x, 0
    elif 1 <= h_prime < 2:
        r, g, b = x, c, 0
    elif 2 <= h_prime < 3:
        r, g, b = 0, c, x
    elif 3 <= h_prime < 4:
        r, g, b = 0, x, c
    elif 4 <= h_prime < 5:
        r, g, b = x, 0, c
    elif 5 <= h_prime < 6:
        r, g, b = c, 0, x
    else:
        r, g, b = 0, 0, 0

    # Calculate final RGB values (0-255)
    r_val = int((r + m) * 255)
    g_val = int((g + m) * 255)
    b_val = int((b + m) * 255)
    return (r_val, g_val, b_val)

def main():
    current_angle = 0.0
    step = 2.0  # Angle increment per iteration (degrees)
    try:
        while True:
            # Calculate current color
            r, g, b = hsl_to_rgb(current_angle, 100, 50)
            color_code = f"\033[38;2;{r};{g};{b}m"
            reset_code = "\033[0m"

            # Clear screen and move cursor to top-left
            print("\033[2J\033[1;1H", end="")
            
            # Print the colored ASCII art
            print(f"{color_code}{ascii_art}{reset_code}")
            
            # Update rotation and sleep
            current_angle = (current_angle + step) % 360.0
            time.sleep(0.05)  # Adjust delay for animation speed
    except KeyboardInterrupt:
        print("\nAnimation stopped.")

if __name__ == "__main__":
    main()