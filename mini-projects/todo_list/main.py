tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

            number = int(input("Task number: "))

            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task deleted.")
            else:
                print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
