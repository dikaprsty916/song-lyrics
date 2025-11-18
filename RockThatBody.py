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
        ("I wanna da-", 0.06),
        ("I wanna dance in the lights", 0.05),
        ("I wanna ro-", 0.07),
        ("I wanna rock your body", 0.08),
        ("I wanna go", 0.08),
        ("I wanna go for a ride", 0.068),
        ("Hop in the music and", 0.07),
        ("Rock your body", 0.08),
        ("Rock that body", 0.069),
        ("come on, come on", 0.035),
        ("Rock that body", 0.05),
        ("(Rock your body)", 0.03),
        ("Rock that body", 0.049),
        ("come on, come on", 0.035),
        ("Rock that body", 0.08),
    ]

    delays = [0.1, 1, 0.2, 1, 0.2, 0.8, 0.2, 0.5, 0.18, 0.1, 0.15, 0.3, 0.3, 0.3, 0.1, 5]

    hide_cursor()

    try:
        for i, (line, char_delay) in enumerate(lines):
            for char in line:
                if line == '(Rock your body)':
                    print(f"[orange4]{char}[/orange4]", end='')
                else:
                    print(f"[bold][gold3]{char}[/bold][/gold3]", end='')  # Perbaikan tag
                sys.stdout.flush()
                sleep(char_delay)
            print()
            if i < len(delays):
                sleep(delays[i])
    finally:
        print()  # Baris kosong setelah lirik terakhir
        sleep(2)  # Penundaan waktu sebelum program berakhir
        show_cursor()


printLyrics()
