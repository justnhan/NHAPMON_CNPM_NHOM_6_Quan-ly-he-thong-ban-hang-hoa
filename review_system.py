import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ORDER_FILE = os.path.join(BASE_DIR, "orders.json")
REVIEW_FILE = os.path.join(BASE_DIR, "reviews.json")


# ---------- LOAD / SAVE ----------
def load_orders():
    if os.path.exists(ORDER_FILE):
        with open(ORDER_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
