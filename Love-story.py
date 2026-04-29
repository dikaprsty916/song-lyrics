import sys
from time import sleep
import time
import os

# Warna
GOLD = "\033[1;38;5;220m"
RESET = "\033[0m"

def hide_cursor():
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def print_lyrics():
    lines = [
        ("That you were Romeo ", 0.08),
        ("you were throwing pebbles ", 0.08),
        ("And my daddy said ", 0.08),
        ("Stay away from Juliet ", 0.08),
        ("And I was crying on the staircase ", 0.08),
        ("Begging you, Please don't go ", 0.08),
        ("And I said ", 0.1), 
        ("Romeo take me ", 0.1), 
        ("Somewhere we can be alone ", 0.08), 
        ("I'll be waiting ", 0.1), 
        ("All there's left to do is run ", 0.07), 
        ("You'll be the prince, ", 0.07), 
        ("And I'll be the princess, ", 0.07), 
        ("It's a love story ", 0.08), 
        ("Baby, just say yes ", 0.1), 
    ]

    delays = [0.1, 0.1, 0.1, 0.1, 0.2, 2.4, 0.28, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

    hide_cursor()

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(GOLD + char + RESET, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

    print("\n")
    time.sleep(3)

    show_cursor()

print_lyrics()