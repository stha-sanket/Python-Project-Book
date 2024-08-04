# this is how we make a to-do list in python well quite a small project but still a quite a good start
todo_file = "todo_list.txt" # this is the file we will be working on

# Function to load tasks from the to-do list file
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


def main():
    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "3":
            view_tasks()
            try:
                task_num = int(input("Enter the task number to remove: "))
                remove_task(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

