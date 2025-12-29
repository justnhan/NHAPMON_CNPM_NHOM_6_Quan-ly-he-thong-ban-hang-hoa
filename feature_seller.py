import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # thư mục chứa file .py

PRODUCT_FILE =  os.path.join(BASE_DIR, "products.json")       # products.json nằm cùng thư mục

REVIEW_FILE = os.path.join(BASE_DIR, "reviews.json")

DISCOUNT_FILE = os.path.join(BASE_DIR, "discount.json")

def load_discount():
    if os.path.exists(DISCOUNT_FILE):
        try:
            with open(DISCOUNT_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            print("⚠️ File discount lỗi. Tạo mới...")
    return {
        "type": "percent",
        "value": 0,
        "active": False
    }

def save_discount(data):
    with open(DISCOUNT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# ------- Hàm tải dữ liệu Đánh giá -------
def load_reviews():
    if os.path.exists(REVIEW_FILE):
        try:
            with open(REVIEW_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            print("⚠️ File đánh giá lỗi. Tạo mới...")
            return {}
    return {}


def save_reviews(data):
    with open(REVIEW_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


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
    if username not in products or not products[username]:
        print(f"{RED}❌ Bạn chưa có sản phẩm nào.{RESET}")
        return

    seller_products = products[username]

    # 🔹 Tính độ rộng cột tên (auto, tối thiểu 25)
    name_width = max(
        len(item.get("name", "")) for item in seller_products
    )
    name_width = max(name_width, 25)

    # Header
    print(f"{YELLOW}{'-' * (name_width + 45)}{RESET}")
    print(
        f"{GREEN}"
        f"{'ID':<5} "
        f"{'Tên sản phẩm':<{name_width}} "
        f"{'Giá':>12} "
        f"{'Tồn kho':>10} "
        f"{'Đã bán':>10}"
        f"{RESET}"
    )
    print(f"{YELLOW}{'-' * (name_width + 45)}{RESET}")

    # In sản phẩm
    for idx, item in enumerate(seller_products, start=1):
        name = item.get("name", "Không tên")
        price = item.get("price", 0)
        qty = item.get("quantity", 0)
        sold = item.get("total_purchased", 0)

        print(
            f"{idx:<5} "
            f"{name:<{name_width}} "
            f"{price:>12,} "
            f"{qty:>10} "
            f"{sold:>10}"
        )

    print(f"{YELLOW}{'-' * (name_width + 45)}{RESET}")


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

# ------- Hàm đánh giá sản phẩm -------

def get_average_rating(product_name):
    reviews = load_reviews()

    if product_name not in reviews or not reviews[product_name]:
        return 0

    total = sum(r["stars"] for r in reviews[product_name])
    return round(total / len(reviews[product_name]), 1)

def count_reviews(product_name):
    reviews = load_reviews()
    return len(reviews.get(product_name, []))

def view_product_reviews(product_name):
    reviews = load_reviews()

    print(f"\n⭐ ĐÁNH GIÁ SẢN PHẨM: {product_name}")

    if product_name not in reviews or not reviews[product_name]:
        print("Chưa có đánh giá nào.")
        return

    avg = get_average_rating(product_name)
    total = count_reviews(product_name)

    print(f"⭐ Trung bình: {avg} / 5 ({total} đánh giá)\n")

    for r in reviews[product_name]:
        print("-" * 40)
        print(f"Người mua : {r['user']}")
        print(f"Số sao    : {r['stars']} ⭐")
        if r["comment"]:
            print(f"Nhận xét  : {r['comment']}")
        print(f"Ngày      : {r['date']}")

def view_all_reviews_of_seller(username):
    products = load_products()
    reviews = load_reviews()

    if username not in products or not products[username]:
        print("❌ Bạn chưa có sản phẩm nào.")
        return

    print("\n====== ĐÁNH GIÁ về SẢN PHẨM CỦA BẠN ======\n")

    for item in products[username]:
        name = item["name"]

        avg = get_average_rating(name)
        total = count_reviews(name)

        print(f"📦 {name}")
        print(f"⭐ Trung bình: {avg} / 5 ({total} đánh giá)")

        if name in reviews:
            for r in reviews[name]:
                print(f"  - {r['user']} | {r['stars']}⭐ | {r['comment']}")
        else:
            print("  (Chưa có đánh giá)")
        print("-" * 40)

def viewsp(username):
    products = load_products()

    # 1. Kiểm tra seller có sản phẩm không
    if username not in products or not products[username]:
        print("❌ Bạn chưa có sản phẩm nào.")
        return

    seller_products = products[username]

    # 2. Hiển thị danh sách sản phẩm
    print("\n--- CHỌN SẢN PHẨM ĐỂ XEM ĐÁNH GIÁ ---")
    for idx, item in enumerate(seller_products):
        print(f"{idx}. {item['name']}")

    # 3. Chọn ID
    try:
        product_id = int(input("\nNhập ID sản phẩm: ").strip())
    except:
        print("❌ ID không hợp lệ!")
        return

    # 4. Kiểm tra ID
    if product_id < 0 or product_id >= len(seller_products):
        print("❌ Không tồn tại sản phẩm này!")
        return

    product_name = seller_products[product_id]["name"]

    # 5. Xem đánh giá
    view_product_reviews(product_name)

# Thêm mã giảm giá theo phần trăm cho toàn bộ sản phẩm của seller
def apply_discount_seller(username, percent):
    products = load_products()

    if username not in products or not products[username]:
        print("❌ Bạn chưa có sản phẩm nào.")
        return

    if percent <= 0 or percent >= 100:
        print("❌ % giảm không hợp lệ.")
        return

    for item in products[username]:
        # Lưu giá gốc nếu chưa có
        if "original_price" not in item:
            item["original_price"] = item["price"]

        item["price"] = int(item["original_price"] * (100 - percent) / 100)

    save_products(products)
    print(f"✅ Đã giảm {percent}% cho toàn bộ sản phẩm.")

# thêm mã giảm giá theo số tiền cố định
def apply_fixed_discount_seller(username, amount):
    products = load_products()

    if username not in products or not products[username]:
        print("❌ Bạn chưa có sản phẩm nào.")
        return

    if amount <= 0:
        print("❌ Số tiền giảm không hợp lệ.")
        return

    for item in products[username]:
        if "original_price" not in item:
            item["original_price"] = item["price"]

        item["price"] = max(0, item["original_price"] - amount)

    save_products(products)
    print(f"✅ Đã giảm {amount:,} cho toàn bộ sản phẩm.")

def remove_discount_seller(username):
    products = load_products()

    if username not in products or not products[username]:
        print("❌ Bạn chưa có sản phẩm nào.")
        return

    for item in products[username]:
        if "original_price" in item:
            item["price"] = item["original_price"]
            del item["original_price"]

    save_products(products)
    print("✅ Đã khôi phục giá gốc cho toàn bộ sản phẩm.")

