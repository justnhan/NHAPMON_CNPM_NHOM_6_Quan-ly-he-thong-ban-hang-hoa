from feature_seller import *
from feature_buyer import *
from order_buyer import *
from feature_admin import *
from utils import format_money_vn
from seller_notification import *

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

def load_users():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

# --- Hàm giao diện người mua và người bán ---

def buyer_welcome(TenDangNhap):  
    # Màu sắc
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    users = load_users()   

    if TenDangNhap not in users:
        print("❌ Lỗi dữ liệu tài khoản!")
        return

    balance = users[TenDangNhap]["balance"]
    balance_str = format_money_vn(balance)
    # Lời chào và số dư
    print(f"\nXin chào {CYAN}{TenDangNhap}{RESET}  "
        f"[Số dư: {YELLOW}{balance_str}đ{RESET}]")
    print("Chúc bạn một ngày tốt lành!\n")

def seller_welcome(TenDangNhap):
        # Màu sắc
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    users = load_users()

    if TenDangNhap not in users:
        print("❌ Lỗi dữ liệu tài khoản!")
        return
    balance = users[TenDangNhap]["balance"]
    balance_str = format_money_vn(balance)
    # Lời chào (không khung)
    print(f"\nXin chào {CYAN}{TenDangNhap}{RESET}  "
        f"[Số dư: {YELLOW}{balance_str}đ{RESET}]")
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

    print(f"{YELLOW}1.{RESET} Xem toàn bộ sản phẩm hệ thống")
    print(f"{YELLOW}2.{RESET} Xem danh sách sản phẩm (theo đề xuất)")
    print(f"{YELLOW}3.{RESET} Tìm kiếm sản phẩm theo tên hàng")
    print(f"{YELLOW}4.{RESET} Tìm kiếm sản phẩm theo shop.")
    print(f"{YELLOW}5.{RESET} Xem giỏ hàng của tôi")
    print(f"{YELLOW}6.{RESET} Xem đơn hàng đã mua")
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
    print(f"{YELLOW}6.{RESET} Thông báo đơn hàng")
    print(f"{YELLOW}0.{RESET} Đăng xuất")

    print("\nBạn muốn làm gì?")
    choice = input("Chọn chức năng: ")
    return choice

def buyer_menu(username):
    buyer_welcome(username)
    while True:
        choice = buyer_giaodien()   # giữ nguyên hàm này
        if choice == "1":
            view_all_products(username)
            tiep_tuc()
            # gọi hàm tương ứng
        elif choice == "2":
            view_top_10_products(username)
            tiep_tuc()
        elif choice == "3":
            search_product(username)
            tiep_tuc()
        elif choice == "4":
            search_product_by_username()
            tiep_tuc()
        elif choice == "5":
            view_cart(username)
            tiep_tuc()
        elif choice == "6":
            view_order_history(username)
            tiep_tuc()
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
            tiep_tuc()
        elif choice == "2":
            add_product(username)
            tiep_tuc()
        elif choice == "3":
            edit_product(username)
            tiep_tuc()
        elif choice == "4":
            delete_product(username)
            tiep_tuc()
        elif choice == "5":
            print("Xem đơn hàng - chưa hoàn thiện")
            tiep_tuc()
        elif choice == "6":
            view_notifications(username)
            update_order_status(username)
            tiep_tuc()
        elif choice == "0":
            print("Đăng xuất...")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

def admin_welcome(TenDangNhap):
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    users = load_users()

    if TenDangNhap not in users:
        print("❌ Lỗi dữ liệu tài khoản!")
        return

    balance = users[TenDangNhap]["balance"]
    balance_str = format_money_vn(balance)
    print(f"\nXin chào {RED}ông chủ{RESET}  "
          f"[Số dư: {YELLOW}{balance_str}đ{RESET}]")

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
    admin_welcome(username)
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

def tiep_tuc():
    input("\nNhấn Enter để tiếp tục:")
