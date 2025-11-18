import sys
from rich import print
from time import sleep

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def printLyrics():
    lines = [
        ("And now", 0.1),
        ("When all is done, there is nothing to say", 0.06),
        ("And if you're done with embarrassing me", 0.06),
        ("On your own, you can go ahead tell them", 0.06),
        ("Tell them all I know now", 0.08),
        ("Shout it from the rooftops", 0.08),
        ("Write it on the skyline", 0.08),
        ("All we had is gone now", 0.08),
        ("Tell them I was happy", 0.08),
        ("And my heart is broken", 0.08),
        ("All my scars are open", 0.08),
        ("Tell them what I hoped would be", 0.08),
        ("Impossible", 0.1),
    ]

    # jeda antarbaris (seragam dulu biar clean, nanti bisa lo tune biar sesuai nadanya)
    delays = [0.5] * len(lines)

    hide_cursor()
    try:
        for i, (line, char_delay) in enumerate(lines):
            for char in line:
                print(f"[bold white]{char}[/bold white]", end="")
                sys.stdout.flush()
                sleep(char_delay)
            print()
            if i < len(delays):
                sleep(delays[i])
    finally:
        sleep(3)
        show_cursor()

printLyrics()


