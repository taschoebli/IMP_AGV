# taskManager.py
import string
import uuid
# from typing import Dict, Any, List
from typing import List

import logging

logging.basicConfig(level=logging.INFO)


class Task:
    def __init__(self, departure, destination, amount):
        self.departure = departure
        self.destination = destination
        self.amount = amount
        self.taskId = str(uuid.uuid4())
        # self.subtaskIds = self.break_down_task(self)

    def validate_task(self) -> [bool, str]:
        # Check existence of departure attribute
        if not hasattr(self, 'departure'):
            return [False, "Attribute 'departure' is missing."]
        # Check if value is a string and uppercase letter
        if not isinstance(self.departure, str) or self.departure not in string.ascii_uppercase:
            return [False, "Attribute 'departure' needs to be a single, capital letter."]

        # Check existence of destination attribute
        if not hasattr(self, 'destination'):
            return [False, "Attribute 'destination' is missing."]
        # Check if value is a string and uppercase letter
        if not isinstance(self.destination, str) or self.destination not in string.ascii_uppercase:
            return [False, "Attribute 'destination' needs to be a single, capital letter."]

        # Check existence of amount attribute
        if not hasattr(self, 'amount'):
            return [False, "Attribute 'amount' is missing."]
        # Check if amount value is an integer and >0
        if not isinstance(self.amount, int) or self.amount <= 0:
            return [False, "Attribute 'amount' needs to be an integer value and larger than 0."]

        # All checks approved
        return [True, ""]

    """
    def break_down_task(self) -> List[Dict[str, Any]]:
        """
    """
                Breaks down the task into subtasks based on the edges between departure and destination.
                Each subtask represents moving one unit of the total amount and has an amount of 1.

                Args:
                    The task containing 'departure', 'destination', and 'amount'

                Returns:
                    A list of dictionaries, each representing a subtask. Or a list of subtask ids
    
    
        subtasks = []

        # Assuming you have a method to find the path between nodes
        path = self.find_path(self.departure, self.destination)
        if not path:
            # No path found between departure and destination
            return subtasks

        # Break down the total amount into subtasks of amount 1
        for i in range(self.amount):
            for idx in range(len(path) - 1):
                edge_departure = path[idx]
                edge_destination = path[idx + 1]
                subtask = {
                    'subtask_id': f"{uuid.uuid4()}",
                    'departure': edge_departure,
                    'destination': edge_destination,
                    'amount': 1
                }
                subtasks.append(subtask)

        return subtasks
    """


class Subtask(Task):
    """
        Subtasks are the atomic steps of a Task
    """


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # Check if an instance already exists
        if cls not in cls._instances:
            # If not, create one and store it
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TaskManager(metaclass=SingletonMeta):
    def __init__(self):
        # empty taskList
        self.taskList = {}

        # add database connection later for consistency

    """
    def process_task(self, task_data: Dict[str, Any]) -> Dict[str, Any]:

        subtasks = self.break_down_task(task_data)

        self.tasks[task_id] = {
            'task_data': task_data,
            'subtasks': subtasks,
            'status': 'pending'
        }

        logging.info(f"Task {task_id} processed with {len(subtasks)} subtasks")

        return {
            'task_id': task_id,
            'subtasks': subtasks,
            'message': 'Task processed successfully'
        }
    """
