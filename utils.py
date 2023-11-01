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
    options = {'Shortcut': {}, 'Abbreviation': {}}
    try:
        with open(file, 'r') as f:
            options = json.load(f)
    except FileNotFoundError:
        with open(file, 'x') as _f:
            pass
        save_file(file, options)
    return options


def save_file(file, data):
    for short, macro in data['Shortcut'].items():
        events = []
        for event in macro:
            events.append(event.to_json())
        data['Shortcut'][short] = events

    with open(file, 'w') as f:
        json.dump(data, f)
