import numpy as np

# نمرات ۱۰ دانش‌آموز در ۳ درس مختلف (ریاضی، فیزیک، شیمی)
grades = np.array([
    [18, 15, 17],
    [12, 14, 16],
    [20, 19, 18],
    [10, 11, 9],
    [15, 16, 14],
    [8, 12, 10],
    [19, 20, 17],
    [13, 14, 15],
    [17, 16, 18],
    [11, 13, 12]
])

print("جدول نمرات (هر سطر یک دانش‌آموز):\n", grades)

# میانگین هر درس (میانگین روی ستون‌ها → axis=0)
subject_avg = grades.mean(axis=0)
print("\nمیانگین هر درس (ریاضی، فیزیک، شیمی):", subject_avg)

# میانگین هر دانش‌آموز (میانگین روی سطرها → axis=1)
student_avg = grades.mean(axis=1)
print("\nمیانگین هر دانش‌آموز:", student_avg)

# بالاترین میانگین بین دانش‌آموزان
best_student_index = np.argmax(student_avg)
print(f"\nبهترین دانش‌آموز: دانش‌آموز شماره {best_student_index + 1} با میانگین {student_avg[best_student_index]:.2f}")

# چند نفر بالای ۱۵ میانگین دارن؟
count_above_15 = np.sum(student_avg > 15)
print(f"تعداد دانش‌آموزان با میانگین بالای 15: {count_above_15}")