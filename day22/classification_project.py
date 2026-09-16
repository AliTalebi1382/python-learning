import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# داده فرضی: سن، درآمد ماهانه → خرید محصول (1) یا نه (0)
data = {
    "age": [22, 25, 47, 52, 46, 56, 55, 60, 62, 61, 18, 28, 27, 29, 49],
    "income": [15, 18, 45, 50, 42, 55, 53, 60, 62, 58, 10, 20, 19, 22, 48],
    "purchased": [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1]
}
df = pd.DataFrame(data)
print("داده‌ها:\n", df)

X = df[["age", "income"]]
y = df["purchased"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(f"\nدقت مدل: {accuracy:.2f}")

print("\nگزارش کامل دسته‌بندی:")
print(classification_report(y_test, predictions))

# پیش‌بینی برای یک مشتری جدید: سن 35، درآمد 30 میلیون
new_customer = pd.DataFrame({"age": [35], "income": [30]})
prediction = model.predict(new_customer)
probability = model.predict_proba(new_customer)

result = "خرید می‌کند" if prediction[0] == 1 else "خرید نمی‌کند"
print(f"\nپیش‌بینی برای مشتری 35 ساله با درآمد 30: {result}")
print(f"احتمال خرید: {probability[0][1]:.2f}")