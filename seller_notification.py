import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOTI_FILE = os.path.join(BASE_DIR, "seller_notifications.json")
ORDER_FILE = os.path.join(BASE_DIR, "orders.json")



# --------- Load & Save đơn hàng ---------
def load_orders():
    if os.path.exists(ORDER_FILE):
        try:
            with open(ORDER_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            print("⚠️ File đơn hàng lỗi. Tạo mới...")
            return {}
    return {}
def save_orders(data):
    with open(ORDER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
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

# ---------- CẬP NHẬT TRẠNG THÁI ----------
def update_order_status(seller):
    notifications = load_notifications()

    if seller not in notifications or not notifications[seller]:
        print("❌ Không có đơn hàng!")
        return

    view_notifications(seller)

    try:
        idx = int(input("\nNhập ID đơn hàng cần cập nhật: "))
        order = notifications[seller][idx]
       
    except:
        print("❌ ID không hợp lệ!")
        return

    print("\n1. Đã giao")
    print("2. Hoàn thành")
    print("3. Hủy đơn")

    choice = input("Chọn: ")

    if choice == "1":
        order["delivery_status"] = "Đã giao"

    elif choice == "2":
        order["order_status"] = "Hoàn thành"
    elif choice == "3":
        order["order_status"] = "Đã hủy"
    else:
        print("❌ Lựa chọn không hợp lệ!")
        return

    save_notifications(notifications)
    print("✅ Cập nhật trạng thái thành công!")
