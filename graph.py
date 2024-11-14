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
