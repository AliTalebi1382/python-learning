# روش معمولی برای ساخت لیست مربعات اعداد
squares_normal = []
for i in range(1, 6):
    squares_normal.append(i ** 2)
print("روش معمولی:", squares_normal)

# همون کار با List Comprehension (یک‌خطی و سریع‌تر)
squares_comprehension = [i ** 2 for i in range(1, 6)]
print("با Comprehension:", squares_comprehension)

# List Comprehension با شرط: فقط اعداد زوج
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print("اعداد زوج:", even_numbers)

# Dict Comprehension: ساخت دیکشنری از عدد و مربعش
squares_dict = {i: i ** 2 for i in range(1, 6)}
print("دیکشنری مربعات:", squares_dict)