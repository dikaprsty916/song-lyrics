import sys
from time import sleep
import time
import os

os.system('cls')

def print_lyrics():
    lines = [
        ("I'm sorry if I say I need you", 0.1),
        ("But I don't care, I'm not scared of love", 0.07),
        ("Cause when I'm not with you, I'm weaker", 0.07),
        ("Is that so wrong?", 0.07),
        ("Is it so wrong", 0.07),
        ("That you make me strong?", 0.07),
    ]

    delays = [ 1, 1.2, 0.6 , 0.64, 0.64, 0.64 ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()