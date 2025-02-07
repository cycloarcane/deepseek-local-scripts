import time
from rich import print
from rich.color import Color
from rich.console import Console

# Create a set of vibrant colors
colors = [
    Color.from_hex("#FF6B6B"),
    Color.from_hex("#4ECDC4"),
    Color.from_hex("#45B7D1"),
    Color.from_hex("#96CEB4"),
    Color.from_hex("#FFEEAD"),
    Color.from_hex("#D4A5A5"),
    Color.from_hex("#9B87C9"),
    Color.from_hex("#6B7D9B")
]

# Create the basic ASCII hexagon art
hexagon = [
    "   o   ",
    "  o o  ",
    " o   o ",
    "o     o",
    " o   o ",
    "  o o  ",
    "   o   "
]

console = Console()

try:
    while True:
        # Clear the screen
        console.clear()
        
        # Generate random colors for each character
        for i, line in enumerate(hexagon):
            styled_line = []
            for j, char in enumerate(line):
                # Apply different colors to create a dynamic effect
                color = colors[(i + j) % len(colors)]
                styled_line.append(f"[{color.hex}] {char} [/]")
            
            # Print each styled line with proper formatting
            print("".join(styled_line))
        
        # Add some padding
        print("\n" * 2)
        
        # Increment rotation and sleep for smooth animation
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nAnimation stopped.")