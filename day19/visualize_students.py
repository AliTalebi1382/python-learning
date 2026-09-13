import pandas as pd
import matplotlib.pyplot as plt
from persian_fix import fix_persian

data = {
    "name": ["علی", "سارا", "رضا", "مریم", "حسن", "زهرا"],
    "city": ["تهران", "اصفهان", "تهران", "شیراز", "تهران", "اصفهان"],
    "score": [18, 15, 20, 12, 17, 19]
}
df = pd.DataFrame(data)

# نمودار میله‌ای نمرات هر دانش‌آموز
names_fixed = [fix_persian(n) for n in df["name"]]

plt.figure(figsize=(8, 5))
plt.bar(names_fixed, df["score"], color='skyblue')
plt.title(fix_persian("نمرات دانش‌آموزان"))
plt.xlabel(fix_persian("نام"))
plt.ylabel(fix_persian("نمره"))
plt.savefig("student_scores.png")
plt.show()

# میانگین نمره هر شهر
city_avg = df.groupby("city")["score"].mean()
cities_fixed = [fix_persian(c) for c in city_avg.index]

plt.figure(figsize=(6, 4))
plt.bar(cities_fixed, city_avg.values, color='coral')
plt.title(fix_persian("میانگین نمره هر شهر"))
plt.xlabel(fix_persian("شهر"))
plt.ylabel(fix_persian("میانگین نمره"))
plt.savefig("city_avg_scores.png")
plt.show()