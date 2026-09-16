import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# داده فرضی: ساعت مطالعه → قبول (1) یا رد (0) شدن در امتحان
study_hours = np.array([1, 2, 3, 3.5, 4, 5, 6, 6.5, 7, 8, 9, 10]).reshape(-1, 1)
passed = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1])

X_train, X_test, y_train, y_test = train_test_split(
    study_hours, passed, test_size=0.25, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("مقادیر واقعی:", y_test)
print("پیش‌بینی مدل:", predictions)

accuracy = accuracy_score(y_test, predictions)
print(f"\nدقت مدل (Accuracy): {accuracy:.2f}")

print("\nماتریس درهم‌ریختگی (Confusion Matrix):")
print(confusion_matrix(y_test, predictions))

# پیش‌بینی برای یک مقدار جدید
new_hours = np.array([[4.5]])
prediction = model.predict(new_hours)
probability = model.predict_proba(new_hours)

result = "قبول" if prediction[0] == 1 else "رد"
print(f"\nپیش‌بینی برای 4.5 ساعت مطالعه: {result}")
print(f"احتمال قبولی: {probability[0][1]:.2f}")