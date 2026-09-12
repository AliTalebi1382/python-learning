import pandas as pd
import numpy as np

# یک دیتاست با مشکلات واقعی (مقادیر خالی، تکراری)
data = {
    "name": ["علی", "سارا", "رضا", "علی", "مریم", None],
    "age": [20, 22, None, 20, 23, 19],
    "score": [18, 15, 20, 18, np.nan, 17]
}
df = pd.DataFrame(data)

print("داده اولیه:\n", df)

# بررسی مقادیر خالی
print("\nتعداد مقادیر خالی در هر ستون:\n", df.isnull().sum())

# حذف ردیف‌هایی که مقدار خالی دارن
df_dropped = df.dropna()
print("\nبعد از حذف ردیف‌های خالی:\n", df_dropped)

# پر کردن مقادیر خالی به‌جای حذف (مثلاً با میانگین)
df_filled = df.copy()
df_filled["age"] = df_filled["age"].fillna(df_filled["age"].mean())
df_filled["score"] = df_filled["score"].fillna(df_filled["score"].mean())
print("\nبعد از پر کردن مقادیر خالی با میانگین:\n", df_filled)

# پیدا کردن و حذف ردیف‌های تکراری
print("\nردیف‌های تکراری:\n", df.duplicated())
df_no_duplicates = df.drop_duplicates()
print("\nبعد از حذف تکراری‌ها:\n", df_no_duplicates)