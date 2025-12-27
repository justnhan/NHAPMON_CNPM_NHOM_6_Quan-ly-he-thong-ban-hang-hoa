import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCT_FILE = os.path.join(BASE_DIR, "products.json")
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

    if username not in orders or not orders[username]:
        print("❌ Bạn chưa có đơn hàng nào!")
        return

    print("\n=== 📦 LỊCH SỬ ĐƠN HÀNG CỦA BẠN ===")
    print(f"{'ID':<3} {'Mã đơn':<15} {'Ngày mua':<20} {'Trạng thái'}")
    print("-" * 55)

    for idx, order in enumerate(orders[username]):
        # check cả 2 key, ưu tiên order_date, fallback time
        order_time = order.get("order_date") or order.get("time") or "N/A"
        print(
            f"{idx:<3} {order['order_id']:<15} {order_time:<20} {order['status']}"
        )

def load_products():
    if os.path.exists(PRODUCT_FILE):
        with open(PRODUCT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
def check_stock(product_name, buy_quantity):
    products = load_products()

    for seller, plist in products.items():
        for p in plist:
            if p["name"].lower() == product_name.lower():
                if buy_quantity > p["quantity"]:
                    print(
                        f"❌ Quá số lượng tồn kho!\n"
                        f"Tồn kho hiện tại: {p['quantity']}"
                    )
                    return False
                return True

    print("❌ Không tìm thấy sản phẩm!")
    return False