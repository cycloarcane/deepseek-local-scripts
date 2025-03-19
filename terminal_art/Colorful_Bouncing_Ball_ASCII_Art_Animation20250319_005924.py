import time
import os
import sys

def hsv_to_rgb(h, s=1.0, v=1.0):
    """Convert HSV to RGB values in the range 0-255."""
    h = h % 1
    s = max(0, min(s, 1))
    v = max(0, min(v, 1))

    if s == 0.0:
        return (int(v * 255),) * 3

    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1 - s)
    q = v * (1 - s * f)
    t = v * (1 - s * (1 - f))
    i %= 6

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
    # Initialize screen dimensions and ball properties
    screen_width = os.get_terminal_size().columns
    screen_height = os.get_terminal_size().lines

    # Initial position and velocity of the ball
    x = screen_width // 2
    y = screen_height // 2
    vx = 1
    vy = 1

    start_time = time.time()
    try:
        while True:
            # Calculate current time-based color and position
            elapsed_time = time.time() - start_time
            hue = (elapsed_time / 5) % 1  # 5-second color cycle
            r, g, b = hsv_to_rgb(hue)

            # Check boundaries for bouncing
            if x == 0 or x == screen_width - 1:
                vx = -vx
            if y == 0 or y == screen_height - 1:
                vy = -vy
            x += vx
            y += vy

            # Clear screen and update ball position
            sys.stdout.write('\033[2J\033[H')  # Clear screen and reset cursor
            # Set cursor position and display the ball
            sys.stdout.write(f'\033[{y+1};{x+1}H')  # Move cursor
            color_code = f"\033[38;2;{r};{g};{b}m"  # Set color
            sys.stdout.write(f"{color_code}○\033[0m")  # Display ball with reset
            sys.stdout.flush()  # Ensure output is immediate

            time.sleep(0.08)  # Frame delay

    except KeyboardInterrupt:
        # Clean exit
        sys.stdout.write('\033[2J\033[H')
        print("Animation stopped.")
        sys.exit(0)

if __name__ == "__main__":
    main()