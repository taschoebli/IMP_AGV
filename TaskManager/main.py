from api import app  # Import the Flask app from api.py
from taskManager import TaskManager  # Import taskManager to process tasks

if __name__ == '__main__':
    # Start TaskManager as a singleton
    task_manager = TaskManager()

    # Run the Flask app
    app.run(host='172.20.10.2', port=5000)
