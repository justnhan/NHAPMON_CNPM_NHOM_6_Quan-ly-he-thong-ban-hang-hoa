import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # thư mục chứa file .py

CART_FILE = os.path.join(BASE_DIR, "cart.json")  # cart.json nằm cùng thư mục

PRODUCT_FILE =  os.path.join(BASE_DIR, "products.json")     # products.json nằm cùng thư mục

# ------- Hàm tải dữ liệu Sản phẩm -------
def load_products():
    if os.path.exists(PRODUCT_FILE):
        try:
            with open(PRODUCT_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            print("⚠️ File sản phẩm lỗi. Tạo mới...")
            return {}
    return {}

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

    if username not in cart or len(cart[username]) == 0:
        print("🛒 Giỏ hàng trống!")
        return

    # 🔹 Tính độ rộng cột tên sản phẩm
    name_width = max(len(item["name"]) for item in cart[username])
    name_width = max(name_width, 20)  # tối thiểu 20 ký tự

    total = 0

    print(f"\n{'ID':<3} {'Tên sản phẩm':<{name_width}} {'Giá':<10} {'SL':<5} {'Thành tiền'}")
    print("-" * (name_width + 35))

    for idx, item in enumerate(cart[username]):
        name = item["name"]
        price = item["price"]
        qty = item["quantity"]
        money = price * qty
        total += money

        print(f"{idx:<3} {name:<{name_width}} {price:<10} {qty:<5} {money}")

    print("-" * (name_width + 35))
    print(f"💰 Tổng tiền tạm tính: {total} VND")
    
    print("\nBạn muốn làm gì?")
    print("1. Thay đổi số lượng")
    print("2. Xóa sản phẩm")
    print("0. Thoát")

    choice = input("Chọn: ")
    
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
        return

def add_to_cart(username):
    products = load_products()
    cart = load_cart()

    # 1. Kiểm tra có sản phẩm không
    if not products:
        print("❌ Hiện chưa có sản phẩm nào!")
        return

    # 2. Gom toàn bộ sản phẩm vào 1 danh sách
    all_products = []
    for seller, items in products.items():
        if isinstance(items, list):
            for item in items:
                # đảm bảo item hợp lệ
                if all(k in item for k in ("name", "price", "quantity")):
                    all_products.append(item)

    # Không có sản phẩm hợp lệ
    if not all_products:
        print("❌ Không có sản phẩm hợp lệ!")
        return

    # 3. Tính độ rộng cột tên sản phẩm (an toàn)
    name_width = max(
        (len(item["name"]) for item in all_products),
        default=20
    )
    name_width = max(name_width, 20)

    # 4. In danh sách sản phẩm
    print("\n=== DANH SÁCH SẢN PHẨM ===")
    print(f"{'ID':<3} {'Tên sản phẩm':<{name_width}} {'Giá':<10} {'Tồn kho'}")
    print("-" * (name_width + 30))

    for idx, item in enumerate(all_products):
        print(f"{idx:<3} {item['name']:<{name_width}} {item['price']:<10} {item['quantity']}")

    # 5. Nhập ID sản phẩm
    try:
        pid = int(input("\nNhập ID sản phẩm cần thêm: "))
        if pid < 0 or pid >= len(all_products):
            print("❌ ID sản phẩm không hợp lệ!")
            return
    except:
        print("❌ ID sản phẩm không hợp lệ!")
        return

    product = all_products[pid]

    # 6. Nhập số lượng
    qty = input("Nhập số lượng muốn mua: ").strip()
    if not qty.isdigit() or int(qty) <= 0:
        print("❌ Số lượng phải là số > 0!")
        return

    qty = int(qty)

    # 7. Kiểm tra tồn kho
    if qty > product["quantity"]:
        print("❌ Số lượng vượt quá tồn kho!")
        return

    # 8. Tạo giỏ hàng cho user nếu chưa có
    if username not in cart:
        cart[username] = []

    # 9. Nếu sản phẩm đã có trong giỏ → cộng số lượng
    for item in cart[username]:
        if item["name"] == product["name"]:
            item["quantity"] += qty
            save_cart(cart)
            print("✅ Đã cập nhật số lượng sản phẩm trong giỏ!")
            view_cart(username)
            return

    # 10. Nếu chưa có → thêm mới
    cart[username].append({
        "name": product["name"],
        "price": product["price"],
        "quantity": qty
    })

    save_cart(cart)
    print("✅ Đã thêm sản phẩm vào giỏ hàng!")

    # 11. Hiển thị lại giỏ hàng
    view_cart(username)

def search_product (username):
    products = load_products()
    cart = load_cart()

    if not products:
        print("❌ Hiện chưa có sản phẩm nào!")
        return

    keyword = input("🔍 Nhập tên sản phẩm cần tìm: ").strip().lower()
    if not keyword:
        print("❌ Từ khóa tìm kiếm không được để trống!")
        return

    # 1. Gom & lọc sản phẩm theo từ khóa
    matched_products = []

    for seller, items in products.items():
        if isinstance(items, list):
            for item in items:
                if (
                    isinstance(item, dict)
                    and all(k in item for k in ("name", "price", "quantity"))
                    and keyword in item["name"].lower()
                ):
                    matched_products.append(item)

    if not matched_products:
        print("❌ Không tìm thấy sản phẩm phù hợp!")
        return

    # 2. Tính độ rộng cột tên
    name_width = max(
        (len(item["name"]) for item in matched_products),
        default=20
    )
    name_width = max(name_width, 20)

    # 3. In kết quả tìm kiếm
    print("\n=== KẾT QUẢ TÌM KIẾM ===")
    print(f"{'ID':<3} {'Tên sản phẩm':<{name_width}} {'Giá':<10} {'Tồn kho'}")
    print("-" * (name_width + 30))

    for idx, item in enumerate(matched_products):
        print(f"{idx:<3} {item['name']:<{name_width}} {item['price']:<10} {item['quantity']}")

    # 4. Chọn sản phẩm
    try:
        pid = int(input("\nNhập ID sản phẩm muốn thêm: "))
        if pid < 0 or pid >= len(matched_products):
            print("❌ ID không hợp lệ!")
            return
    except:
        print("❌ ID không hợp lệ!")
        return

    product = matched_products[pid]

    # 5. Nhập số lượng
    qty = input("Nhập số lượng muốn mua: ").strip()
    if not qty.isdigit() or int(qty) <= 0:
        print("❌ Số lượng phải là số > 0!")
        return

    qty = int(qty)

    # 6. Kiểm tra tồn kho
    if qty > product["quantity"]:
        print("❌ Số lượng vượt quá tồn kho!")
        return

    # 7. Tạo giỏ hàng nếu chưa có
    if username not in cart:
        cart[username] = []

    # 8. Nếu sản phẩm đã có → cộng số lượng
    for item in cart[username]:
        if item["name"] == product["name"]:
            item["quantity"] += qty
            save_cart(cart)
            print("✅ Đã cập nhật số lượng trong giỏ!")
            view_cart(username)
            return

    # 9. Nếu chưa có → thêm mới
    cart[username].append({
        "name": product["name"],
        "price": product["price"],
        "quantity": qty
    })

    save_cart(cart)
    print("✅ Đã thêm sản phẩm vào giỏ!")

    view_cart(username)

# load & save đơn hàng
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

import time
import uuid

def place_order(username):
    products = load_products()
    cart = load_cart()
    orders = load_orders()

    # 1. Kiểm tra giỏ hàng
    if username not in cart or len(cart[username]) == 0:
        print("❌ Giỏ hàng trống, không thể đặt hàng!")
        return

    user_cart = cart[username]

    # 2. Kiểm tra tồn kho
    for cart_item in user_cart:
        found = False
        for seller, items in products.items():
            if isinstance(items, list):
                for product in items:
                    if product["name"] == cart_item["name"]:
                        found = True
                        if cart_item["quantity"] > product["quantity"]:
                            print(f"❌ Sản phẩm '{product['name']}' không đủ tồn kho!")
                            return
        if not found:
            print(f"❌ Sản phẩm '{cart_item['name']}' không còn tồn tại!")
            return

    # 3. Trừ tồn kho
    for cart_item in user_cart:
        for seller, items in products.items():
            if isinstance(items, list):
                for product in items:
                    if product["name"] == cart_item["name"]:
                        product["quantity"] -= cart_item["quantity"]

    # 4. Tạo mã đơn hàng
    order_id = f"DH{int(time.time())}{str(uuid.uuid4())[:4]}"

    # 5. Tính tổng tiền
    total = sum(item["price"] * item["quantity"] for item in user_cart)

          # 6. Tạo đơn hàng
    order_data = {
        "order_id": order_id,
        "username": username,
        "items": user_cart,
        "total": total,
        "status": "Đã đặt",
        "time": time.strftime("%d/%m/%Y %H:%M:%S")
    }

    # 7. Lưu đơn hàng
    if username not in orders:
        orders[username] = []

    orders[username].append(order_data)

    save_orders(orders)

    # 8. Lưu lại kho sau khi trừ
    with open(PRODUCT_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

    # 9. Xóa giỏ hàng
    cart[username] = []
    save_cart(cart)

    # 10. Thông báo thành công
    print("\n🎉 ĐẶT HÀNG THÀNH CÔNG!")
    print(f"🧾 Mã đơn hàng: {order_id}")
    print(f"💰 Tổng tiền: {total} VND")

def view_all_products():
    products = load_products()

    print("\n=== DANH SÁCH TOÀN BỘ SẢN PHẨM ===")

    # 1. Kiểm tra có sản phẩm không
    if not products:
        print("❌ Hiện chưa có sản phẩm nào!")
        return

    # 2. Gom toàn bộ sản phẩm hợp lệ
    all_products = []

    for seller, items in products.items():
        if isinstance(items, list):
            for item in items:
                if isinstance(item, dict) and all(k in item for k in ("name", "price", "quantity")):
                    all_products.append(item)

    if not all_products:
        print("❌ Không có sản phẩm hợp lệ!")
        return

    # 3. Tính độ rộng cột tên
    name_width = max(
        (len(item["name"]) for item in all_products),
        default=20
    )
    name_width = max(name_width, 20)

    # 4. In tiêu đề bảng
    print(f"\n{'ID':<3} {'Tên sản phẩm':<{name_width}} {'Giá':<10} {'Tồn kho'}")
    print("-" * (name_width + 30))

    # 5. In từng sản phẩm
    for idx, item in enumerate(all_products):
        print(f"{idx:<3} {item['name']:<{name_width}} {item['price']:<10} {item['quantity']}")

    print("-" * (name_width + 30))
    print(f"📦 Tổng số sản phẩm: {len(all_products)}")


def search_product_by_username():
    products = load_products()

    if not products:
        print("❌ Hiện chưa có sản phẩm nào!")
        return

    seller_username = input("👤 Nhập username người bán: ").strip()

    if not seller_username:
        print("❌ Username không được để trống!")
        return

    # 1. Kiểm tra người bán tồn tại
    if seller_username not in products or not isinstance(products[seller_username], list):
        print("❌ Không tìm thấy người bán này!")
        return

    seller_products = products[seller_username]

    if not seller_products:
        print("❌ Người bán này chưa có sản phẩm!")
        return

    # 2. Tính độ rộng cột tên
    name_width = max(
        (len(item["name"]) for item in seller_products),
        default=20
    )
    name_width = max(name_width, 20)

    # 3. In danh sách sản phẩm của người bán
    print(f"\n=== SẢN PHẨM CỦA NGƯỜI BÁN: {seller_username} ===")
    print(f"{'ID':<3} {'Tên sản phẩm':<{name_width}} {'Giá':<10} {'Tồn kho'}")
    print("-" * (name_width + 30))

    for idx, item in enumerate(seller_products):
        if all(k in item for k in ("name", "price", "quantity")):
            print(f"{idx:<3} {item['name']:<{name_width}} {item['price']:<10} {item['quantity']}")

    print("-" * (name_width + 30))
    print(f"📦 Tổng số sản phẩm: {len(seller_products)}")
