import time

def dynamic_spinner():
    """Generate a colorful rotating ASCII spinner with rainbow color transitions."""
    symbols = ['-', '/', '◈', '\\', '*', '蠖', '|']  # Multisymbol rotation
    colors = [31, 93, 92, 95, 36, 91, 35]  # ANSI color codes (red/yellow/green/cyan/blue/purple)
    interval = 0.1  # Animation speed in seconds
    counter = 0

    try:
        while True:
            symbol = symbols[counter % len(symbols)]
            color_code = colors[counter % len(colors)]
            # Use ANSI codes: \033[ and reset after
            spinner = f'\r\033[{color_code}m{symbol}\033[0m'
            print(spinner, end='', flush=True)
            time.sleep(interval)
            counter += 1
    except KeyboardInterrupt:
        print("\nAnimation stopped.")

if __name__ == "__main__":
    print("Starting dynamic spinner. Press Ctrl+C to exit.")
    dynamic_spinner()