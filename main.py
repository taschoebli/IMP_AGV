import graph

warehouse_graph = graph.Graph()
warehouse_graph.print_graph_info()
warehouse_graph.update_blocked_status(('E', 'D'), True)
warehouse_graph.print_graph_info()
unblocked_result = warehouse_graph.find_unblocked_path('A', 'F')
print(f"Unblocked Path: {unblocked_result['path']}, Cost: {unblocked_result['cost']}, Blocked: {unblocked_result['blocked']}")