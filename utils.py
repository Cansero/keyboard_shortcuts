import json
import keyboard
from keyboard import KeyboardEvent


def play_macro(macro):
    keyboard.play(macro, speed_factor=2)


def json_to_event(obj):
    return KeyboardEvent(event_type=obj['event_type'],
                         scan_code=obj['scan_code'],
                         name=obj['name'],
                         time=obj['time'],
                         is_keypad=obj['is_keypad'])


def load_file(file):
    options = dict()
    try:
        with open(file, 'r') as f:
            options = json.load(f)
    except FileNotFoundError:
        with open(file, 'x') as f:
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
                        keyboard.add_abbreviation(short, abbre)
                        abbreviations[short] = abbre

    return shortcuts, abbreviations
