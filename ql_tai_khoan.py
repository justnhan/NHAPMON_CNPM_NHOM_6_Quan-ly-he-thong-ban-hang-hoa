import json
import os
import re

from giao_dien import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # thư mục chứa file .py
DATA_FILE = os.path.join(BASE_DIR, "users.json")       # users.json nằm cùng thư mục

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


# lưu thông tin tài khoản
def save_users():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


# ----- CÁC HÀM XỬ LÝ VẤN ĐỀ TÀI KHOẢN CƠ BẢN -----
def is_valid_gmail(email):
    """
    Kiểm tra email có đúng định dạng Gmail hay không
    Ví dụ hợp lệ: abc@gmail.com
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
    return re.match(pattern, email) is not None
def register():
    print("\n--- ĐĂNG KÝ TÀI KHOẢN ---")

    username = input("Tên tài khoản: ").strip()
    if username in users:
        print("❌ Tài khoản đã tồn tại!")
        return

    email = input("Email: ").strip()
    if not is_valid_gmail(email):
        print("❌ Email không hợp lệ! Vui lòng nhập đúng định dạng @gmail.com")
        return
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
        "role": role,
        "balance": 0
}

    save_users()
    print("✅ Đăng ký thành công vui lòng đăng nhập lại!")

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



# --- CÁC HÀM CHO QUẢN LÝ TÀI KHOẢN BẰNG ADMIN ----
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
