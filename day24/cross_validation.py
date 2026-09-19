import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

data = {
    "age": [22, 25, 47, 52, 46, 56, 55, 60, 62, 61, 18, 28, 27, 29, 49],
    "income": [15, 18, 45, 50, 42, 55, 53, 60, 62, 58, 10, 20, 19, 22, 48],
    "purchased": [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1]
}
df = pd.DataFrame(data)

X = df[["age", "income"]]
y = df["purchased"]

# به‌جای یک تقسیم ثابت train/test، داده رو ۵ بار به روش‌های مختلف تقسیم می‌کنیم
tree_model = DecisionTreeClassifier(random_state=42)
tree_scores = cross_val_score(tree_model, X, y, cv=5)

print("دقت مدل Decision Tree در هر تکرار:", tree_scores)
print(f"میانگین دقت: {tree_scores.mean():.2f}")
print(f"انحراف معیار: {tree_scores.std():.2f}")

log_model = LogisticRegression()
log_scores = cross_val_score(log_model, X, y, cv=5)

print("\nدقت مدل Logistic Regression در هر تکرار:", log_scores)
print(f"میانگین دقت: {log_scores.mean():.2f}")
print(f"انحراف معیار: {log_scores.std():.2f}")