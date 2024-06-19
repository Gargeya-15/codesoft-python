class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task number.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
        else:
            print("Invalid task number.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")


def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Options:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Complete task")
        print("4. List tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            index = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == "3":
            index = int(input("Enter task number to complete: ")) - 1
            todo_list.complete_task(index)
        elif choice == "4":
            todo_list.list_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
