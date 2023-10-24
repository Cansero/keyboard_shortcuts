import json
import keyboard
from keyboard import KeyboardEvent
from time import sleep


def json_to_event(obj):
    return KeyboardEvent(event_type=obj['event_type'],
                         scan_code=obj['scan_code'],
                         name=obj['name'],
                         time=obj['time'],
                         is_keypad=obj['is_keypad'])


def play_macro(thing_to_play):
    keyboard.play(thing_to_play, speed_factor=2)


x = {
    "Shortcut": [],
    "Abbreviation": []
}

while True:
    r = input('What to do?\n'
              'A - Add hotkey\n'
              'B - Add abbreviation\n'
              'C - Continue\n')
    sleep(0.2)
    match r:
        case 'A':
            print('Press shortcut:')
            macro_name = keyboard.read_hotkey(suppress=False)
            sleep(0.2)
            print('Recording macro (esc to finish):')
            macro = keyboard.record()
            macro_json = []
            for kp in macro:
                macro_json.append(kp.to_json())
            x['Shortcut'].append([macro_name, macro_json])

        case 'B':
            abbreviation = input('What to abbreviate: ')
            short = input('How to abbreviate: ')
            x['Abbreviation'].append([short, abbreviation])

        case 'C':
            break

with open('config.json', 'w') as f:
    json.dump(x, f)

with open('config.json', 'r') as f:
    fail = json.load(f)

for k, v in fail.items():
    match k:
        case 'Shortcut':
            for key, presses in v:
                events = []
                for press in presses:
                    events.append(json_to_event(json.loads(press)))
                keyboard.add_hotkey(key, play_macro, [events])

        case 'Abbreviation':
            for short, abbre in v:
                keyboard.add_abbreviation(short, abbre)

keyboard.wait('alt+ctrl+tab')
