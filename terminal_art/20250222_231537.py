import time
import os

# Define the ASCII cube structure with different rotations
cube_frames = [
    [
        "  _______  ",
        " /       \\ ",
        "/         \\",
        "|         |",
        "|         |",
        "\\         /",
        " \\_______/ "
    ],
    [
        "  \\_______/  ",
        "  _______   ",
        "        \\  ",
        "         | ",
        " ________| ",
        "        |  ",
        "        /  "
    ]
]

# ANSI color codes
colors = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
]

# Reset color
reset = "\033[0m"

# Animation loop
while True:
    for frame in cube_frames:
        for i, line in enumerate(frame):
            # Apply different color for each line in the cube
            color = colors[i % len(colors)]
            print(color + line + reset)
        # Pause for a moment
        time.sleep(0.3)
        # Clear the terminal
        os.system('clear')