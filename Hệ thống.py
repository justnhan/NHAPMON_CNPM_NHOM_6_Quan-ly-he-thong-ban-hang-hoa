import json
import os

#Cấu trúc lưu trữ dữ liệu
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # thư mục chứa file .py
DATA_FILE = os.path.join(BASE_DIR, "users.json")       # users.json nằm cùng thư mục
PRODUCT_FILE =  os.path.join(BASE_DIR, "products.json")       # products.json nằm cùng thư mục


# CÁC HÀM ĐƯỢC SỬ DỤNG
#---------------------------------------------------------------------------------------------
def buyer_giaodien(TenDangNhap):
    
    # Màu sắc
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    
    # Lời chào (không khung)
    print(f"\nXin chào {CYAN}{TenDangNhap}{RESET}!")
    print("Chúc bạn một ngày tốt lành!\n")
    print("\n--CHƯA HOÀN THIỆN CHỨC NĂNG--")

    # Menu có khung
    print(f"{CYAN}╔════════════════════════════╗{RESET}")
    print(f"{CYAN}║        MENU NGƯỜI MUA      ║{RESET}")
    print(f"{CYAN}╚════════════════════════════╝{RESET}")

    print(f"{YELLOW}1.{RESET} Xem danh sách sản phẩm (Đề xuất)")
    print(f"{YELLOW}2.{RESET} Tìm kiếm sản phẩm")
    print(f"{YELLOW}3.{RESET} Xem giỏ hàng")
    print(f"{YELLOW}4.{RESET} Xem đơn hàng đã mua")
    print(f"{YELLOW}0.{RESET} Đăng xuất")

    print("\nBạn muốn làm gì?")
    choice = input("Chọn chức năng: ")
    return choice

def buyer_menu(username):
    while True:
        choice = buyer_giaodien(username)   # giữ nguyên hàm này
        if choice == "1":
            print("Bạn đã chọn: Xem danh sách sản phẩm - chưa hoàn thiện")
            # gọi hàm tương ứng
        elif choice == "2":
            print("Bạn đã chọn: Tìm kiếm sản phẩm - chưa hoàn thiện")
        elif choice == "3":
            print("Bạn đã chọn: Xem giỏ hàng - chưa hoàn thiện")
        elif choice == "4":
            print("Bạn đã chọn: Xem đơn hàng đã mua - chưa hoàn thiện")
        elif choice == "0":
            print("Đăng xuất...")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")


def seller_giaodien(TenDangNhap):

    # Màu sắc
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    # Lời chào (không khung)
    print(f"\nXin chào {CYAN}{TenDangNhap}{RESET}!")
    print("Chúc bạn một ngày tốt lành!\n")

    # Menu có khung
    print(f"{CYAN}╔════════════════════════════╗{RESET}")
    print(f"{CYAN}║        MENU NGƯỜI BÁN      ║{RESET}")
    print(f"{CYAN}╚════════════════════════════╝{RESET}")

    print(f"{YELLOW}1.{RESET} Xem danh sách sản phẩm của SHOP")
    print(f"{YELLOW}2.{RESET} Thêm sản phẩm mới")
    print(f"{YELLOW}3.{RESET} Sửa thông tin sản phẩm")
    print(f"{YELLOW}4.{RESET} Xóa sản phẩm")
    print(f"{YELLOW}5.{RESET} Xem đơn hàng của cửa hàng")
    print(f"{YELLOW}0.{RESET} Đăng xuất")

    print("\nBạn muốn làm gì?")
    choice = input("Chọn chức năng: ")
    return choice

def seller_menu(username):
    while True:
        choice = seller_giaodien(username)
        if choice == "1":
            view_products_seller(username)
        elif choice == "2":
            add_product(username)
        elif choice == "3":
            edit_product(username)
        elif choice == "4":
            delete_product(username)
        elif choice == "5":
            print("Xem đơn hàng - chưa hoàn thiện")
        elif choice == "0":
            print("Đăng xuất...")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")




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

def save_users():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


# --- TẢI DỮ LIỆU NGƯỜI DÙNG ---
if os.path.exists(DATA_FILE):
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            users = json.load(f)
    except Exception as e:
        print("LỖI LOAD JSON:", e)
        print("→ File users.json có vấn đề, hệ thống sẽ bỏ qua và dùng dữ liệu rỗng.")
        users = {}

else:
    users = {}
# --- TẠO ADMIN MẶC ĐỊNH ---
if "admin" not in users:
    users["admin"] = {
        "password": "admin123",
        "email": "admin@gmail.com",
        "phone": "0000000000",
        "role": "admin"
    }
    save_users()

