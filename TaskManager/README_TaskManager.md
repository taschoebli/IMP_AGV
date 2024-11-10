## Task Management for IMP_AGV

---

The main components include:

1. A [REST API](api.py) where Task can be added to the AGV system.
2. A [Task Manager](taskManager.py) which is able to 
   - check the validity of a submitted task
   - divide a task in atomic subtasks
   - track the progress of (sub)tasks across the AGV system
3. Assign (sub)tasks to available and suitable AGV agents (**to be discussed**, *maybe in another bounded context*)

## How to use
1. Make sure that Flask is installed on your machine
   > pip install flask
2. Run [`main.py`](main.py)
3. Submit a task using Postman or similar
   > POST http://[client-ip-address]:5000/api/v1/tasks

   With a body as JSON
   
   > {
   > "departure":    "A",
   > "destination":  "D",
   > "amount":       2 
   > }
   

