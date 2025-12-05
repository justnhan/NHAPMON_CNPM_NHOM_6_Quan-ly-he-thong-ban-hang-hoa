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

    # Kiểm tra file tồn tại
    if not os.path.exists(File_Taikhoan):
        print("Chưa có tài khoản nào! Hãy đăng ký trước.\n")
        return False

    # Đọc file để tìm username trước
    saved_password = None
    with open(File_Taikhoan, "r") as f:
        for line in f:
            saved_user, saved_pass = line.strip().split(":")
            if saved_user == username:
                saved_password = saved_pass
                break

    # Không tìm thấy username
    if saved_password is None:
        print("Tên đăng nhập không tồn tại!\n")
        return False

    # Username đúng → bắt đầu kiểm tra mật khẩu với 3 lần thử
    Lanthu = 0
    while Lanthu < 3:
        password = input("Mật khẩu: ")

        if password == saved_password:
            print("Đăng nhập thành công!\n")
            return True
        else:
            Lanthu += 1
            if Lanthu < 3:
                print("Sai mật khẩu! Bạn còn" ,3 - Lanthu, "lần thử.\n")

    print("Bạn đã nhập sai mật khẩu quá 3 lần. Đăng nhập thất bại!\n")
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

if __name__=="__main__":
    Main()