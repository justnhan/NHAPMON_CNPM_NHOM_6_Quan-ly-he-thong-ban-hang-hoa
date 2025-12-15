import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # thư mục chứa file .py

PRODUCT_FILE =  os.path.join(BASE_DIR, "products.json")       # products.json nằm cùng thư mục


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

# ------- Hàm lưu dữ liệu Sản phẩm
def save_products(data):
    with open(PRODUCT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def view_products_seller(username):
    # Màu ANSI
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"

    products = load_products()

    print(f"\n{CYAN}====== ĐÂY LÀ DANH SÁCH SẢN PHẨM CỦA BẠN ======{RESET}\n")

    # Kiểm tra có sản phẩm không
    if username not in products or len(products[username]) == 0:
        print(f"{RED}❌ Bạn chưa có sản phẩm nào.{RESET}")
        return

    # Header
    print(f"{YELLOW}{'-'*60}{RESET}")
    print(f"{GREEN}{'ID':<5} {'Tên sản phẩm':<25} {'Giá':<12} {'Số lượng':<10}{RESET}")
    print(f"{YELLOW}{'-'*60}{RESET}")

    # In sản phẩm
    for idx, item in enumerate(products[username], start=1):
        name = item.get("name", "Không tên")
        price = item.get("price", 0)
        qty = item.get("quantity", 0)

        print(f"{idx:<5} {name:<25} {price:<12} {qty:<10}")

    print(f"{YELLOW}{'-'*60}{RESET}")






def add_product(username):
    print("\n--- THÊM SẢN PHẨM ---")
    name = input("Tên sản phẩm: ").strip()
    price = input("Giá: ").strip()
    quantity = input("Số lượng: ").strip()

    if not name or not price.isdigit() or not quantity.isdigit():
        print("❌ Giá và số lượng phải là số > 0.")
        return

    price = int(price)
    quantity = int(quantity)

    if price <= 0 or quantity <= 0:
        print("❌ Giá và số lượng phải > 0.")
        return

    products = load_products()

    if username not in products:
        products[username] = []

    new_item = {"name": name, "price": price, "quantity": quantity}

    products[username].append(new_item)
    save_products(products)

    print("✅ Thêm sản phẩm thành công!")



def edit_product(username):

    print("\n--- CHỈNH SỬA SẢN PHẨM ---")

    products = load_products()

    # Kiểm tra seller có sản phẩm hay chưa
    if username not in products or len(products[username]) == 0:
        print("❌ Bạn chưa có sản phẩm nào để sửa!")
        return

    # Hiển thị danh sách sản phẩm với ID
    print("\nDanh sách sản phẩm:")
    for idx, item in enumerate(products[username]):
        print(f"{idx}. {item['name']} - Giá: {item['price']} - SL: {item['quantity']}")

    # Nhập ID sản phẩm
    try:
        product_id = int(input("\nNhập ID sản phẩm cần sửa: ").strip())
    except:
        print("❌ ID không hợp lệ!")
        return

    # Kiểm tra ID hợp lệ
    if product_id < 0 or product_id >= len(products[username]):
        print("❌ Không tồn tại sản phẩm này!")
        return

    sp = products[username][product_id]

    print("\n--- Thông tin cũ ---")
    print(f"Tên hiện tại: {sp['name']}")
    print(f"Giá hiện tại: {sp['price']}")
    print(f"Số lượng hiện tại: {sp['quantity']}")

    print("\nNhấn Enter để giữ nguyên giá trị cũ.")

    # Nhập dữ liệu mới
    new_name = input("Tên mới: ").strip()
    new_price = input("Giá mới: ").strip()
    new_quantity = input("Số lượng mới: ").strip()

    # Xử lý tên
    if new_name != "":
        sp["name"] = new_name

    # Xử lý giá
    if new_price != "":
        if not new_price.isdigit() or int(new_price) <= 0:
            print("❌ Giá phải là số > 0")
            return
        sp["price"] = int(new_price)

    # Xử lý số lượng
    if new_quantity != "":
        if not new_quantity.isdigit() or int(new_quantity) <= 0:
            print("❌ Số lượng phải là số > 0")
            return
        sp["quantity"] = int(new_quantity)

    # Lưu file
    save_products(products)

    print("✅ Cập nhật sản phẩm thành công!")

def delete_product(username):
    print("\n--- XÓA SẢN PHẨM ---")

    products = load_products()

    # 1. Kiểm tra seller có sản phẩm không
    if username not in products or len(products[username]) == 0:
        print("❌ Bạn không có sản phẩm nào để xóa!")
        return

    # 2. Hiển thị danh sách sản phẩm kèm ID
    print("\nDanh sách sản phẩm:")
    for idx, item in enumerate(products[username]):
        print(f"{idx}. {item['name']} - Giá: {item['price']} - SL: {item['quantity']}")

    # 3. Nhập ID sản phẩm cần xóa
    try:
        product_id = int(input("\nNhập ID sản phẩm cần xóa: ").strip())
    except:
        print("❌ ID không hợp lệ!")
        return

    # 4. Kiểm tra ID có hợp lệ không
    if product_id < 0 or product_id >= len(products[username]):
        print("❌ Không tồn tại sản phẩm này!")
        return

    sp = products[username][product_id]

    # 5. Xác nhận xóa
    print(f"\nBạn có chắc chắn muốn xóa sản phẩm:")
    print(f"➡ {sp['name']} (Giá: {sp['price']}, SL: {sp['quantity']})")
    confirm = input("Nhập 'YES' để xác nhận xóa: ").strip()

    if confirm != "YES":
        print("⛔ Hủy thao tác xóa.")
        return

    # 6. Xóa sản phẩm
    del products[username][product_id]

    # 7. Cập nhật file
    save_products(products)

    print("✅ Xóa sản phẩm thành công!")