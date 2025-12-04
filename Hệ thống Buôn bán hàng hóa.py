import os
File_Taikhoan = "taikhoan.inp"

# Hàm lưu tài khoản mới vào file
def Dang_ky():
    print("\n--- ĐĂNG KÝ TÀI KHOẢN ---")
    username = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")

    # Kiểm tra trùng username
    with open(File_Taikhoan, "r") as f:
        for line in f:
            saved_user, _ = line.strip().split(":")
            if saved_user == username:
                print("Tên đăng nhập đã tồn tại! Hãy thử tên khác.\n")
                return

    # Lưu tài khoản mới
    with open(File_Taikhoan, "a") as f:
        f.write(f"{username}:{password}\n")

    print("Tạo tài khoản thành công!\n")


# Hàm đăng nhập
def Dang_nhap():
    print("\n--- ĐĂNG NHẬP ---")
    username = input("Tên đăng nhập: ")
    password = input("Mật khẩu: ")

    # Đọc file kiểm tra
    if not os.path.exists(File_Taikhoan):
        print("Chưa có tài khoản nào! Hãy đăng ký trước.\n")
        return False

    with open(File_Taikhoan, "r") as f:
        for line in f:
            saved_user, saved_pass = line.strip().split(":")
            if saved_user == username and saved_pass == password:
                print("Đăng nhập thành công!\n")
                return True

    print("Sai tên đăng nhập hoặc mật khẩu!\n")
    return False


# Màn hình đầu tiên
def Main():
    while True:
        print("\n--- HỆ THỐNG ĐĂNG NHẬP ---")
        print("1. Đăng nhập")
        print("2. Tạo tài khoản")
        print("3. Thoát")
        choice = input("Chọn: ")

        if choice == "1":
            if Dang_nhap():
                return True   # cho phép vào hệ thống chính
        elif choice == "2":
            Dang_ky()
        elif choice == "3":
            print("Tạm biệt!")
            exit()
        else:
            print("Lựa chọn không hợp lệ!\n")