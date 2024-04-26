import json
import os
from datetime import datetime

# Function to load tasks from a JSON file
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            return json.load(file)
    else:
        return []

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (Low/Medium/High): ")
    tasks.append({
        'description': description,
        'due_date': due_date,
        'priority': priority,
        'status': 'Pending'
    })
    save_tasks(tasks)
    print("Task added successfully.")

# Function to delete a task
def delete_task(tasks):
    print_tasks(tasks)
    task_index = int(input("Enter the index of the task to delete: ")) - 1
    del tasks[task_index]
    save_tasks(tasks)
    print("Task deleted successfully.")

# Function to update a task
def update_task(tasks):
    print_tasks(tasks)
    task_index = int(input("Enter the index of the task to update: ")) - 1
    tasks[task_index]['description'] = input("Enter new description: ")
    tasks[task_index]['due_date'] = input("Enter new due date (YYYY-MM-DD): ")
    tasks[task_index]['priority'] = input("Enter new priority (Low/Medium/High): ")
    save_tasks(tasks)
    print("Task updated successfully.")

# Function to view all tasks
def view_tasks(tasks):
    print("Tasks:")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task['description']} - Due: {task['due_date']} - Priority: {task['priority']} - Status: {task['status']}")

# Function to mark a task as complete
def mark_complete(tasks):
    print_tasks(tasks)
    task_index = int(input("Enter the index of the task to mark as complete: ")) - 1
    tasks[task_index]['status'] = 'Complete'
    save_tasks(tasks)
    print("Task marked as complete.")

# Function to print all tasks
def print_tasks(tasks):
    if tasks:
        view_tasks(tasks)
    else:
        print("No tasks found.")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Update Task")
        print("4. View Tasks")
        print("5. Mark Task as Complete")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            delete_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            view_tasks(tasks)
        elif choice == '5':
            mark_complete(tasks)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
