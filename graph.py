import networkx as nx

class Graph:
    def __init__(self):
        self.G = nx.Graph()
        self.initialize_graph()

    def initialize_graph(self):
        # Add edges with weights and the Blocked attribute
        edges = [
            ('A', 'B', {'weight': 4, 'Blocked': False}),
            ('A', 'C', {'weight': 2, 'Blocked': False}),
            ('A', 'D', {'weight': 3, 'Blocked': False}),
            ('B', 'E', {'weight': 3, 'Blocked': False}),
            ('B', 'F', {'weight': 2, 'Blocked': False}),
            ('C', 'D', {'weight': 1, 'Blocked': False}),
            ('D', 'E', {'weight': 1, 'Blocked': False}),
            ('E', 'F', {'weight': 1, 'Blocked': False})
        ]

        self.G.add_edges_from(edges)

    def update_blocked_status(self, edge_nodes, status):
        try:
            node1, node2 = edge_nodes
            if self.G.has_edge(node1, node2):
                self.G[node1][node2]['Blocked'] = status
                print(f"Updated Blocked status of edge {node1}-{node2} to {status}.")
            else:
                print(f"Edge {node1}-{node2} does not exist.")
        except ValueError:
            print("Invalid edge_nodes input. Please provide exactly two nodes, e.g., ('A', 'B').")

    def find_shortest_path(self, start, end):
        try:
            # Compute shortest path using weights
            path = nx.shortest_path(self.G, source=start, target=end, weight='weight')
            cost = nx.shortest_path_length(self.G, source=start, target=end, weight='weight')

            # Check if any edge in the path is blocked
            blocked_status = any(self.G[path[i]][path[i + 1]]['Blocked'] for i in range(len(path) - 1))

            return {
                'path': path,
                'cost': cost,
                'blocked': blocked_status
            }
        except nx.NetworkXNoPath:
            return {
                'path': None,
                'cost': float('inf'),
                'blocked': None
            }
        except nx.NodeNotFound as e:
            print(f"Error: {e}")
            return {
                'path': None,
                'cost': None,
                'blocked': None
            }

    def find_unblocked_path(self, start, end):
        try:
            # Create a subgraph with only unblocked edges
            unblocked_edges = [(u, v) for u, v, attr in self.G.edges(data=True) if not attr['Blocked']]
            unblocked_graph = self.G.edge_subgraph(unblocked_edges).copy()

            # Compute shortest path in the unblocked graph
            path = nx.shortest_path(unblocked_graph, source=start, target=end)
            cost = nx.shortest_path_length(unblocked_graph, source=start, target=end, weight='weight')

            return {
                'path': path,
                'cost': cost,
                'blocked': False
            }
        except nx.NetworkXNoPath:
            return {
                'path': None,
                'cost': float('inf'),
                'blocked': True
            }
        except nx.NodeNotFound as e:
            print(f"Error: {e}")
            return {
                'path': None,
                'cost': None,
                'blocked': None
            }

    def print_graph_info(self):
        print("Graph Edges with Attributes:")
        for u, v, attr in self.G.edges(data=True):
            print(f"{u}-{v}: {attr}")

    def get_subpaths_with_costs(self, path):
        """Returns all subpaths (pairs of consecutive waypoints) with their respective costs."""
        if not path or len(path) < 2:
            print("Invalid path. A valid path must contain at least two nodes.")
            return []

        subpaths = []
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            if self.G.has_edge(u, v):
                cost = self.G[u][v].get('weight', float('inf'))
                subpaths.append(((u, v), cost))
            else:
                print(f"No edge found between {u} and {v}.")
                subpaths.append(((u, v), float('inf')))
        return subpaths

    def next_turn(self, current_edge, approaching_waypoint, goal):
        """
        Determine the next turn based on the current edge, approaching waypoint, and goal.

        Parameters:
        - current_edge: tuple (node1, node2) representing the edge the robot is currently on.
        - approaching_waypoint: the waypoint the robot is moving towards.
        - goal: the final destination waypoint.
        """
        # Define the rules for turns
        rules = {
            (('A', 'B'), 'B', 'F'): "go straight",
            (('A', 'B'), 'B', 'E'): "turn right",
            (('A', 'B'), 'A', 'C'): "go straight",
            (('A', 'B'), 'A', 'D'): "turn left",
            (('A', 'D'), 'D', 'C'): "turn right",
            (('A', 'D'), 'D', 'E'): "turn left",
            (('A', 'D'), 'A', 'C'): "turn left",
            (('A', 'D'), 'A', 'B'): "turn right",
            (('A', 'C'), 'A', 'D'): "turn right",
            (('A', 'C'), 'A', 'B'): "go straight",
            (('A', 'C'), 'C', 'D'): "turn left",
            (('C', 'D'), 'C', 'A'): "turn right",
            (('C', 'D'), 'D', 'A'): "turn left",
            (('C', 'D'), 'D', 'E'): "go straight",
            (('D', 'E'), 'D', 'C'): "go straight",
            (('D', 'E'), 'D', 'A'): "turn right",
            (('D', 'E'), 'E', 'F'): "go straight",
            (('D', 'E'), 'E', 'B'): "turn left",
            (('B', 'E'), 'E', 'D'): "turn right",
            (('B', 'E'), 'E', 'F'): "turn left",
            (('B', 'E'), 'B', 'A'): "turn left",
            (('B', 'E'), 'B', 'F'): "turn right",
            (('B', 'F'), 'B', 'E'): "turn left",
            (('B', 'F'), 'B', 'A'): "go straight",
            (('B', 'F'), 'F', 'E'): "turn right",
            (('E', 'F'), 'F', 'B'): "turn left",
            (('E', 'F'), 'E', 'B'): "turn right",
            (('E', 'F'), 'E', 'D'): "go straight",
        }

        # Normalize the edge direction to match the rules
        normalized_edge = tuple(sorted(current_edge))
        turn = rules.get((normalized_edge, approaching_waypoint, goal), "unknown")
        print(f"Next turn on edge {current_edge} approaching {approaching_waypoint} towards {goal}: {turn}")
        return turn
