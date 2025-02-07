import time
import sys

colors = [f'\033[3{j}m' for j in range(8)]
figure = ['💀', '🖤', '哂)', 'MutableFigure', ' образования', 'ໝຶ', ' fist up ➛', ' fist down ↩️']

while True:
    t = int(time.time() * 100)
    s = ''
    for i, c in enumerate(figure):
        color_idx = (i + t // 5) % 8
        s += colors[color_idx] + c
    print('\r' + s + '\033[0m', end='')
    time.sleep(0.1)
    sys.stdout.flush()