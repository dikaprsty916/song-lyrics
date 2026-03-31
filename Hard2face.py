import sys
from time import sleep
import time
import os

os.system('cls')

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def print_lyrics():
    lines = [
        ("Don't be afraid to stand alone ", 0.06),
        ("Don't be afraid to stand outside your comfort zone ", 0.06),
        ("I know it's hard away from home ", 0.06),
        ("And it ain't easy all alone ", 0.06),
        ("Relationships over the phone ", 0.06),
        ("Talkin' to your significant other all night long ", 0.06),
        ("Sometimes it's hard to face reality ", 0.06), 
    ]
    delays = [ 1, 0.8, 1, 1.5, 0.8, 0.2, 1]


    hide_cursor()
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()