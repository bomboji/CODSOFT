import os

class ToDoList:
    def __init__(self, file_path='todolist.txt'):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        return [task.strip() for task in open(self.file_path).readlines()] if os.path.exists(self.file_path) else []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            file.write('\n'.join(self.tasks))

    def show(self):
        print("Tasks:" if self.tasks else "No tasks found.")
        [print(f"{index}. {task}") for index, task in enumerate(self.tasks, start=1)]

    def add(self, new_task):
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{new_task}' added successfully.")

    def delete(self, task_index):
        try:
            task_index = int(task_index)
            deleted_task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f"Task '{deleted_task}' deleted successfully.")
        except (ValueError, IndexError):
            print("Invalid task index.")

    def update(self, task_index, new_task):
        try:
            task_index = int(task_index)
            self.tasks[task_index - 1] = new_task
            self.save_tasks()
            print("Task updated successfully.")
        except (ValueError, IndexError):
            print("Invalid task index.")

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\n==== To-Do List Menu ====")
        print("1. Show Tasks\n2. Add Task\n3. Delete Task\n4. Update Task\n5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            todo_list.show()
        elif choice == "2":
            todo_list.add(input("Enter the new task: "))
        elif choice == "3":
            todo_list.delete(input("Enter the task index to delete: "))
        elif choice == "4":
            todo_list.update(input("Enter the task index to update: "), input("Enter the new task: "))
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
