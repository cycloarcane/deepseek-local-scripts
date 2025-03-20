import time
import sys

MESSAGE = "✨ ASCII ART 🎨".center(20)  # Centered with decorations
COLORS = [  # ANSI color codes for vibrant colors
    "\x1b[31m",    # Red
    "\x1b[33m",    # Yellow
    "\x1b[93m",    # Gold
    "\x1b[92m",    # Green
    "\x1b[34m",    # Blue
    "\x1b[35m",    # Magenta
    "\x1b[36m"     # Cyan
]
RESET = "\x1b[0m"  # Reset color code
speed = 0.1  # Animation speed in seconds
offset = 0

try:
    while True:
        sys.stdout.write('\r')  # Return to start of current line
        for i, char in enumerate(MESSAGE):
            # Cycle through colors with offset for each character
            color_code = COLORS[(offset + i) % len(COLORS)]
            sys.stdout.write(color_code + char)
        sys.stdout.write(RESET)  # Reset after all characters
        sys.stdout.flush()  # Force immediate display
        time.sleep(speed)
        offset = (offset + 1) % len(COLORS)  # Advance color offset
except KeyboardInterrupt:
    print('\n' + RESET)  # Cleanup on exit