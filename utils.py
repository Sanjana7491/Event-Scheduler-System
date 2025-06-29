import json
from os.path import exists

FILE = 'events.json'

def load_events():
    if not exists(FILE):
        return []
    with open(FILE, 'r') as f:
        return json.load(f)

def save_events(events):
    with open(FILE, 'w') as f:
        json.dump(events, f, indent=4)
