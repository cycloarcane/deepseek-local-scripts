from blessed import Terminal
import time
import random

def main():
    term = Terminal()
    
    # ASCII flame art
    flame_art = [
        "          ######          ",
        "        ####  ####        ",
        "       ##      ## ##       ",
        "     ##         ####       ",
        "     ##         ####       ",
        "      ##       ####        ",
        "        ####  ####         ",
        "          ######           ",
    ]

    # Define colors for different sections
    colors = [
        term.on_red,
        term.on_orange,
        term.on_yellow,
        term.on_white,
    ]
    
    # Initial phase
    phase = 0
    
    try:
        while True:
            # Calculate position to center the flame
            height = term.height
            width = term.width
            start_y = (height - len(flame_art)) // 2
            start_x = (width - max(len(line) for line in flame_art)) // 2
            
            # Clear screen
            print(term.clear())
            
            for i, line in enumerate(flame_art):
                # Get color based on position and phase
                color_idx = (i + phase) % len(colors)
                color = colors[color_idx]
                
                # Add dynamic noise
                noise = random.uniform(-0.1, 0.1) * start_x
                x_pos = int(start_x + noise)
                
                # Print line with color
                print(term.move(start_y + i, x_pos) + color + line)
            
            # Update phase for color cycling
            phase += 0.2
            phase %= len(colors)
            
            # Wait for next frame
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print(term.clear())
        print("ASCII art flame extinguished. Goodbye!")

if __name__ == "__main__":
    main()