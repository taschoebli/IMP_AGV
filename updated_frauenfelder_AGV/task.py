class Task:
    def __init__(self):
        self.tasklist = []

    def add_task(self, start, end, packages):
        task = {
            'start': start,
            'end': end,
            'packages': packages
        }
        self.tasklist.append(task)
        print(f"Task added: {task}")

    def get_tasks(self):
        return self.tasklist

    def get_task(self):
        if self.tasklist:
            first_task = self.tasklist[0]
            print(f"First Task: {first_task}")
            return first_task
        else:
            print("No tasks in the tasklist.")
            return None
