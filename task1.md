# 1. مالفرق بين fot & while

for: نستخدمها لما نكون عارفين عدد مرات التكرار أو عندنا قائمة نبي نمر على عناصرها

مثال:

for i in range(1, 6):
   print(i)


while: نستخدمها لما نبي نكرر الكود طالما توفر عندنا شرط صحيح

مثال:

number = 1

while number <= 5:
    print(number)
    number += 1


# 2. قراءة الكود وتوقع الناتج

def add(a, b): 
    print(a + b) 
    
def multiply(a, b): 
    return a * b 

x = add(2, 3) 
y = multiply(2, 3) 
print(x, y) 

for i in range(1, 10, 3): 
    print(i) 
    
count = 3 
while count > 0: 
    print("Attempt", count) 
    count -= 1

**RESULTS:**

5
None 6
1
4
7
Attempt 3
Attempt 2
Attempt 1

# بعد تشغيل الكود لاحظت أن الناتج الفعلي مطابقًا لتوقعي


**لماذا ظهرت None?**
**ومالفرق بين print , return ?**

ظهرت كلمة None 
لان الدالة add 
استخدمت print فقط
ومارجعت اي قيمة باستخدام return

print تستخدم لعرض النتيجة على الشاشة
return ترجع النتيجة من الدالة عشان نقدر نستخدمها مرة ثانية

# 3. جدول التتبع 

total = 0
i = 1

while i <= 5:
    total = total + i * 2
    i = i + 1

print(total)


**الناتج :**
30


![Trace Table](image/trace_table.jpeg)