import math
import time
from colorize import color
import os
import shutil

# Ascii characters for different levels of brightness
ASCII_CHARS = [' ', '░', '▒', '▓', '█']

def create_ascii_art(angle):
    # This function generates a rotating ASCII circle pattern
    width = shutil.get_terminal_size().columns
    center = width // 2
    radius = 20
    art = []
    
    for y in range(-radius, radius+1):
        row = []
        for x in range(-radius, radius+1):
            # Calculate angle for current position
            x_pos = center + x
            dist = math.hypot(x, y)
            
            # Calculate brightness based on distance from center
            brightness = 4 * math.sin(angle + dist) + 4
            brightness = int(max(0, min(len(ASCII_CHARS)-1, brightness)))
            
            row.append(ASCII_CHARS[brightness])
        art.append(''.join(row))
    return '\n'.join(art)

try:
    color_index = 0
    angle = 0
    
    while True:
        # Change color every frame
        current_color = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan'][color_index]
        color_index = (color_index + 1) % 6
        
        # Generate and print the ASCII art
        os.system('clear')  # Clear the screen
        art = create_ascii_art(angle)
        print(color(art, current_color))
        
        # Update variables for next frame
        angle += 0.1
        time.sleep(0.1)  # Control frame rate
        
except KeyboardInterrupt:
    print("\nAnimation stopped.")