import pandas as pd

data = {
    "name": ["علی", "سارا", "رضا", "مریم", "حسن", "زهرا"],
    "city": ["تهران", "اصفهان", "تهران", "شیراز", "تهران", "اصفهان"],
    "score": [18, 15, 20, 12, 17, 19]
}
df = pd.DataFrame(data)

print("داده کامل:\n", df)

# فیلتر کردن: فقط دانش‌آموزهای تهرانی
tehran_students = df[df["city"] == "تهران"]
print("\nدانش‌آموزهای تهران:\n", tehran_students)

# فیلتر با چند شرط: تهرانی‌ها با نمره بالای 17
tehran_top = df[(df["city"] == "تهران") & (df["score"] > 17)]
print("\nتهرانی‌های با نمره بالای 17:\n", tehran_top)

# گروه‌بندی بر اساس شهر و گرفتن میانگین نمره هر شهر
city_avg = df.groupby("city")["score"].mean()
print("\nمیانگین نمره هر شهر:\n", city_avg)

# گروه‌بندی با چند تابع آماری همزمان
city_stats = df.groupby("city")["score"].agg(["mean", "max", "min", "count"])
print("\nآمار کامل هر شهر:\n", city_stats)