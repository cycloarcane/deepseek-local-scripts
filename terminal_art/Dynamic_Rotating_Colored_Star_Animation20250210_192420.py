import sys
import math
import time
import colorsys
from itertools import cycle

def main():
    # Terminal setup and parameters
    size = 30  # Diameter of the star in characters
    angle_step = 0.1  # Rotation step per frame
    max_angle = 2 * math.pi  # Full rotation
    
    # Character to display
    star = '★'
    
    try:
        angle = 0
        while True:
            # Clear terminal
            sys.stdout.write("\033[2J\033[H")  # Clear screen and move to top-left
            
            # Calculate positions for this frame
            for x in range(size):
                for y in range(size):
                    # Calculate relative position to center
                    xc = x - size//2
                    yc = y - size//2
                    
                    # Apply rotation
                    rotated_x = xc * math.cos(angle) - yc * math.sin(angle)
                    rotated_y = xc * math.sin(angle) + yc * math.cos(angle)
                    
                    # Calculate distance from center
                    distance = math.sqrt(rotated_x**2 + rotated_y**2)
                    
                    if distance < size/3:  # Inside the star pattern
                        # Map distance to color
                        hue = (distance / (size/3)) * max_angle
                        r, g, b = colorsys.hsv_to_rgb(hue/max_angle, 1.0, 1.0)
                        
                        # Convert RGB to ANSI color code
                        r_int = int(r * 255)
                        g_int = int(g * 255)
                        b_int = int(b * 255)
                        color_code = f"\033[38;2;{r_int};{g_int};{b_int}m"
                        
                        # Print character with color
                        sys.stdout.write(color_code + star)
                    else:
                        sys.stdout.write(' ')
                sys.stdout.write('\n')
            
            sys.stdout.flush()
            angle += angle_step
            time.sleep(0.05)
            
            if angle >= max_angle:
                angle = 0
                
    except KeyboardInterrupt:
        # Clean up terminal before exit
        sys.stdout.write("\033[0m\033[2J\033[H")
        sys.stdout.flush()
        return

if __name__ == "__main__":
    main()