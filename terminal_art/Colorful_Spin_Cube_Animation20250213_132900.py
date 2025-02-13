import sys
import math
import time
import colorsys
from colorama import init, Fore, Back, Style
from asciimatics.screen import Screen
from asciimatics.effects import Effect
from asciimatics.exceptions import ResizeError, StopApplication

# Initialize colorama
init()

class ColorfulSpinCube(Effect):
    def __init__(self, screen):
        super().__init__(screen)
        # Cube definition
        self.cube = [
            [
                " █████ ",
                "███████",
                " █████ "
            ],
            [
                " █████ ",
                "███████",
                " █████ "
            ],
            [
                " █████ ",
                "███████",
                " █████ "
            ]
        ]
        self.angle = 0

    def _set_color(self, h):
        # Convert HSL to RGB
        r, g, b = colorsys.hls_to_rgb(h, 0.5, 1.0)
        # Scale to 0-255 and convert to hex
        r, g, b = [int(x*255) for x in (r, g, b)]
        # Set color using ANSI escape codes
        return f"\033[38;2;{r};{g};{b}m"

    def _update_cube(self):
        self.angle += 0.1
        rotated_cube = []
        for face in self.cube:
            # Simple rotation for demonstration
            rotated_face = [line * int(math.cos(self.angle) * 2 + 1) for line in face]
            # Apply random color
            color = self._set_color(time.time() % 1)
            rotated_face = [f"{color}{line}\033[0m" for line in rotated_face]
            rotated_cube.append(rotated_face)
        return rotated_cube

    def _draw_cube(self):
        cube = self._update_cube()
        lines = []
        for row in range(3):
            line = ""
            for face in cube:
                line += face[row] + "  "
            lines.append(line)
        return lines

    def update(self, frame_no):
        # Clear screen
        self._screen.clear()
        
        # Get terminal dimensions
        width, height = self._screen.dimensions
        
        # Get cube lines
        cube_lines = self._draw_cube()
        
        # Print cube centered on screen
        for i, line in enumerate(cube_lines):
            self._screen.print_at(line, (width - len(line)) // 2, i + (height - len(cube_lines)) // 2)
        
        # Flush buffer
        self._screen.refresh()

def demo(screen):
    effects = [
        ColorfulSpinCube(screen)
    ]
    screen.play(effects, interval=1/30)

if __name__ == "__main__":
    Screen.wrapper(demo)