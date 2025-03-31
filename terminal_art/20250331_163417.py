import os
import time
import colorsys
import sys

ASCII_ART = r"""
   |\_/|
   |o o|   /}
`.\/_/ |
   \__/|
"""

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    current_hue = 0.0  # Starting hue angle
    delta = 1.5  # Hue change per frame (0.0-360.0)
    speed = 0.1  # Delay between frames in seconds

    try:
        while True:
            clear_screen()
            output = []
            for y, line in enumerate(ASCII_ART.split('\n')):
                new_line = []
                for x, char in enumerate(line.strip('\n')):
                    # Calculate hue based on column position and current angle
                    offset = x * 5  # Multiplier for column effect
                    hue = (current_hue + offset) % 360  # Keep in 0-360 range
                    
                    # Convert hue to RGB values
                    r, g, b = colorsys.hsv_to_rgb(hue/360, 1.0, 1.0)
                    r = int(r * 255)
                    g = int(g * 255)
                    b = int(b * 255)
                    
                    # Apply the color and append character to the line
                    new_line.append(f"\033[38;2;{r};{g};{b}m{char}")
                # Reset color after each line
                new_line.append('\033[0m')
                output.append(''.join(new_line))
            
            # Display the animated frames
            print('\n'.join(output))
            current_hue += delta  # Increment hue angle
            
            # Pause before next frame
            time.sleep(speed)
    
    except KeyboardInterrupt:
        print("\nAnimation stopped.")
        sys.exit(0)

if __name__ == "__main__":
    main()