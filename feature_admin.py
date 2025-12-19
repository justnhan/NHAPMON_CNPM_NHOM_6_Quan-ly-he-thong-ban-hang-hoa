import  os
import json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # thư mục chứa file .py
DATA_FILE = os.path.join(BASE_DIR, "users.json")       # users.json nằm cùng thư mục
CART_FILE = os.path.join(BASE_DIR, "cart.json")  # cart.json nằm cùng thư mục

PRODUCT_FILE =  os.path.join(BASE_DIR, "products.json")     # products.json nằm cùng thư mục

# ------- Hàm tải dữ liệu Sản phẩm -------
def load_products():
    if os.path.exists(PRODUCT_FILE):
        try:
            with open(PRODUCT_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            print("⚠️ File sản phẩm lỗi. Tạo mới...")
            return {}
    return {}

# ------- Hàm tải dữ liệu Giỏ hàng -------
def load_cart():
    if os.path.exists(CART_FILE):
        try:
            with open(CART_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            print("⚠️ File giỏ hàng lỗi. Tạo mới...")
            return {}
    return {}
def save_cart(data):
    with open(CART_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
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



def show_sellers():
    print("\n--- DANH SÁCH NGƯỜI BÁN ---")
    sellers = [u for u, info in users.items() if info["role"] == "seller"]

    if not sellers:
        print("⚠️ Không có người bán nào.")
        return

    for s in sellers:
        print(f"- {s}")

def show_buyers():
    print("\n--- DANH SÁCH NGƯỜI MUA ---")
    buyers = [u for u, info in users.items() if info["role"] == "buyer"]

    if not buyers:
        print("⚠️ Không có người mua nào.")
        return

    for b in buyers:
        print(f"- {b}")

def show_all_products():
    products = load_products()

    print("\n--- TẤT CẢ SẢN PHẨM TRONG HỆ THỐNG ---")

    if not products:
        print("⚠️ Chưa có sản phẩm nào.")
        return

    for seller, plist in products.items():
        print(f"\n🔹 Người bán: {seller}")
        if not plist:
            print("   (Không có sản phẩm)")
            continue
        for p in plist:
            print(f"   - {p['name']} | Giá: {p['price']} | SL: {p['quantity']}")
def delete_user_by_role(role):
    print(f"\n--- DANH SÁCH {role.upper()} ---")
    ds = [u for u, info in users.items() if info["role"] == role]

    if not ds:
        print("⚠️ Không có tài khoản nào.")
        return

    for i, u in enumerate(ds):
        print(f"{i}. {u}")

    try:
        idx = int(input("\nNhập ID muốn xóa: ").strip())
    except:
        print("❌ ID không hợp lệ!")
        return

    if idx < 0 or idx >= len(ds):
        print("❌ Không tồn tại ID này!")
        return

    user_delete = ds[idx]
    del users[user_delete]
    save_users()

    print(f"✅ Đã xóa: {user_delete}")
    for username, info in users.items():
        print(f"• Tên tài khoản:{username}")
        print(f"  Mật khẩu : {info['password']}")
        print(f"  Email    : {info['email']}")
        print(f"  SĐT      : {info['phone']}")
        print(f"  Vai trò  : {info['role']}")
        print("----------------------------------")
