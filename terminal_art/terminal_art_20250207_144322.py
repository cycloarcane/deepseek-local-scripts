import time
import sys
import colorsys
import shutil

ascii_art = [
    "  \\o/  ",
    " /   \\ ",
    "//     \\\\",
    "       ",
    "   o   ",
    "  | |  ",
    "   o   ",
    " __   __ ",
    "(_ _) (_ _)",
    "   -*-*-   ",
]

while True:
    terminal_width = shutil.get_terminal_size().columns
    hue = time.time() % 1
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    color_code = f"\033[38;2;{r};{g};{b}m"
    
    for line in ascii_art:
        line_centered = line.center(terminal_width)
        print(f"{color_code}{line_centered}\033[0m")
    time.sleep(0.1)
    print("\033[10F", end="")