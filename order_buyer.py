import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
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
def view_order_history(username):
    orders = load_orders()

    print("\n=== 📦 LỊCH SỬ ĐƠN HÀNG CỦA BẠN ===")

    # ❌ Chưa có đơn hàng
    if username not in orders or len(orders[username]) == 0:
        print("❌ Bạn chưa có đơn hàng nào.")
        return

    # Header
    print(f"{'ID':<5} {'Mã đơn':<10} {'Ngày mua':<20} {'Trạng thái'}")
    print("-" * 55)

    for idx, order in enumerate(orders[username]):
        print(
            f"{idx:<5} "
            f"{order['order_id']:<10} "
            f"{order['order_date']:<20} "
            f"{order['status']}"
        )

    try:
        choice = input("\nNhập ID đơn hàng để xem chi tiết (Enter để thoát): ").strip()
        if choice == "":
            return

        oid = int(choice)
        if oid < 0 or oid >= len(orders[username]):
            print("❌ ID không hợp lệ!")
            return
    except:
        print("❌ ID không hợp lệ!")
        return

    order = orders[username][oid]

    print("\n=== 🧾 CHI TIẾT ĐƠN HÀNG ===")
    print(f"Mã đơn     : {order['order_id']}")
    print(f"Ngày mua   : {order['order_date']}")
    print(f"Trạng thái : {order['status']}")
    print("-" * 40)

    total = 0
    for item in order["items"]:
        money = item["price"] * item["quantity"]
        total += money
        print(
            f"- {item['name']} | "
            f"SL: {item['quantity']} | "
            f"Giá: {item['price']} | "
            f"Thành tiền: {money}"
        )

    print("-" * 40)
    print(f"💰 Tổng tiền: {total} VND")