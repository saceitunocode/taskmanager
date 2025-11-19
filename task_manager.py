import json

class Task:

    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] #{self.id}: {self.description}"

class TaskManager:

    FILENAME = "tasks.json"

    def __init__(self):
        self._tasks = []
        self._next_id = 1
        self.load_tasks()

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"\nTarea añadida: {task}")
        self.save_tasks()

    def list_task(self):
        if not self._tasks:
            print("\nNo hay tareas para mostrar")
        else:
            print("\nLista de tareas:")
            for task in self._tasks:
                print(task)

    def complete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                print(f"\nTarea completada: {task}")
                self.save_tasks()
                return
        print(f"\nNo se encuentra la tarea con ID {id}")

    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"\nTarea eliminada: {task}")
                self.save_tasks()
                return
        print(f"\nNo se encuentra la tarea con ID {id}")

    def save_tasks(self):
        with open(self.FILENAME, 'w') as file:
            data = [{"id": task.id, "description": task.description, "complete": task.completed} for task in self._tasks]
            json.dump(data, file, indent=4)

    def load_tasks(self):
        try:
            with open(self.FILENAME, 'r') as file:
                data = json.load(file)
                self._tasks = [Task(item["id"], item["description"], item["complete"]) for item in data]
                if self._tasks:
                    self._next_id = max(task.id for task in self._tasks) + 1
                else:
                    self._next_id = 1

        except FileNotFoundError:
            self._tasks = []