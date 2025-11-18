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
        ("she said, “careful, or you’ll lose it”", 0.05),
        ("but, girl, i’m only human", 0.05),
        ("and i know there’s a blade where your heart is", 0.05),
        ("and you know how to use it", 0.05),
        ("and you can take my flesh if you want, girl", 0.05),
        ("but, baby, don’t abuse it", 0.068),
        ("(Calm down)", 0.068),
        ("these voices in my head screaming, “run, now”", 0.06),
        ("i’m praying that they’re human", 0.06),
    ]

    # jeda antarbaris (bisa lo tune biar pas sama nadanya)
    delays = [1.5, 2.1, 0.9, 1.9, 0.54, 0.31, 0.27, 0.6, 0.18]

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
