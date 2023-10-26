import json
import keyboard
from PySide6.QtWidgets import QApplication
from keyboard import KeyboardEvent
from win_util import Win


def json_to_event(obj):
    return KeyboardEvent(event_type=obj['event_type'],
                         scan_code=obj['scan_code'],
                         name=obj['name'],
                         time=obj['time'],
                         is_keypad=obj['is_keypad'])


def play_macro(thing_to_play):
    keyboard.play(thing_to_play, speed_factor=2)


if __name__ == '__main__':
    options = dict()
    try:
        with open('config.json', 'r') as f:
            options = json.load(f)
    except FileNotFoundError:
        with open('config.json', 'x') as f:
            pass

    shortcuts = dict()
    abbreviations = dict()

    if options:
        for k, v in options.items():
            match k:
                case 'Shortcut':
                    for key, presses in v:
                        events = []
                        for press in presses:
                            events.append(json_to_event(json.loads(press)))
                        s = keyboard.add_hotkey(key, play_macro, (events,))
                        shortcuts[key] = s

                case 'Abbreviation':
                    for short, abbre in v:
                        s = keyboard.add_abbreviation(short, abbre)
                        abbreviations[short] = [abbre, s]

    else:
        pass

    app = QApplication([])
    x = Win(abbreviations=abbreviations, shortcuts=shortcuts)
    x.show()
    app.exec()
