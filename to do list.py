# Simple To-Do List Command-Line Application in Python

def show_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "status": "Pending"})
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']} [Status: {task['status']}]")

def update_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_number = int(input("\nEnter the task number to update: "))
        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the new task description: ")
            new_status = input("Enter the new status (Pending/Completed): ")
            tasks[task_number - 1]["task"] = new_task
            tasks[task_number - 1]["status"] = new_status
            print("Task updated successfully.")
        else:
            print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_number = int(input("\nEnter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['task']}' deleted.")
        else:
            print("Invalid task number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
