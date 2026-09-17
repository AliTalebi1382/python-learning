import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = {
    "age": [22, 25, 47, 52, 46, 56, 55, 60, 62, 61, 18, 28, 27, 29, 49],
    "income": [15, 18, 45, 50, 42, 55, 53, 60, 62, 58, 10, 20, 19, 22, 48],
    "purchased": [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1]
}
df = pd.DataFrame(data)

X = df[["age", "income"]]
y = df["purchased"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# مدل KNN (نزدیک‌ترین همسایه‌ها)
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)
knn_predictions = knn_model.predict(X_test)
knn_accuracy = accuracy_score(y_test, knn_predictions)

# مدل Decision Tree
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)
tree_predictions = tree_model.predict(X_test)
tree_accuracy = accuracy_score(y_test, tree_predictions)

# مدل Logistic Regression
log_model = LogisticRegression()
log_model.fit(X_train, y_train)
log_predictions = log_model.predict(X_test)
log_accuracy = accuracy_score(y_test, log_predictions)

# مقایسه نهایی
print("مقایسه دقت مدل‌های مختلف:")
print(f"KNN: {knn_accuracy:.2f}")
print(f"Decision Tree: {tree_accuracy:.2f}")
print(f"Logistic Regression: {log_accuracy:.2f}")

best_model = max(
    [("KNN", knn_accuracy), ("Decision Tree", tree_accuracy), ("Logistic Regression", log_accuracy)],
    key=lambda x: x[1]
)
print(f"\nبهترین مدل: {best_model[0]} با دقت {best_model[1]:.2f}")