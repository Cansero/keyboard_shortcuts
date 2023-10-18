import keyboard


def on_mn():
    print("se preciono n y m juntas")


if __name__ == '__main__':
    keyboard.add_hotkey("n+m", on_mn)
    keyboard.add_abbreviation("@@", "hola como estas")
    keyboard.wait()