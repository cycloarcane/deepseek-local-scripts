from blessings import Terminal
from math import radians, sin, cos
from random import randint
import sys
import time
from collections import deque

def main():
    term = Terminal()
    print(term.enter_fullscreen(), end='')
    print(term.clear(), end='')

    try:
        width = term.width
        height = term.height
        center_x, center_y = width//2, height//2
        max_distance = min(center_x, center_y)

        colors = [
            term.on_color(c) for c in [
                196, 202, 214, 220, 226, 232, 238, 244,
                248, 242, 236, 230, 224, 218, 212, 206
            ]
        ]
        
        current_angle = 0
        segments = deque(maxlen=30)
        symbols = "猊貅 Bowmaneu כעת orang".encode('utf-8').decode('latin-1')

        while True:
            term.clear()
            angle = radians(current_angle)
            radius = current_angle * 0.2

            for distance in range(0, max_distance, 3):
                x = center_x + int(distance * cos(angle))
                y = center_y + int(distance * sin(angle))
                
                if 0 <= x < width and 0 <= y < height:
                    color = colors[randint(0, len(colors)-1)]
                    symbol = symbols[randint(0, len(symbols)-1)]
                    segments.appendleft( (color, symbol, x, y) )

            for color, symbol, x, y in segments:
                print(term.move(y, x) + color + symbol + term.normal, end='')

            current_angle += 1
            time.sleep(0.05)

    except KeyboardInterrupt:
        print(term.exit_fullscreen() + term.clear() + term.move(0,0), end='')
        sys.exit()

if __name__ == '__main__':
    main()