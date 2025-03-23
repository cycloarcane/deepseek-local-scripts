import sys
import time
import math

# Function to convert HSV values to RGB (0-255 range)
def hsv_to_rgb(h, s, v):
    h = h % 360
    h /= 60.0
    i = int(h)
    f = h - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    else:
        r, g, b = v, p, q
    return (int(r * 255), int(g * 255), int(b * 255))

def main():
    ascii_text = "Happy Coding! \U0001f600 " * 6  # Unicode heart, may require terminal support
    try:
        cols = os.get_terminal_size().columns
    except:
        cols = 80  # Fallback if terminal size can't be detected

    offset = 0
    fps = 15
    sleep_time = 1 / fps

    try:
        while True:
            # Fetch current terminal width dynamically
            cols = os.get_terminal_size().columns
            text_len = len(ascii_text)
            start = offset % text_len
            end = start + cols
            segment = ascii_text[start:end] + (ascii_text * 2)[start:end][text_len:]  # Handle wrap-around
            
            # Build colored output
            output = ""
            for i, char in enumerate(segment[:cols]):
                # Calculate hue based on position and offset rotation
                hue = ((offset * 3 + i) % (cols * 2)) / cols  # Doubling hues per frame
                r, g, b = hsv_to_rgb(hue * 360, 1.0, 0.8)
                
                # Format ANSI color codes
                color_code = f"\x1b[38;2;{r};{g};{b}m"
                output += color_code + char
                
            # Reset color and clear previous line
            output += "\x1b[0m\x1b[K\r"
            sys.stdout.write(output)
            sys.stdout.flush()
            offset += 1
            time.sleep(sleep_time)
    except KeyboardInterrupt:
        print("\x1b[0m\nStopped the show! 👋")  # Graceful exit with color reset

if __name__ == "__main__":
    import os
    main()