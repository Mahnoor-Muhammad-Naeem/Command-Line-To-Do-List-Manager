# Command-Line To-Do List Manager
A simple Python-based to-do list application that allows you to manage tasks directly from the command line. This application supports adding tasks, viewing tasks, marking tasks as completed, and deleting tasks. All tasks are stored in a JSON file for persistent storage.

## Features
View tasks with their completion status.

Add new tasks to your to-do list.

Mark tasks as completed.

Delete tasks from the list.

Persistent task storage using a JSON file.

### Prerequisites
To run this project, ensure the following:

Python 3.x is installed on your system.
### How to Run
Clone the repository or download the script:

```bash
git clone https://github.com/Mahnoor-Muhammad-Naeem/command-line-to-Do-Manager.git
cd command-line-todo-manager
```
Install Python (if not already installed). You can download it from [ python.org](https://www.python.org/)

Run the script using the following command:

```bash
python todo_manager.py
```
Follow the prompts in the command-line interface to manage your tasks.

### File Structure

```bash
├── tasks.json           # JSON file to store tasks
├── todo_manager.py      # Main Python script
```
### How It Works
View Tasks: Lists all tasks with their status (completed or not).
Add Task: Prompts for a task title and adds it to the list.
Mark Task as Completed: Displays tasks and allows marking one as completed.
Delete Task: Displays tasks and allows deleting a specific one.
Exit: Exits the program.
### Example
#### Running the Program:

```bash
To-Do List
1. View tasks
2. Add a task
3. Mark task as completed
4. Delete a task
5. Exit

Enter your choice: 2
Enter task title: Buy groceries
Task 'Buy groceries' added successfully!
```
### After Adding Tasks:

```bash
To-Do List
1. View tasks
2. Add a task
3. Mark task as completed
4. Delete a task
5. Exit

Enter your choice: 1
1. Buy groceries [ ✗ ]
```
### Notes
All tasks are saved in `tasks.json` in the same directory as the script. Do not delete this file unless you want to reset your tasks.

This project is beginner-friendly and demonstrates basic file handling, JSON operations, and command-line interfaces in Python.
### Contributions
Feel free to fork the project, make improvements, and submit a pull request. Contributions are welcome!
