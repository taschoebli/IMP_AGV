import time
from api import app  # Import the Flask app from api.py
from taskManager import TaskManager  # Import taskManager to process tasks

if __name__ == '__main__':
    # Start TaskManager as a singleton
    task_manager = TaskManager()

    # Run the Flask app
    app.run(host='10.255.215.145', port=5000)

    time.sleep(5)

    task_manager = TaskManager()
    print(f"Aktuelle Tasks: {task_manager.tasks}")
