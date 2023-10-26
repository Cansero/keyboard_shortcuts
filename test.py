import json

try:
    with open('config.json', 'r') as f:
        text = json.load(f)
except FileNotFoundError:
    with open('config.json', 'x') as f:
        pass

print(text)
