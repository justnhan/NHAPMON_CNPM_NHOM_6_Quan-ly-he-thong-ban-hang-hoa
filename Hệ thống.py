import json
import os

from ql_tai_khoan import *

# ----- Hàm Main và Hàm Đồ họa cơ bản -----
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


if __name__ == "__main__":
    main()

