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