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
    # 1. Load dữ liệu từ cả hai file
    notifications = load_notifications()
    all_orders = load_orders() # Giả sử bạn có hàm này để load file order

    if seller not in notifications or not notifications[seller]:
        print("❌ Bạn không có thông báo đơn hàng nào!")
        return

    # Hiển thị danh sách cho người bán chọn
    view_notifications(seller)

    try:
        idx = int(input("\nChọn số thứ tự đơn hàng cần cập nhật (từ 0): "))
        if idx < 0 or idx >= len(notifications[seller]):
            raise ValueError
            
        # Lấy thông tin đơn hàng từ notification
        noti_item = notifications[seller][idx]
        target_order_id = noti_item["order_id"]
        buyer_name = noti_item["buyer"]
        
    except (ValueError, IndexError):
        print("❌ Lựa chọn không hợp lệ!")
        return

    print(f"\n--- Cập nhật đơn hàng: {target_order_id} ---")
    print("1. Đã giao")
    print("2. Hoàn thành")
    print("3. Hủy đơn")
    choice = input("Chọn (1-3): ")

    # 2. Xử lý cập nhật trạng thái
    new_delivery_status = noti_item["delivery_status"]
    new_order_status = noti_item["order_status"]

    if choice == "1":
        new_delivery_status = "Đã giao"
    elif choice == "2":
        new_order_status = "Hoàn thành"
        new_delivery_status = "Đã giao" # Thường hoàn thành thì mặc định là đã giao
    elif choice == "3":
        new_order_status = "Đã hủy"
    else:
        print("❌ Lựa chọn không hợp lệ!")
        return

    # 3. Cập nhật vào cấu trúc Notifications (File Noti)
    noti_item["delivery_status"] = new_delivery_status
    noti_item["order_status"] = new_order_status

    # 4. Cập nhật vào cấu trúc Orders (File Order của người mua)
    # Tìm đơn hàng khớp ID trong danh sách của người mua
    if buyer_name in all_orders:
        for order in all_orders[buyer_name]:
            if order["order_id"] == target_order_id:
                # Map trạng thái tương ứng sang file Order
                if choice == "1":
                    order["status"] = "Đang giao hàng"
                elif choice == "2":
                    order["status"] = "Hoàn thành"
                elif choice == "3":
                    order["status"] = "Đã hủy"
                break

    # 5. Lưu lại cả hai file
    save_notifications(notifications)
    save_orders(all_orders) # Giả sử bạn có hàm này
    
    print(f"✅ Đã cập nhật đơn hàng {target_order_id} thành: {new_order_status} ({new_delivery_status})")
