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
def load_reviews():
    if os.path.exists(REVIEW_FILE):
        with open(REVIEW_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
def save_reviews(data):
    with open(REVIEW_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def has_purchased(username, product_name):
    orders = load_orders()

    if username not in orders:
        return False

    for order in orders[username]:
        for item in order["items"]:
            if item["name"].lower() == product_name.lower():
                return True
    return False
