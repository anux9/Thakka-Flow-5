def add_vat(amount, rate=0.15):
    return round(amount * (1 + rate), 2)


def format_price(amount):
    return f"{amount:,.2f} SAR"


def is_valid_phone(phone):
    phone = phone.replace(" ", "")

    if phone.isdigit() and phone.startswith("05") and len(phone) == 10:
        return True
    else:
        return False


# اختبار الدوال
print(add_vat(1000))
print(add_vat(500, 0.10))
print(add_vat(200, 0.15))

print(format_price(1234.5))
print(format_price(500))
print(format_price(10000))

print(is_valid_phone("0551234567"))
print(is_valid_phone("0661234567"))
print(is_valid_phone("05512"))


# استخدام الدوال مع بعضها
print(format_price(add_vat(1000)))


# التحقق من أرقام الجوال
phones = ["0551234567", "0661234567", "055 123 4567", "05512", "05abc12345"]

count = 0

for phone in phones:
    if is_valid_phone(phone):
        print(phone)
        count += 1

print("Valid numbers:", count)