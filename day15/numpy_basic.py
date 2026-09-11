import numpy as np

# ساخت یک آرایه از یک لیست معمولی
list_normal = [1, 2, 3, 4, 5]
array_numpy = np.array(list_normal)

print("لیست معمولی:", list_normal)
print("آرایه NumPy:", array_numpy)
print("نوع داده:", type(array_numpy))

# چرا NumPy بهتره؟ عملیات ریاضی روی کل آرایه یکجا
print("\nآرایه ضرب‌شده در 2:", array_numpy * 2)
print("آرایه به‌علاوه 10:", array_numpy + 10)

# ساخت آرایه دو بعدی (ماتریس)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\nماتریس:\n", matrix)
print("شکل ماتریس (سطر, ستون):", matrix.shape)

# چندتا تابع کاربردی NumPy
zeros = np.zeros(5)
ones = np.ones(5)
range_array = np.arange(0, 10, 2)

print("\nآرایه صفرها:", zeros)
print("آرایه یک‌ها:", ones)
print("آرایه با فاصله 2:", range_array)