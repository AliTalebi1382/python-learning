def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Save Tasks")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if not tasks:
            print("\nNo tasks found.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "3":
        if not tasks:
            print("\nNo tasks to delete.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                number = int(input("Enter task number to delete: "))

                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    print(f'"{removed}" deleted successfully.')
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        save_tasks(tasks)
        print("Tasks saved successfully.")

    elif choice == "5":
        save_tasks(tasks)
        print("Tasks saved.")
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
