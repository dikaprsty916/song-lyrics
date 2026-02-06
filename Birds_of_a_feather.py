import sys
from time import sleep
import time
import os

os.system('cls')

def print_lyrics():
    lines = [
        ("And I don't know what I'm cryin' for", 0.12),
        ("I don't thing i could love you more", 0.12),
        ("It might not be long", 0.1),
        ("but baby, I", 0.14),
        ("I'll love you 'til the day that I die", 0.09),
        ("'Til the day that I die", 0.09),
    ]

    delays = [ 0.4, 0.2, 0.2 , 2, 2.4, 1 ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()