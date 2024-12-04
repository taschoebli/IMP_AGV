from flask import Flask, request, jsonify, make_response
from taskManager import Task, TaskManager


print("Starting the Flask application...")
app = Flask(__name__)
api_prefix = '/api/v1'


# Add a task to the AGV system
@app.route(api_prefix + '/tasks', methods=['POST'])
def add_task():
    submitted_task_body = request.get_json()

    # Create an actual task and submit it to the task manager
    task = Task(submitted_task_body.get('departure'), submitted_task_body.get('destination'), submitted_task_body.get('amount'))
    valid, message = task.validate_task()
    if not valid:
        response = make_response(jsonify({'error': message}), 400)
        return response

    # add the assigned taskId before returning it
    submitted_task_body['task_id'] = task.taskId
    submitted_task_body['distance'] = abs(ord(submitted_task_body['departure']) - ord(submitted_task_body['destination']))
    submitted_task_body['cost'] = submitted_task_body['distance'] * submitted_task_body['amount']

    response = make_response(jsonify(accepted_task=submitted_task_body), 200)
    return response


@app.route(api_prefix + '/tasklist', methods=['GET'])
def get_tasklist():
    TaskManager
    return make_response(jsonify({'taskId': 'a400ee34-3750-4ad2-8d9d-549ac5f8742f-TESTDATA'}), 200)

