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
