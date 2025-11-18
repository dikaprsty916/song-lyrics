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
        ("You can't fight it, you can't breathe", 0.05),
        ("You say something so loving, but", 0.08),
        ("Now I gotta let you go", 0.05), #3
        ("You'll be better off in someone new", 0.05),
        ("I don't wanna be alone", 0.06), #5
        ("You know it hurts me too", 0.09),#6
        ("You look so broken when you cry", 0.09),
        ("One more and then I say goodbye", 0.06), #8
        ("Sometimes, all I think about is you", 0.08), #9
        ("Late nights in the middle of June", 0.08), #10
        ("Heat waves been fakin' me out", 0.08), #11
        ("Can't make you happier now", 0.07), #12
    ]

    delays = [0.4, 0.7, 1.6, 1, 1.6, 0.7, 0.6, 0.6, 0.8, 1, 0.5, 0.5]

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
        print("\n[bold green]✨ End of Heat Waves ✨[/bold green]")
        sleep(3)
        show_cursor()


printLyrics()

