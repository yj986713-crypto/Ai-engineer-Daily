import json
import os

DATA_FILE = "todo_list.json"

def load_tasks():
    """Loads tasks from a JSON file. Returns an empty list if file doesn't exist."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    """Saves the current task list to a JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """Adds a new task to the list."""
    print("\n--- Add New Task ---")
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty!")
        return
    
    new_task = {"title": title, "completed": False}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"✅ Task '{title}' added successfully!")

def view_tasks(tasks):
    """Displays all tasks with status checkboxes."""
    print("\n--- Current Tasks ---")
    if not tasks:
        print("Your to-do list is empty!")
        return

    for index, task in enumerate(tasks, start=1):
        status = "[❌]" if task["completed"] else "[  ]"
        print(f"{index}. {status} {task['title']}")

def complete_task(tasks):
    """Marks a selected task as completed."""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        choice = int(input("\nEnter task number to mark complete: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            save_tasks(tasks)
            print(f"🎉 Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Deletes a selected task from the list."""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        choice = int(input("\nEnter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"🗑️ Deleted task: '{removed['title']}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n=========================")
        print("    TASK MANAGER CLI     ")
        print("=========================")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nGoodbye! Have a productive day! 🚀")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
