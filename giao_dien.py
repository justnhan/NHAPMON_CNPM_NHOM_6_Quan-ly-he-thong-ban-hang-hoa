from feature_seller import *
from feature_buyer import *

# --- Hàm giao diện người mua và người bán ---

def buyer_welcome(TenDangNhap):  
    # Màu sắc
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    
    # Lời chào (không khung)
    print(f"\nXin chào {CYAN}{TenDangNhap}{RESET}!")
    print("Chúc bạn một ngày tốt lành!\n")
    print("\n--CHƯA HOÀN THIỆN CHỨC NĂNG--")

def seller_welcome(TenDangNhap):
        # Màu sắc
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    # Lời chào (không khung)
    print(f"\nXin chào {CYAN}{TenDangNhap}{RESET}!")
    print("Chúc bạn một ngày tốt lành!\n")

def buyer_giaodien():

    
    # Màu sắc
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    


    # Menu có khung
    print(f"{CYAN}╔════════════════════════════╗{RESET}")
    print(f"{CYAN}║        MENU NGƯỜI MUA      ║{RESET}")
    print(f"{CYAN}╚════════════════════════════╝{RESET}")

    print(f"{YELLOW}1.{RESET} Xem danh sách sản phẩm (Đề xuất)")
    print(f"{YELLOW}2.{RESET} Tìm kiếm sản phẩm")
    print(f"{YELLOW}3.{RESET} Xem giỏ hàng")
    print(f"{YELLOW}4.{RESET} Xem đơn hàng đã mua")
    print(f"{YELLOW}5.{RESET} Thêm sản phẩm vào giỏ hàng")
    print(f"{YELLOW}0.{RESET} Đăng xuất")

    print("\nBạn muốn làm gì?")
    choice = input("Chọn chức năng: ")
    return choice

def seller_giaodien():

    # Màu sắc
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    # Menu có khung
    print(f"{CYAN}╔════════════════════════════╗{RESET}")
    print(f"{CYAN}║        MENU NGƯỜI BÁN      ║{RESET}")
    print(f"{CYAN}╚════════════════════════════╝{RESET}")

    print(f"{YELLOW}1.{RESET} Xem danh sách sản phẩm của SHOP")
    print(f"{YELLOW}2.{RESET} Tìm để thêm sản phẩm mới")
    print(f"{YELLOW}3.{RESET} Sửa thông tin sản phẩm")
    print(f"{YELLOW}4.{RESET} Xóa sản phẩm")
    print(f"{YELLOW}5.{RESET} Xem đơn hàng của cửa hàng")
    print(f"{YELLOW}0.{RESET} Đăng xuất")

    print("\nBạn muốn làm gì?")
    choice = input("Chọn chức năng: ")
    return choice

def buyer_menu(username):
    buyer_welcome(username)
    while True:
        choice = buyer_giaodien()   # giữ nguyên hàm này
        if choice == "1":
            print("Bạn đã chọn: Xem danh sách sản phẩm - chưa hoàn thiện")
            # gọi hàm tương ứng
        elif choice == "2":
            search_product(username)
        elif choice == "3":
            view_cart(username)
        elif choice == "4":
            print("Bạn đã chọn: Xem đơn hàng đã mua - chưa hoàn thiện")
        elif choice == "5":
            add_to_cart(username)
        elif choice == "0":
            print("Đăng xuất...")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

def seller_menu(username):
    seller_welcome(username)
    while True:
        choice = seller_giaodien()
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


# Hàm giao diện Admin
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
