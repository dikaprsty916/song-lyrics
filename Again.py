from rich import print
from time import sleep
import os

os.system('cls')

lines = [
    (0.8, "I wanna be your lover", 0.13),
    (1.2, "I don't wanna be your friend", 0.08),
    (0.5, "You don't know what you have until it's gone, my dear", 0.06),
    (1.8, "So tell me that you love me again", 0.068),
    (1.8, "I wanna be your lover", 0.08),
    (1.7, "Baby, I'm holding my breath", 0.08),
    (0.8, "You don't know what you have until it's gone, my dear", 0.06),
    (5, "So tell me that you love me again", 0.06),
]

def printLyrics():
    for i, (lines_delay, line, char_delay) in enumerate(lines):
        clean_line = line.replace("\\", "")  
        for char in clean_line:
            print(f"{char}", end='', flush=True)
            sleep(char_delay)
        sleep(lines_delay)
        print()

printLyrics()

