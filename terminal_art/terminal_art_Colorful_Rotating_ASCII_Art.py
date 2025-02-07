import os
import sys
from time import sleep
from rich.console import Console
from itertools import cycle

console = Console()

class ArtGenerator:
    def __init__(self):
        # Basic ASCII art shapes
        self.shapes = [
            "████", 
            "####", 
            "▒▒▒▒", 
            "░░░░",
            "蹶蹶",
            "ipop"
        ]
        self.color_palette = [
            "red", "green", "blue", "cyan", 
            "magenta", "yellow", "bright_red",
            "bright_green", "bright_blue"
        ]
        self.current_colors = cycle(self.color_palette)
        
    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def generate_art(self):
        art = []
        for shape in self.shapes:
            color = next(self.current_colors)
            art.append(f"[{color}]{shape}[/{color}]")
        return ' '.join(art) + ' '
    
    def animate(self):
        while True:
            self.clear_terminal()
            for _ in range(5):
                print(self.generate_art())
            sleep(0.1)
            # Rotate the art elements
            self.shapes = self.shapes[1:] + [self.shapes[0]]

def main():
    console.print("[bold green]Starting ASCII Art Animation...[/bold green]")
    art_gen = ArtGenerator()
    try:
        art_gen.animate()
    except KeyboardInterrupt:
        art_gen.clear_terminal()
        console.print("\n[bold yellow]Animation stopped. Thanks for watching![/bold yellow]")

if __name__ == "__main__":
    main()