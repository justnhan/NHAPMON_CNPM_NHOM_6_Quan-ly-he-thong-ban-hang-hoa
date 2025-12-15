import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # thư mục chứa file .py

CART_FILE = os.path.join(BASE_DIR, "cart.json")  # cart.json nằm cùng thư mục

# ------- Hàm tải dữ liệu Giỏ hàng -------
def load_cart():
    if os.path.exists(CART_FILE):
        try:
            with open(CART_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            print("⚠️ File giỏ hàng lỗi. Tạo mới...")
            return {}
    return {}
def save_cart(data):
    with open(CART_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def view_cart(username):
    cart = load_cart()

    print("\n=== GIỎ HÀNG CỦA BẠN ===")

    # 1. Giỏ hàng trống
    if username not in cart or len(cart[username]) == 0:
        print("🛒 Giỏ hàng trống!")
        return

    total = 0
    print("\nID | Tên sản phẩm | Giá | Số lượng | Thành tiền")
    print("-" * 60)

    for idx, item in enumerate(cart[username]):
        name = item["name"]
        price = item["price"]
        qty = item["quantity"]
        money = price * qty
        total += money

        print(f"{idx:<3} {name:<20} {price:<10} {qty:<10} {money}")

    print("-" * 60)
    print(f"💰 Tổng tiền tạm tính: {total} VND")
    
    print("\nBạn muốn làm gì?")
    print("1. Thay đổi số lượng")
    print("2. Xóa sản phẩm")
    print("0. Thoát")
    
    if choice == "1":
        try:
            pid = int(input("Nhập ID sản phẩm: "))
            if pid < 0 or pid >= len(cart[username]):
                print("❌ ID không hợp lệ!")
                return
        except:
            print("❌ ID không hợp lệ!")
            return

        new_qty = input("Nhập số lượng mới: ")

        if not new_qty.isdigit() or int(new_qty) <= 0:
            print("❌ Số lượng phải là số > 0")
            return

        cart[username][pid]["quantity"] = int(new_qty)
        save_cart(cart)
        print("✅ Cập nhật số lượng thành công!")
    elif choice == "2":
        try:
            pid = int(input("Nhập ID sản phẩm cần xóa: "))
            if pid < 0 or pid >= len(cart[username]):
                print("❌ ID không hợp lệ!")
                return
        except:
            print("❌ ID không hợp lệ!")
            return

        del cart[username][pid]
        save_cart(cart)

        print("✅ Đã xóa sản phẩm khỏi giỏ!")

    else:
        print("↩ Trở lại menu.")

    choice = input("Chọn: ")