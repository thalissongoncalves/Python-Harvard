import json
import os

def main():
    while True:
        option = input("""\nWelcome to the To-Do List!
                           
1 - Add task
2 - List tasks
3 - Mark as completed
4 - Remove task
5 - Exit
                       
Select an option: """)
    
        if option == "1":
            task = input("Enter the task: ").strip()
            add_task(task)
        elif option == "2":
            list_tasks()
        elif option == "3":
            task = input("Enter the task to mark as completed: ").strip()
            mark_as_completed(task)
        elif option == "4":
            task = input("Enter the task to remove: ").strip()
            remove_task(task)
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please select a valid number.")


def add_task(task):
    file_path = "tasks.json"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                tasks = json.load(f)
                if not isinstance(tasks, list):
                    tasks = []
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []

    tasks.append({"task": task, "status": "pending"})

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)

    print("Task added successfully!")


def list_tasks():
    file_path = "tasks.json"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                tasks = json.load(f)
                if not tasks:
                    print("No tasks available. Add one!")
                    return
                print("\nYour To-Do List:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task['task']} | Status: {task['status']}")
            except json.JSONDecodeError:
                print("Error loading tasks.")
    else:
        print("No tasks available. Add one!")


def mark_as_completed(task):
    file_path = "tasks.json"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                tasks = json.load(f)
                found = False
                for tk in tasks:
                    if tk['task'].lower() == task.lower():
                        tk['status'] = 'completed'
                        found = True
                        break
                if not found:
                    print("Task not found.")
            except json.JSONDecodeError:
                print("Error loading tasks.")
                return

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4)
        print("Task marked as successfully completed!")
    else:
        print("No tasks available. Add one!")


def remove_task(task):
    file_path = "tasks.json"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                tasks = json.load(f)
                for index, tk in enumerate(tasks):
                    if tk['task'].lower() == task.lower():
                        del tasks[index]
            except json.JSONDecodeError:
                print("Error loading tasks.")

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4)
        print("Task removed successfully!")
    else:
        print("No tasks available. Add one!")


if __name__ == "__main__":
    main()