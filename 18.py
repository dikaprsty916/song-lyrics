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
        ("A long way from the playground ", 0.12),
        ("I have loved you since we were 18 ", 0.08),
        ("Long before we both thought the same thing ", 0.09),
        ("To be loved and to be in love ", 0.07),
        ("All I can do ", 0.07),
        ("Is say that these arms ", 0.05),
        ("Are made for holding you, oh-oh ", 0.09), 
        ("I wanna love ", 0.07)
        ("like you made me feel ", 0.07),
        ("When we were 18", 0.06),
    ]

    delays = [ 1.17, 4.55, 1.08, 0.49, 0.5, 0.8, 1.5, 1.45, 1.05, 1.6]


    hide_cursor()
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()