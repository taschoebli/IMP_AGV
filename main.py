import graph
import task
import agent

warehouse_graph = graph.Graph()
warehouse_graph.print_graph_info()


task = task.Task()
task.add_task("A", "F", 3)
task.add_task("A", "C", 3)

agent1 = agent.Agent(1, True, True,('A', 'C'), 'A')