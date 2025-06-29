import time
from datetime import datetime, timedelta
from utils import load_events

def check_reminders():
    while True:
        now = datetime.now()
        upcoming = [e for e in load_events() if datetime.fromisoformat(e['start_time']) - now <= timedelta(hours=1)]
        for e in upcoming:
            print(f"Reminder: {e['title']} at {e['start_time']}")
        time.sleep(60)
