import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

# Indexing (دسترسی به یک عضو خاص)
print("عضو اول:", numbers[0])
print("عضو آخر:", numbers[-1])

# Slicing (برش - گرفتن یک بازه)
print("از عضو 1 تا 3:", numbers[1:4])

# عملیات آماری روی آرایه
print("\nمجموع:", numbers.sum())
print("میانگین:", numbers.mean())
print("بیشترین:", numbers.max())
print("کمترین:", numbers.min())
print("انحراف معیار:", numbers.std())

# مقایسه با شرط (خیلی کاربردی در ML)
print("\nاعداد بزرگتر از 25:", numbers[numbers > 25])