def admin_giaodien():
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    print(f"\n{CYAN}╔════════════════════════════╗{RESET}")
    print(f"{CYAN}║        MENU ADMIN          ║{RESET}")
    print(f"{CYAN}╚════════════════════════════╝{RESET}")

    print(f"{YELLOW}1.{RESET} Hiển thị tất cả người bán")
    print(f"{YELLOW}2.{RESET} Hiển thị tất cả người mua")
    print(f"{YELLOW}3.{RESET} Hiển thị tất cả sản phẩm")
    print(f"{YELLOW}4.{RESET} Xóa tài khoản người bán")
    print(f"{YELLOW}5.{RESET} Xóa tài khoản người mua")
    print(f"{YELLOW}0.{RESET} Đăng xuất")

    return input("Chọn chức năng: ")

def admin_menu(username):
    while True:
        choice = admin_giaodien()

        if choice == "1":
            show_sellers()
        elif choice == "2":
            show_buyers()
        elif choice == "3":
            show_all_products()
        elif choice == "4":
            delete_user_by_role("seller")
        elif choice == "5":
            delete_user_by_role("buyer")
        elif choice == "0":
            print("Đăng xuất...")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")


def register():
    print("\n--- ĐĂNG KÝ TÀI KHOẢN ---")

    username = input("Tên tài khoản: ").strip()
    if username in users:
        print("❌ Tài khoản đã tồn tại!")
        return

    email = input("Email: ").strip()
    phone = input("Số điện thoại: ").strip()

    password = input("Mật khẩu: ").strip()
    repass = input("Nhập lại mật khẩu: ").strip()

    if password != repass:
        print("❌ Mật khẩu không khớp!")
        return

    print("\nLoại tài khoản:")
    print("1. Người bán")
    print("2. Người mua")
    role_choice = input("Chọn (1/2): ").strip()

    role = "seller" if role_choice == "1" else "buyer"

    # Lưu dữ liệu
    users[username] = {
        "password": password,
        "email": email,
        "phone": phone,
        "role": role
    }

    save_users()
    print("✅ Đăng ký thành công!")

def login():
    print("\n--- ĐĂNG NHẬP ---")
    username = input("Tên tài khoản: ").strip()
    password = input("Mật khẩu: ").strip()

    if username not in users:
        print("❌ Tài khoản không tồn tại!")
        return

    if users[username]["password"] != password:
        print("❌ Sai mật khẩu!")
        return

    print("✅ Đăng nhập thành công!")

    role = users[username]["role"]

    if role == "buyer":
        buyer_menu(username)
    elif role == "seller":
        seller_menu(username)
    elif role == "admin":
        admin_menu(username)

#   THAY ĐỔI THÔNG TIN
def change_password(username):
    print("\n--- ĐỔI MẬT KHẨU ---")
    old = input("Mật khẩu cũ: ").strip()

    if old != users[username]["password"]:
        print("❌ Sai mật khẩu cũ!")
        return

    new = input("Mật khẩu mới: ").strip()
    rep = input("Nhập lại mật khẩu mới: ").strip()

    if new != rep:
        print("❌ Mật khẩu không trùng khớp!")
        return

    users[username]["password"] = new
    save_users()
    print("✅ Đổi mật khẩu thành công!")


def forgot_password():
    print("\n--- QUÊN MẬT KHẨU ---")
    username = input("Nhập tên tài khoản: ").strip()

    if username not in users:
        print("❌ Không tồn tại tài khoản này!")
        return

    phone = input("Nhập số điện thoại đã đăng ký: ").strip()

    if phone != users[username]["phone"]:
        print("❌ Số điện thoại không khớp!")
        return

    newpass = input("Nhập mật khẩu mới: ").strip()
    rep = input("Nhập lại mật khẩu mới: ").strip()

    if newpass != rep:
        print("❌ Mật khẩu không khớp!")
        return

    users[username]["password"] = newpass
    save_users()
    print("✅ Khôi phục mật khẩu thành công!")


def change_contact(username):
    print("\n--- THAY ĐỔI THÔNG TIN LIÊN HỆ ---")
    print("1. Thay đổi email")
    print("2. Thay đổi số điện thoại")
    choice = input("Chọn: ").strip()

    if choice == "1":
        new_email = input("Nhập email mới: ").strip()
        users[username]["email"] = new_email
        print("✅ Đổi email thành công!")
    elif choice == "2":
        new_phone = input("Nhập số điện thoại mới: ").strip()
        users[username]["phone"] = new_phone
        print("✅ Đổi số điện thoại thành công!")
    else:
        print("❌ Lựa chọn không hợp lệ!")

    save_users()


