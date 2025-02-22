import sys
import math
import time
import termios
import tty

def main():
    # Save terminal settings
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        # Clear the screen
        sys.stdout.write('\x1b[2J\x1b[0;0H')
        sys.stdout.flush()
        
        # Animation loop
        angle = 0.0
        while True:
            # Terminal clear
            sys.stdout.write('\x1b[2J\x1b[0;0H')
            sys.stdout.flush()
            
            # ASCII art with rainbow effect
            for y in range(-20, 21):
                for x in range(-40, 41):
                    # Calculate distance from origin
                    distance = math.sqrt(x**2 + y**2)
                    
                    # Draw outer circle (globe)
                    if 18 <= distance <= 20:
                        # Color transitions based on angle
                        hue = (math.sin(angle * 0.5 + x * 0.5) + 1) / 2
                        r = int(255 * math.sin(hue * math.pi))
                        g = int(255 * math.sin((hue + 1/3) * math.pi))
                        b = int(255 * math.sin((hue + 2/3) * math.pi))
                        # Set color
                        sys.stdout.write(f'\x1b[38;2;{r};{g};{b}m*')
                        sys.stdout.flush()
                    
                    # Draw inner circle (clouds)
                    elif 10 <= distance <= 12:
                        sys.stdout.write('o')
                    
                    elif distance <= 2:
                        sys.stdout.write(' ')  # Empty space
            
                sys.stdout.write('\n')  # Move to next line
            sys.stdout.write('\x1b[0m')  # Reset color
                
            # Update angle for next frame and sleep
            angle += 0.2
            time.sleep(0.1)
            
            # Check for exit condition (Ctrl-C or 'q')
            if sys.stdin.read(1) == 'q':
                break
                
    except KeyboardInterrupt:
        pass
    finally:
        # Restore terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print("\nTerminating gracefully...")

if __name__ == "__main__":
    main()