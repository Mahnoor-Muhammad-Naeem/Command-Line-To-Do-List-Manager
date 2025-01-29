import os
import json

# File to store tasks
TASKS_FILE = "tasks.json"

# Function to load tasks from a file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save tasks to a file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Function to display tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. {task['title']} [ {status} ]")

# Function to add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print(f"Task '{title}' added successfully!")

# Function to mark task as completed
def complete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to mark as completed: "))
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to delete: "))
    if 0 < task_num <= len(tasks):
        deleted_task = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Task '{deleted_task['title']}' deleted successfully!")
    else:
        print("Invalid task number.")

# Main menu
def show_menu():
    print("\nTo-Do List")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