def load_products():
    if os.path.exists(PRODUCT_FILE):
        try:
            with open(PRODUCT_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            print("⚠️ File sản phẩm lỗi. Tạo mới...")
            return {}
    return {}

def save_products(data):
    with open(PRODUCT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

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


def show_logo():
    # Màu ANSI
    PINK = "\033[95m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    print()
    print(f"{PINK}{BOLD}(づ｡◕‿‿◕｡)づ  💖  CHÀO MỪNG ĐẾN VỚI SHOP 💖{RESET}")

def main():
    while True:
        show_logo()
        # Màu ANSI
        CYAN = "\033[96m"
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        BLUE = "\033[94m"
        RESET = "\033[0m"
        BOLD = "\033[1m"

        WIDTH = 42  # chiều rộng phần trong khung

        print("\n" + CYAN + "╔" + "═" * WIDTH + "╗" + RESET)

        line1 = "👋👋👋👋"
        print(CYAN + "║" + RESET + f"{line1.center(WIDTH)}" + CYAN + "║" + RESET)

        line2 = "Hệ thống Bán hàng"
        print(CYAN + "║" + RESET + f"{line2.center(WIDTH)}" + CYAN + "║" + RESET)

        print(CYAN + "╠" + "═" * WIDTH + "╣" + RESET)

        title = "🌟 MENU CHÍNH 🌟"
        print(CYAN + "║" + RESET + BOLD + BLUE + f"{title.center(WIDTH)}" + RESET + CYAN + "║" + RESET)

        print(CYAN + "╠" + "═" * WIDTH + "╣" + RESET)

        print(CYAN + "║" + RESET + f"1. Đăng nhập".ljust(WIDTH) + CYAN + "║" + RESET)
        print(CYAN + "║" + RESET + f"2. Đăng ký".ljust(WIDTH) + CYAN + "║" + RESET)
        print(CYAN + "║" + RESET + f"3. Quên mật khẩu".ljust(WIDTH) + CYAN + "║" + RESET)
        print(CYAN + "║" + RESET + f"4. Thoát".ljust(WIDTH) + CYAN + "║" + RESET)

        print(CYAN + "╚" + "═" * WIDTH + "╝" + RESET)

        choice = input("Lựa chọn: ")

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            forgot_password()
        elif choice == "4":
            print("Thoát chương trình...")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

def show_sellers():
    print("\n--- DANH SÁCH NGƯỜI BÁN ---")
    sellers = [u for u, info in users.items() if info["role"] == "seller"]

    if not sellers:
        print("⚠️ Không có người bán nào.")
        return

    for s in sellers:
        print(f"- {s}")

def show_buyers():
    print("\n--- DANH SÁCH NGƯỜI MUA ---")
    buyers = [u for u, info in users.items() if info["role"] == "buyer"]

    if not buyers:
        print("⚠️ Không có người mua nào.")
        return

    for b in buyers:
        print(f"- {b}")

def show_all_products():
    products = load_products()

    print("\n--- TẤT CẢ SẢN PHẨM TRONG HỆ THỐNG ---")

    if not products:
        print("⚠️ Chưa có sản phẩm nào.")
        return

    for seller, plist in products.items():
        print(f"\n🔹 Người bán: {seller}")
        if not plist:
            print("   (Không có sản phẩm)")
            continue
        for p in plist:
            print(f"   - {p['name']} | Giá: {p['price']} | SL: {p['quantity']}")
def delete_user_by_role(role):
    print(f"\n--- DANH SÁCH {role.upper()} ---")
    ds = [u for u, info in users.items() if info["role"] == role]

    if not ds:
        print("⚠️ Không có tài khoản nào.")
        return

    for i, u in enumerate(ds):
        print(f"{i}. {u}")

    try:
        idx = int(input("\nNhập ID muốn xóa: ").strip())
    except:
        print("❌ ID không hợp lệ!")
        return

    if idx < 0 or idx >= len(ds):
        print("❌ Không tồn tại ID này!")
        return

    user_delete = ds[idx]
    del users[user_delete]
    save_users()

    print(f"✅ Đã xóa: {user_delete}")
    for username, info in users.items():
        print(f"{YELLOW}• Tên tài khoản:{RESET} {username}")
        print(f"  Mật khẩu : {info['password']}")
        print(f"  Email    : {info['email']}")
        print(f"  SĐT      : {info['phone']}")
        print(f"  Vai trò  : {info['role']}")
        print("----------------------------------")
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

CART_FILE = os.path.join(BASE_DIR, "cart.json")

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

    choice = input("Chọn: ")
if __name__ == "__main__":
    main()

