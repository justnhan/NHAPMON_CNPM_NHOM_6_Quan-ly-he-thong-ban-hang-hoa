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

    def add_to_cart(buyer_username, seller_username):
    products = load_products()
    cart = load_cart()

    # 1. Kiểm tra seller có sản phẩm không
    if seller_username not in products or len(products[seller_username]) == 0:
        print("❌ Người bán chưa có sản phẩm nào!")
        return

    # 2. Hiển thị sản phẩm của seller
    print("\n=== DANH SÁCH SẢN PHẨM ===")
    print("ID | Tên sản phẩm | Giá | Số lượng còn")
    print("-" * 50)

    for idx, item in enumerate(products[seller_username]):
        print(f"{idx:<3} {item['name']:<15} {item['price']:<10} {item['quantity']}")

    # 3. Nhập ID sản phẩm
    try:
        pid = int(input("\nNhập ID sản phẩm cần thêm: "))
        if pid < 0 or pid >= len(products[seller_username]):
            print("❌ ID sản phẩm không hợp lệ!")
            return
    except:
        print("❌ ID sản phẩm không hợp lệ!")
        return

    product = products[seller_username][pid]

    # 4. Nhập số lượng
    qty = input("Nhập số lượng muốn mua: ").strip()

    if not qty.isdigit() or int(qty) <= 0:
        print("❌ Số lượng phải là số > 0!")
        return

    qty = int(qty)

    # 5. Kiểm tra tồn kho
    if qty > product["quantity"]:
        print("❌ Số lượng vượt quá tồn kho!")
        return

    # 6. Thêm vào giỏ hàng buyer
    if buyer_username not in cart:
        cart[buyer_username] = []

    cart[buyer_username].append({
        "name": product["name"],
        "price": product["price"],
        "quantity": qty
    })

    save_cart(cart)

    print("✅ Đã thêm sản phẩm vào giỏ hàng!")

    # 7. Hiển thị lại giỏ hàng
    view_cart(buyer_username)
