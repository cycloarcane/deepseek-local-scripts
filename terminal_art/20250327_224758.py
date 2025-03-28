import os
import time

# Terminal Grid Dimensions
ROWS = 10  # Number of rows in the grid
COLS = 20  # Number of columns in the grid
DELAY = 0.1  # Delay between frames in seconds

# Ball Properties
dx = 1  # Initial x-direction
dy = 1  # Initial y-direction
pos_x, pos_y = COLS // 2, ROWS // 2  # Start position (center)
current_color = 0  # Cycle starting color index

# Color Palette (ANSI codes)
colors = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
]
RESET = "\033[0m"  # Reset ANSI color


def clear_screen():
    """Clear terminal screen based on OS."""
    os.system("cls" if os.name == "nt" else "clear")


def draw_ball():
    """Draw the ball in the terminal with current colors."""
    clear_screen()
    for y in range(ROWS):
        row = []
        for x in range(COLS):
            if x == pos_x and y == pos_y:
                # Color the ball's position
                row.append(f"{colors[current_color]} Размер: 50")
            else:
                row.append(" ")
        print("".join(row), end="\n")
    global current_color
    current_color = (current_color + 1) % len(colors)  # Cycle color


def update_position():
    """Update ball position and reverse direction on collisions."""
    global pos_x, pos_y, dx, dy
    new_x = pos_x + dx
    new_y = pos_y + dy

    # Check for wall collisions in x-direction
    if new_x <= 0 or new_x >= COLS - 1:
        dx *= -1
    # Check for wall collisions in y-direction
    if new_y <= 0 or new_y >= ROWS - 1:
        dy *= -1

    # Update position
    pos_x += dx
    pos_y += dy


def main():
    try:
        while True:
            draw_ball()
            update_position()
            time.sleep(DELAY)
    except KeyboardInterrupt:
        clear_screen()
        print("Animation ended.")


if __name__ == "__main__":
    main()