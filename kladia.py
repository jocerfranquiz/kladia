add_node = lambda graph, node_key, node_value: graph.update({node_key: node_value})

add_edge = lambda graph, node_key, link_key, link_value: graph[node_key].update({link_key: link_value})

delete_edge = lambda graph, node_key, link_key: graph[node_key].pop(link_key, None)

delete_node = lambda graph, node_key: graph.pop(node_key, None)

if "__main__" == __name__:
    # Initialize an empty graph
    graph = {0: None}

    print(f"Graph: {graph}")

    # Add a node to the graph
    add_node(graph, 1, None)

    # The graph now looks like this: {0: None, 1: None}
    print(graph)

    # Add an edge from node 1 to node 0
    add_edge(graph, 1, 0, None)

    # The graph now looks like this: {0: None, 1: {0: None}}
    print(graph)

    # Delete the edge from node 1 to node 0
    delete_edge(graph, 1, 0)

    # The graph now looks like this: {0: None, 1: None}
    print(graph)

    # Delete node 1 from the graph
    delete_node(graph, 1)

    # The graph is now empty: {0: None}
    print(graph)
