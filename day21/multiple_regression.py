import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# داده فرضی: مساحت خانه، تعداد اتاق → قیمت خانه (میلیون تومان)
data = {
    "area": [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
    "rooms": [1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
    "price": [800, 950, 1100, 1300, 1450, 1700, 1850, 2000, 2300, 2500]
}
df = pd.DataFrame(data)
print("داده‌ها:\n", df)

X = df[["area", "rooms"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nقیمت‌های واقعی:", y_test.values)
print("قیمت‌های پیش‌بینی‌شده:", predictions)

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print(f"\nMSE: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

print(f"\nضرایب مدل: {model.coef_}")
print(f"عرض از مبدا: {model.intercept_:.2f}")

# پیش‌بینی قیمت یک خانه جدید: 95 متر، 2 اتاق
new_house = pd.DataFrame({"area": [95], "rooms": [2]})
predicted_price = model.predict(new_house)
print(f"\nقیمت پیش‌بینی‌شده برای خانه 95 متری با 2 اتاق: {predicted_price[0]:.2f} میلیون تومان")