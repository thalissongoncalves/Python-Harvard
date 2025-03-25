import json
import os

def main():
    option = int(input("""Welcome to the To-Do List!
                           
1 - Add task
2 - List tasks
3 - Mark as completed
4 - Remove task
                       
Select a option: """))
    
    if option == 1:
        task = input("Enter the task: ")
        add_task(task)
    elif option == 2:
        list_tasks()
    elif option == 3:
        task = input("Enter the task: ")
        mark_as_completed(task)


def add_task(task):
    file_path = "tarefas.json"

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

    tasks.append({"tarefa": task, "status": "pendente"})

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)


def list_tasks():
    file_path = "tarefas.json"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                tasks = json.load(f)
                for task in tasks:
                    print(f"Tarefa: {task['tarefa']} | Status: {task['status']}")
            except json.JSONDecodeError:
                print("Não existe tarefas em sua lista, fique a vontade para adicionar alguma!")
    else:
        print("Não existe tarefas em sua lista, fique a vontade para adicionar alguma!")


def mark_as_completed(task):
    file_path = "tarefas.json"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                tasks = json.load(f)
                for index, tk in enumerate(tasks):
                    if tk['tarefa'] == task:
                        tasks[index]['status'] = 'completed'
                        print(tasks)
            except json.JSONDecodeError:
                print("Não existe tarefas em sua lista, fique a vontade para adicionar alguma!")

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4)
    else:
        print("Não existe tarefas em sua lista, fique a vontade para adicionar alguma!")


def remove_task():
    ...


if __name__ == "__main__":
    main()