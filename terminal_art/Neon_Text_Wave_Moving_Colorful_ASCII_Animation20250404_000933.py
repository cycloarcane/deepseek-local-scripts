import sys
import time

MESSAGE = "WELCOME TO ANSI COLOR ART!"
COLOR_CODES = ['31', '33', '32', '36', '34', '35', '37', '91', '92', '93', '94', '95', '96', '97']

def main():
    try:
        # Hide terminal cursor
        sys.stdout.write('\033[?25l')
        frame = 0
        while True:
            # Clear screen and move cursor to top-left corner
            sys.stdout.write('\033[H\033[2J')
            line = ''
            for idx, char in enumerate(MESSAGE):
                # Calculate color index based on character position and frame
                color_index = (idx + frame) % len(COLOR_CODES)
                color = COLOR_CODES[color_index]
                line += f'\033[{color}m{char}\033[0m'
            sys.stdout.write(line)
            sys.stdout.flush()
            time.sleep(0.2)
            frame += 1
    except KeyboardInterrupt:
        pass
    finally:
        # Restore terminal settings
        sys.stdout.write('\033[?25h\033[H\033[2J')
        print("\nAnimation Stopped!")

if __name__ == "__main__":
    main()