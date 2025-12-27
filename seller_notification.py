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
def add_notification(
    seller,
    buyer,
    product_name,
    quantity,
    total,
    order_id
):
    notifications = load_notifications()

    if seller not in notifications:
        notifications[seller] = []

    notifications[seller].append({
        "order_id": order_id,
        "buyer": buyer,
        "product_name": product_name,
        "quantity": quantity,
        "total": total,
        "payment_status": "Đã thanh toán",
        "delivery_status": "Đang giao",
        "order_status": "Chưa hoàn thành",
        "time": datetime.now().strftime("%d/%m/%Y %H:%M")
    })

    save_notifications(notifications)

# ---------- XEM THÔNG BÁO ----------
def view_notifications(seller):
    notifications = load_notifications()

    print("\n📢 THÔNG BÁO ĐƠN HÀNG")

    if seller not in notifications or not notifications[seller]:
        print("📭 Không có thông báo nào.")
        return

    for idx, n in enumerate(notifications[seller]):
        print("-" * 50)
        print(f"ID: {idx}")
        print(f"Mã đơn: {n['order_id']}")
        print(f"Người mua: {n['buyer']}")
        print(f"Sản phẩm: {n['product_name']}")
        print(f"Số lượng: {n['quantity']}")
        print(f"Tổng tiền: {n['total']}")
        print(f"Thanh toán: {n['payment_status']}")
        print(f"Giao hàng: {n['delivery_status']}")
        print(f"Trạng thái: {n['order_status']}")
        print(f"Thời gian: {n['time']}")

