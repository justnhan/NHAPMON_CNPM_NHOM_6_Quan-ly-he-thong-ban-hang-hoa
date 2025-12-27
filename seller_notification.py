import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOTI_FILE = os.path.join(BASE_DIR, "seller_notifications.json")

# ---------- LOAD / SAVE ----------
def load_notifications():
    if os.path.exists(NOTI_FILE):
        try:
            with open(NOTI_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_notifications(data):
    with open(NOTI_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
