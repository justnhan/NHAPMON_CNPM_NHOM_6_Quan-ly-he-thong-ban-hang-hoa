import json
import os

DATA_FILE = "users.json"

def buyer_menu(TenDangNhap):
    
    # Màu sắc
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    # Lời chào (không khung)
    print(f"\nXin chào {CYAN}{TenDangNhap}{RESET}!")
    print("Chúc bạn một ngày tốt lành!\n")

    # Menu có khung
    print(f"{CYAN}╔════════════════════════════╗{RESET}")
    print(f"{CYAN}║        MENU NGƯỜI MUA      ║{RESET}")
    print(f"{CYAN}╚════════════════════════════╝{RESET}")

    print(f"{YELLOW}1.{RESET} Xem danh sách sản phẩm")
    print(f"{YELLOW}2.{RESET} Tìm kiếm sản phẩm")
    print(f"{YELLOW}3.{RESET} Xem giỏ hàng")
    print(f"{YELLOW}4.{RESET} Xem đơn hàng đã mua")
    print(f"{YELLOW}0.{RESET} Đăng xuất")

    print("\nBạn muốn làm gì?")
    choice = input("Chọn chức năng: ")
    return choice

def seller_menu(TenDangNhap):

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

    print(f"{YELLOW}1.{RESET} Xem danh sách sản phẩm của bạn")
    print(f"{YELLOW}2.{RESET} Thêm sản phẩm mới")
    print(f"{YELLOW}3.{RESET} Sửa thông tin sản phẩm")
    print(f"{YELLOW}4.{RESET} Xóa sản phẩm")
    print(f"{YELLOW}5.{RESET} Xem đơn hàng của cửa hàng")
    print(f"{YELLOW}0.{RESET} Đăng xuất")

    print("\nBạn muốn làm gì?")
    choice = input("Chọn chức năng: ")
    return choice
    

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

def save_users():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


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

    if users[username]["role"] == "buyer":
        buyer_menu(username)
    else:
        seller_menu(username)
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
PRODUCT_FILE = "products.json"

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

def seller_menu(username):
    while True:
        print("\n=== MENU NGƯỜI BÁN ===")
        print("1. Thêm sản phẩm")
        print("2. Đổi mật khẩu")
        print("3. Thay đổi thông tin liên hệ")
        print("4. Đăng xuất")

        choice = input("Chọn: ").strip()

        if choice == "1":
            add_product(username)
        elif choice == "2":
            change_password(username)
        elif choice == "3":
            change_contact(username)
        elif choice == "4":
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

def buyer_menu(username):
    print("\n💬 Chức năng người mua sẽ được cập nhật sau!")
    input("Nhấn Enter để quay lại menu...")
    
def main():
    while True:
        print("\n=== MENU CHÍNH ===")
        print("1. Đăng nhập")
        print("2. Đăng ký")
        print("3. Quên mật khẩu")
        print("4. Thoát")

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


if __name__ == "__main__":
    main()
    main()
