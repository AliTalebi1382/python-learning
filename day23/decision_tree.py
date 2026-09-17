import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# همون داده مشتری‌ها از روز قبل
data = {
    "age": [22, 25, 47, 52, 46, 56, 55, 60, 62, 61, 18, 28, 27, 29, 49],
    "income": [15, 18, 45, 50, 42, 55, 53, 60, 62, 58, 10, 20, 19, 22, 48],
    "purchased": [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1]
}
df = pd.DataFrame(data)

X = df[["age", "income"]]
y = df["purchased"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ساخت و آموزش مدل درخت تصمیم
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(f"دقت مدل Decision Tree: {accuracy:.2f}")
print("\nگزارش کامل:")
print(classification_report(y_test, predictions))

# اهمیت هر ویژگی در تصمیم‌گیری مدل
print("اهمیت هر ویژگی (Feature Importance):")
for feature, importance in zip(X.columns, model.feature_importances_):
    print(f"{feature}: {importance:.2f}")