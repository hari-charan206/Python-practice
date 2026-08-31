tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['name']}")

def add_task():
    name = input("Enter task: ").strip()

    if not name:
        print("Task cannot be empty.")
        return

    tasks.append({
        "name": name,
        "completed": False
    })

    print("Task added successfully.")

def complete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        if tasks[number - 1]["completed"]:
            print("Task is already completed.")
        else:
            tasks[number - 1]["completed"] = True
            print("Task completed.")

    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        deleted_task = tasks.pop(number - 1)
        print(f"Deleted: {deleted_task['name']}")

    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
