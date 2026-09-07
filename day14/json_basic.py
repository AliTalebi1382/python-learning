import json

# یک دیکشنری پایتون
student = {
    "name": "علی",
    "age": 20,
    "skills": ["Python", "Machine Learning"]
}

# تبدیل دیکشنری به رشته JSON (تبدیل به فایل قابل ذخیره)
json_string = json.dumps(student, ensure_ascii=False, indent=4)
print(json_string)

# ذخیره در فایل
with open("student.json", "w", encoding="utf-8") as f:
    json.dump(student, f, ensure_ascii=False, indent=4)

# خواندن دوباره از فایل
with open("student.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print("داده خوانده‌شده از فایل:", loaded_data)