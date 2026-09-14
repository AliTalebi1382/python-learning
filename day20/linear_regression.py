import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# داده: ساعت مطالعه → نمره امتحان
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
exam_scores = np.array([5, 8, 12, 15, 18, 20, 23, 25, 28, 30])

# تقسیم داده
X_train, X_test, y_train, y_test = train_test_split(
    study_hours, exam_scores, test_size=0.2, random_state=42
)

# ساخت و آموزش مدل
model = LinearRegression()
model.fit(X_train, y_train)

# پیش‌بینی روی داده تست
predictions = model.predict(X_test)

print("مقادیر واقعی:", y_test)
print("مقادیر پیش‌بینی‌شده:", predictions)

# ارزیابی مدل
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"\nMean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# ضریب و عرض از مبدا مدل (y = a*x + b)
print(f"\nشیب خط (a): {model.coef_[0]:.2f}")
print(f"عرض از مبدا (b): {model.intercept_:.2f}")

# پیش‌بینی یک مقدار جدید (مثلاً کسی که 6.5 ساعت مطالعه کرده)
new_hours = np.array([[6.5]])
predicted_score = model.predict(new_hours)
print(f"\nپیش‌بینی نمره برای 6.5 ساعت مطالعه: {predicted_score[0]:.2f}")