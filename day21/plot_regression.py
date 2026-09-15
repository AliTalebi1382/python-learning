import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from persian_fix import fix_persian

study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
exam_scores = np.array([5, 8, 12, 15, 18, 20, 23, 25, 28, 30])

model = LinearRegression()
model.fit(study_hours, exam_scores)

predicted_line = model.predict(study_hours)

plt.figure(figsize=(8, 6))
plt.scatter(study_hours, exam_scores, color='blue', label=fix_persian('داده واقعی'))
plt.plot(study_hours, predicted_line, color='red', label=fix_persian('خط پیش‌بینی مدل'))
plt.title('Study Hours vs Exam Score')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.legend()
plt.grid(True)
plt.savefig("regression_line.png")
plt.show()