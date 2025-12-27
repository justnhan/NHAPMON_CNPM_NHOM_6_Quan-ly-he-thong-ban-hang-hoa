DISCOUNT_FILE = os.path.join(BASE_DIR, "discounts.json")

def load_discounts():
    if os.path.exists(DISCOUNT_FILE):
        try:
            with open(DISCOUNT_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_discounts(data):
    with open(DISCOUNT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
import time

def discount_all_products(username):
    products = load_products()
    discounts = load_discounts()

    if username not in products or not products[username]:
        print("❌ Bạn chưa có sản phẩm!")
        return

    print("1. Giảm theo %")
    print("2. Giảm theo số tiền")

    choice = input("Chọn kiểu giảm: ").strip()

    value = input("Nhập giá trị giảm: ").strip()
    if not value.isdigit() or int(value) <= 0:
        print("❌ Giá trị không hợp lệ!")
        return

    value = int(value)
    discount_type = "percent" if choice == "1" else "amount"
    start_time = time.strftime("%d/%m/%Y %H:%M:%S")

    if username not in discounts:
        discounts[username] = {}

    for idx, _ in enumerate(products[username]):
        discounts[username][str(idx)] = {
            "type": discount_type,
            "value": value,
            "start_time": start_time
        }

    save_discounts(discounts)
    print("✅ Đã áp dụng giảm giá cho toàn bộ sản phẩm!")
def discount_single_product(username):
    products = load_products()
    discounts = load_discounts()

    if username not in products or not products[username]:
        print("❌ Bạn chưa có sản phẩm!")
        return

    for idx, item in enumerate(products[username]):
        print(f"{idx}. {item['name']} - {item['price']:,} VND")

    try:
        pid = int(input("Chọn ID sản phẩm: "))
    except:
        print("❌ ID không hợp lệ!")
        return

    if pid < 0 or pid >= len(products[username]):
        print("❌ Không tồn tại sản phẩm!")
        return

    print("1. Giảm theo %")
    print("2. Giảm theo số tiền")

    choice = input("Chọn kiểu giảm: ").strip()
    value = input("Nhập giá trị giảm: ").strip()

    if not value.isdigit() or int(value) <= 0:
        print("❌ Giá trị không hợp lệ!")
        return

    discount_type = "percent" if choice == "1" else "amount"
    start_time = time.strftime("%d/%m/%Y %H:%M:%S")

    if username not in discounts:
        discounts[username] = {}

    discounts[username][str(pid)] = {
        "type": discount_type,
        "value": int(value),
        "start_time": start_time
    }

    save_discounts(discounts)
    print("✅ Đã áp dụng giảm giá cho sản phẩm!")
def get_discounted_price(seller, product_id, price):
    discounts = load_discounts()

    if seller not in discounts:
        return price, None

    if str(product_id) not in discounts[seller]:
        return price, None

    d = discounts[seller][str(product_id)]

    if d["type"] == "percent":
        new_price = price * (100 - d["value"]) // 100
    else:
        new_price = max(0, price - d["value"])

    return new_price, d
def view_all_discounts():
    discounts = load_discounts()
    products = load_products()

    print("\n=== DANH SÁCH GIẢM GIÁ ===")

    if not discounts:
        print("❌ Chưa có giảm giá nào!")
        return

    print(f"{'Seller':<15} {'SP':<5} {'Loại':<10} {'Giá trị':<10} {'Thời gian'}")
    print("-" * 70)

    for seller, items in discounts.items():
        for pid, d in items.items():
            discount_type = "%" if d["type"] == "percent" else "VND"
            value = f"{d['value']}{discount_type}"
            time = d["start_time"]

            print(f"{seller:<15} {pid:<5} {d['type']:<10} {value:<10} {time}")
