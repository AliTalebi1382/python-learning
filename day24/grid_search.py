import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

data = {
    "age": [22, 25, 47, 52, 46, 56, 55, 60, 62, 61, 18, 28, 27, 29, 49],
    "income": [15, 18, 45, 50, 42, 55, 53, 60, 62, 58, 10, 20, 19, 22, 48],
    "purchased": [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1]
}
df = pd.DataFrame(data)

X = df[["age", "income"]]
y = df["purchased"]

# می‌خواهیم بهترین مقدار n_neighbors رو برای KNN پیدا کنیم
param_grid = {"n_neighbors": [1, 3, 5, 7, 9]}

knn_model = KNeighborsClassifier()
grid_search = GridSearchCV(knn_model, param_grid, cv=5)
grid_search.fit(X, y)

print("بهترین پارامتر پیدا‌شده:", grid_search.best_params_)
print(f"بهترین دقت به‌دست‌آمده: {grid_search.best_score_:.2f}")

# نمایش نتیجه برای هر مقدار امتحان‌شده
results = pd.DataFrame(grid_search.cv_results_)
print("\nنتیجه هر مقدار n_neighbors:")
print(results[["param_n_neighbors", "mean_test_score"]])