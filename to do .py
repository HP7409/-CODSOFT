class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'done': False})
        print(f"✅ Task added: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("📜 No tasks in the list.")
        else:
            print("\n📌 To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                status = "✔ Done" if task['done'] else "❌ Not Done"
                print(f"{index}. {task['task']} - {status}")

    def mark_done(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]['done'] = True
            print(f"🎉 Task {task_number} marked as done!")
        else:
            print("❌ Invalid task number.")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"🗑 Task removed: {removed_task['task']}")
        else:
            print("❌ Invalid task number.")

    def run(self, mock_inputs=None):
        input_index = 0
        while True:
            print("\nOptions: add, view, done, remove, exit")
            if mock_inputs:
                if input_index >= len(mock_inputs):
                    break
                choice = mock_inputs[input_index].strip().lower()
                input_index += 1
            else:
                try:
                    choice = input("Enter your choice: ").strip().lower()
                except (OSError, EOFError):
                    print("⚠️ Input error detected. Exiting program.")
                    break
            
            if choice == "add":
                if mock_inputs:
                    if input_index >= len(mock_inputs):
                        break
                    task = mock_inputs[input_index].strip()
                    input_index += 1
                else:
                    task = input("Enter the task: ").strip()
                self.add_task(task)
            elif choice == "view":
                self.view_tasks()
            elif choice == "done":
                try:
                    if mock_inputs:
                        if input_index >= len(mock_inputs):
                            break
                        task_number = int(mock_inputs[input_index])
                        input_index += 1
                    else:
                        task_number = int(input("Enter task number to mark as done: "))
                    self.mark_done(task_number)
                except ValueError:
                    print("❌ Please enter a valid number.")
            elif choice == "remove":
                try:
                    if mock_inputs:
                        if input_index >= len(mock_inputs):
                            break
                        task_number = int(mock_inputs[input_index])
                        input_index += 1
                    else:
                        task_number = int(input("Enter task number to remove: "))
                    self.remove_task(task_number)
                except ValueError:
                    print("❌ Please enter a valid number.")
            elif choice == "exit":
                print("👋 Goodbye! Have a productive day!")
                break
            else:
                print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    todo = ToDoList()
    todo.run()