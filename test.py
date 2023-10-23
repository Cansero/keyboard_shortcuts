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

macro_name = keyboard.read_hotkey(suppress=False)
print("recorded")
sleep(0.2)
macro = keyboard.record()
macro.pop()
print("recorded")
sleep(0.2)
macro_str = []
for kp in macro:
    macro_str.append(kp.to_json())

x["Shortcut"].append([macro_name, macro_str])

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
            pass

keyboard.wait('alt+ctrl+tab')
