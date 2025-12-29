import json
import os
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ORDER_FILE = os.path.join(BASE_DIR, "orders.json")
REVIEW_FILE = os.path.join(BASE_DIR, "reviews.json")


# ---------- LOAD / SAVE ----------
def load_orders():
    if os.path.exists(ORDER_FILE):
        with open(ORDER_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
def load_reviews():
    if os.path.exists(REVIEW_FILE):
        with open(REVIEW_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
def save_reviews(data):
    with open(REVIEW_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def has_purchased(username, product_name):
    orders = load_orders()

    for order in orders:
        if order.get("username") != username:
            continue

        # CHỈ cho đánh giá khi HOÀN THÀNH
        if order.get("status", "").strip().lower() != "hoàn thành":
            continue

        for item in order.get("items", []):
            if item.get("name", "").strip().lower() == product_name.strip().lower():
                return True

    return False


def add_review(username, product_name):
    if not has_purchased(username, product_name):
        print("❌ Bạn chỉ có thể đánh giá sản phẩm đã mua!")
        return

    reviews = load_reviews()

    if product_name not in reviews:
        reviews[product_name] = []

    # kiểm tra đã đánh giá chưa
    for r in reviews[product_name]:
        if r["user"] == username:
            print("⚠️ Bạn đã đánh giá sản phẩm này rồi!")
            return

    try:
        stars = int(input("Chấm sao (1-5): "))
        if stars < 1 or stars > 5:
            raise ValueError
    except:
        print("❌ Số sao không hợp lệ!")
        return

    comment = input("Nhận xét (có thể bỏ trống): ").strip()

    reviews[product_name].append({
        "user": username,
        "stars": stars,
        "comment": comment,
        "date": datetime.now().strftime("%d/%m/%Y %H:%M")
    })

    save_reviews(reviews)
    print("✅ Đánh giá đã được gửi!")


def show_reviews(product_name):
    reviews = load_reviews()

    print(f"\n=== ⭐ ĐÁNH GIÁ SẢN PHẨM: {product_name} ===")

    if product_name not in reviews or not reviews[product_name]:
        print("Chưa có đánh giá nào.")
        return

    for r in reviews[product_name]:
        print("-" * 40)
        print(f"Người mua : {r['user']}")
        print(f"Số sao    : {r['stars']} ⭐")
        if r["comment"]:
            print(f"Nhận xét  : {r['comment']}")
        print(f"Ngày      : {r['date']}")

# ---------- SỬA / XÓA ĐÁNH GIÁ ----------
def edit_or_delete_review(username, product_name):
    reviews = load_reviews()

    if product_name not in reviews or not reviews[product_name]:
        print("❌ Không có đánh giá.")
        return

    for idx, r in enumerate(reviews[product_name]):
        if r.get("user") == username:
            print("\n1. Sửa đánh giá")
            print("2. Xóa đánh giá")
            choice = input("Chọn: ").strip()

            if choice == "1":
                try:
                    stars = int(input("Số sao mới (1-5): "))
                    if stars < 1 or stars > 5:
                        raise ValueError
                except:
                    print("❌ Số sao không hợp lệ!")
                    return

                comment = input("Nhận xét mới: ").strip()
                r["stars"] = stars
                r["comment"] = comment
                r["date"] = datetime.now().strftime("%d/%m/%Y %H:%M")

                save_reviews(reviews)
                print("✅ Đã cập nhật đánh giá!")
                return

            elif choice == "2":
                del reviews[product_name][idx]
                save_reviews(reviews)
                print("🗑️ Đã xóa đánh giá!")
                return

            else:
                print("❌ Lựa chọn không hợp lệ!")
                return

    print("❌ Bạn chưa đánh giá sản phẩm này.")
