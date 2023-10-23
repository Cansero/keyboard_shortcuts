import keyboard
from time import sleep


def on_mn():
    keyboard.send('alt+tab')
    sleep(0.1)
    keyboard.send('ctrl+tab')
    sleep(0.1)
    keyboard.send('alt+tab')


if __name__ == '__main__':
    macro = keyboard.record()
    print(macro)