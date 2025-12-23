def format_money_vn(amount):
    if isinstance(amount, int) or amount.is_integer():
        s = f"{int(amount):,}"
        return s.replace(",", ".")
    else:
        s = f"{amount:,.2f}"  # 1,234,567.89
        return s.replace(",", "X").replace(".", ",").replace("X", ".")
