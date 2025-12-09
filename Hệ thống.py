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
