import keyboard
from time import sleep


def on_mn():
    keyboard.send('alt+tab')
    sleep(0.1)
    keyboard.send('ctrl+tab')
    sleep(0.1)
    keyboard.send('alt+tab')


if __name__ == '__main__':
    keyboard.add_hotkey("n+m", on_mn)
    keyboard.add_abbreviation("@@", "hola como estas")

    keyboard.wait('ctrl+alt+tab')