import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("هیچ کاری ثبت نشده.")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['title']}")

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("کار اضافه شد.")

def complete_task(tasks, index):
    try:
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print("کار انجام‌شده علامت خورد.")
    except IndexError:
        print("شماره نامعتبر است.")

# برنامه اصلی
tasks = load_tasks()

while True:
    print("\n1. نمایش کارها")
    print("2. اضافه کردن کار")
    print("3. علامت زدن به‌عنوان انجام‌شده")
    print("4. خروج")

    choice = input("انتخاب شما: ")

    if choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        title = input("عنوان کار: ")
        add_task(tasks, title)
    elif choice == "3":
        show_tasks(tasks)
        idx = int(input("شماره کار انجام‌شده: "))
        complete_task(tasks, idx)
    elif choice == "4":
        break
    else:
        print("انتخاب نامعتبر است.")