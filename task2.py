days = ["Sun", "Mon", "Tue", "Wed", "Thu"]
sales = [1200, 950, 1800, 1430, 2100]

for i in range(len(sales)):
    print(days[i], ":", sales[i], "SAR")

    total = 0

for s in sales:
    total = total + s

average = total / len(sales)

print("Total:", total, "SAR")
print("Average:", average, "SAR")

best_sales = sales[0]
best_day = days[0]

for i in range(len(sales)):
    if sales[i] > best_sales:
        best_sales = sales[i]
        best_day = days[i]

print("Best day:", best_day, "(", best_sales, "SAR)")

count = 0

for s in sales:
    if s > 1500:
        count += 1

print("Days above target:", count)

# استخدمنا range(len(sales)) عشان نقدر نطبع كل يوم مع المبيعات الخاصة فيه