import os
# Lấy thư mục chứa file .py hiện tại
current_dir = os.path.dirname(os.path.abspath(__file__))

# Nối tên file taikhoan.inp vào thư mục này
File_Taikhoan = os.path.join(current_dir, "taikhoan.inp")

# Hàm lưu tài khoản mới vào file
def Dang_ky():
    print("\n--- ĐĂNG KÝ TÀI KHOẢN ---")
    username = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")

    # Chọn loại tài khoản
    print("Chọn loại tài khoản:")
    print("1. Người mua")
    print("2. Người bán")
    loai = input("Chọn (1/2): ")
    if loai == "1":
        role = 1
    elif loai == "2":
        role = 2
    else:
        print("Lựa chọn không hợp lệ! Đăng ký thất bại.\n")
        return

    # Kiểm tra trùng username
    with open(File_Taikhoan, "r") as f:
        for line in f:
            saved_user, _ = line.strip().split(":")
            if saved_user == username:
                print("Tên đăng nhập đã tồn tại! Hãy thử tên khác.\n")
                return

    # Lưu tài khoản mới (bổ sung role)
    with open(File_Taikhoan, "a") as f:
        f.write(f"{username}:{password}:{role}\n")

    print(f"Tạo tài khoản thành công! Loại tài khoản: {role}\n")


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
            saved_user, saved_pass, role = line.strip().split(":")
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
