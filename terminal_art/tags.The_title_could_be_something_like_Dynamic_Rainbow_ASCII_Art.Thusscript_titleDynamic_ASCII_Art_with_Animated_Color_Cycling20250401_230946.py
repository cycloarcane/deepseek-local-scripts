import sys
import time
import pyfiglet
import colorsys

def clear_screen():
    """Clear the terminal screen using ANSI escape codes."""
    print('\033[2J\033[H', end='')

def main():
    """Generate dynamic ASCII art with color cycling animation."""
    try:
        text = input("Enter your text (default: 'Hello World!'): ") or "Hello World!"
        art = pyfiglet.figlet_format(text)
    except KeyboardInterrupt:
        sys.exit()

    lines = art.split('\n')
    num_colors = 16  # Number of color steps for smooth animation
    colors = []
    
    # Generate rainbow color palette using HSV spectrum
    for i in range(num_colors):
        hue = i / num_colors
        r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        colors.append((int(r*255), int(g*255), int(b*255)))

    current_shift = 0
    try:
        while True:
            clear_screen()
            for line_num, line in enumerate(lines):
                if not line.strip():
                    continue
                color_idx = (current_shift + line_num) % num_colors
                r, g, b = colors[color_idx]
                # Apply color using truecolor format
                print(f"\x1b[38;2;{r};{g};{b}m{line}\x1b[0m")
            current_shift = (current_shift + 1) % num_colors
            time.sleep(0.1)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()