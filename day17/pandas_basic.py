import pandas as pd

# Series یعنی یک ستون داده (شبیه لیست ولی با ایندکس)
scores = pd.Series([18, 15, 20, 12], index=["علی", "سارا", "رضا", "مریم"])
print("Series نمرات:\n", scores)
print("\nنمره علی:", scores["علی"])

# DataFrame یعنی یک جدول کامل (شبیه اکسل)
data = {
    "name": ["علی", "سارا", "رضا", "مریم"],
    "age": [20, 22, 21, 23],
    "score": [18, 15, 20, 12]
}

df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# دیدن اطلاعات کلی جدول
print("\nاطلاعات کلی:")
print(df.info())

print("\nخلاصه آماری:")
print(df.describe())

# انتخاب یک ستون خاص
print("\nستون name:\n", df["name"])

# انتخاب چند ستون
print("\nستون‌های name و score:\n", df[["name", "score"]])