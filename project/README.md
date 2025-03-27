# To-Do List Project

#### Video Demo: https://www.youtube.com/watch?v=BmxCcGwGwqY;

#### Description:

This project consists of managing your tasks in a simple and efficient way, being able to add tasks, list tasks, mark as complete and remove tasks. I chose to use JSON to keep the information even after leaving the application.

## Features:

- **Add Task**: The user can add a task and it will be added with the status of "pending".
- **List Tasks**: The user can list all stored tasks.
- **Mark as Completed**: The user can mark a pending task as complete.
- **Remove Task**: The user can remove a task that he has added to the list.
- **Persistent Storage**: The information is saved in the tasks.json file.

## Project Files:

### 1. `project.py`

This is the main file, where all the functions responsible for the operation of the application are concentrated. It contains the following functions:

- `main()`: Responsible for displaying the menu and storing what the user types.
- `add_task(task)`: Adds a new task to the `tasks.json` file.
- `list_tasks()`: Lists all tasks stored in the file.
- `mark_as_completed(task)`: Updates the status of a task to "completed".
- `remove_task(task)`: Removes a task from the list.

### 2. `test_project.py`

This file contains functions that test the operation of the project.py functions:

- `test_add_task()`: Tests adding a new task.
- `test_list_tasks_empty()`: Tests the program's behavior when listing tasks with none registered.
- `test_mark_as_completed()`: Tests the functionality of marking a task as completed.
- `test_remove_task()`: Tests the removal of a task from the list.

## Design Decisions:

1. **Use of JSON for storage**: JSON format was chosen for being lightweight, readable, and easy to handle in Python.
2. **Error handling**: The code includes checks to ensure that the JSON file is correctly read and that operations do not fail if the file is missing or corrupted.
3. **Command-line interface (CLI)**: A simple menu-based interface was chosen to make the program intuitive to use.
4. **Unit testing**: Tests were implemented to ensure the reliability and correct functionality of the system's main functions.

## How to Run the Project:

1. Ensure that Python is installed on your system.
2. Clone this repository or download the files.
3. In the terminal, navigate to the project folder and run:
   ```
   pip install
   ```
   ```
   python project.py
   ```
4. To run the tests, use the command:
   ```
   pytest test_project.py
   ```

This project is a simple and effective solution for task management, with potential for future expansion, such as a graphical interface or database integration.