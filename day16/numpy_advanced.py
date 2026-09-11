import numpy as np

# ساخت ماتریس‌های نمونه
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print("ماتریس A:\n", matrix_a)
print("ماتریس B:\n", matrix_b)

# جمع و ضرب ساده (عضو به عضو)
print("\nجمع ماتریس‌ها:\n", matrix_a + matrix_b)
print("ضرب عضو به عضو:\n", matrix_a * matrix_b)

# ضرب ماتریسی واقعی (dot product)
print("\nضرب ماتریسی (dot product):\n", np.dot(matrix_a, matrix_b))

# ترانهاده (Transpose) - جابه‌جایی سطر و ستون
print("\nترانهاده A:\n", matrix_a.T)

# تغییر شکل آرایه (reshape)
numbers = np.arange(1, 13)
print("\nآرایه اولیه:", numbers)

reshaped = numbers.reshape(3, 4)
print("تبدیل به ماتریس 3x4:\n", reshaped)

reshaped2 = numbers.reshape(4, 3)
print("تبدیل به ماتریس 4x3:\n", reshaped2)