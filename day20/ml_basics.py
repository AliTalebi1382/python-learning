import numpy as np
from sklearn.model_selection import train_test_split

# فرض کنید این داده‌های ساعت مطالعه و نمره امتحان است
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
exam_scores = np.array([5, 8, 12, 15, 18, 20, 23, 25, 28, 30])

# تقسیم داده به آموزش (train) و آزمایش (test)
X_train, X_test, y_train, y_test = train_test_split(
    study_hours, exam_scores, test_size=0.2, random_state=42
)

print("داده‌های آموزش (X_train):\n", X_train)
print("\nداده‌های آزمایش (X_test):\n", X_test)
print("\nنمرات آموزش (y_train):\n", y_train)
print("\nنمرات آزمایش (y_test):\n", y_test)

print(f"\nتعداد کل داده: {len(study_hours)}")
print(f"تعداد داده آموزش: {len(X_train)}")
print(f"تعداد داده آزمایش: {len(X_test)}")