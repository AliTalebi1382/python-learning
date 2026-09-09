# تابع معمولی
def square(x):
    return x ** 2

# همون کار با Lambda (تابع یک‌خطی بدون اسم)
square_lambda = lambda x: x ** 2

print("تابع معمولی:", square(5))
print("با Lambda:", square_lambda(5))

# استفاده از Lambda با map: مربع کردن همه اعضای لیست
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("لیست مربع‌شده:", squared)

# استفاده از Lambda با filter: فقط اعداد بزرگتر از 2
filtered = list(filter(lambda x: x > 2, numbers))
print("فیلترشده:", filtered)

# استفاده از Lambda با sorted: مرتب‌سازی بر اساس یک قانون خاص
students = [
    {"name": "علی", "score": 18},
    {"name": "سارا", "score": 15},
    {"name": "رضا", "score": 20}
]

sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
for s in sorted_students:
    print(f"{s['name']}: {s['score']}")