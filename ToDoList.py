# this is how we make a to-do list in python well quite a small project but still a quite a good start
todo_file = "todo_list.txt" # this is the file we will be working on
def load_tasks():
    try:
        with open(todo_file, "r") as f:
            tasks = f.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

# To save a task
def save_tasks(tasks):
    with open(todo_file, "w") as f:
        for task in tasks:
            f.write(task + "\n")

#To add a task
def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

#To Remove a task
def remove_task(task_num):
    tasks = load_tasks()
    if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task number.")

# To view the task in the list
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

