import pandas as pd

# ساخت یک DataFrame نمونه
data = {
    "name": ["علی", "سارا", "رضا", "مریم", "حسن"],
    "age": [20, 22, 21, 23, 19],
    "city": ["تهران", "اصفهان", "شیراز", "تهران", "مشهد"],
    "score": [18, 15, 20, 12, 17]
}
df = pd.DataFrame(data)

# ذخیره در فایل CSV
df.to_csv("students.csv", index=False, encoding="utf-8-sig")
print("فایل students.csv ساخته شد.")

# خواندن دوباره از فایل CSV
df_loaded = pd.read_csv("students.csv", encoding="utf-8-sig")
print("\nداده خوانده‌شده از CSV:\n", df_loaded)

# نمایش چند ردیف اول
print("\n۳ ردیف اول:\n", df_loaded.head(3))

# مرتب‌سازی بر اساس نمره (نزولی)
sorted_df = df_loaded.sort_values(by="score", ascending=False)
print("\nمرتب‌شده بر اساس نمره:\n", sorted_df)