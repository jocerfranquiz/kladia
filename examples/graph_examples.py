
from src.kladia.graph import graph


if __name__ == '__main__':

    # Create a simple 2 node graph
    g = graph()  # create an empty graph
    g.add(0, {'color': 'red'})  # add a node with a property
    g.add(1, {'color': 'blue'})  # add another node with a property
    g.add((0, 1), {'weight': 1.0})  # add a looping link with a property

    print(g.to_dict())

    # Export a graph to a dictionary
    g1 = graph()
    g1.add(0, {'name': 'Node 0'})
    g1.add(2)
    print(f'g1: {g1.to_dict()}')

    # Create a graph from a dictionary
    try:
        g2 = graph({'graph': {0: {3: {'label': 'node3'}}, 1: None, 3: None, 4: None}})
        print(f'g2: {g2.to_dict()}')
    except Exception as e:
        print(f'g2: {e}')

    # Just remember that the graph must be a dictionary with a single key 'graph'
    try:
        g3 = graph({'grap': {0: None}})
    except Exception as e:
        print(f'g3 error: {e}')

    # Create a graph by adding links
    g4 = graph()
    g4.add((1, 2), {'label': 'link1'})
    g4.add((2, 3))
    g4.add((4, 4))
    print(f'g4: {g4.to_dict()}')

    # Delete a node
    g5 = graph({'graph': {0: {3: {'label': 'node3'}}, 1: None, 3: None, 4: None}})
    g5.dlt(0)
    print(f'g5: {g5.to_dict()}')

    # Delete a link
    g6 = graph({'graph': {0: {3: {'label': 'node3'}}, 1: None, 3: None, 4: None}})
    g6.dlt((0, 3))
    print(f'g6: {g6.to_dict()}')

    # Create a triangular graph
    triangular_graph = graph({'graph': {
        0: {1: {'label': 'link1'}, 'color': 'red'},
        1: {2: None, 'color': 'green'},
        2: {0: {'label': 'link3'}},
    }})

    # Get the nodes, links and adjacency matrix
    print(triangular_graph.to_dict())
    print(f'triangular_graph nodes: {triangular_graph.nodes()}')
    print(f'triangular_graph links: {triangular_graph.links()}')
    print(f'triangular_graph array: {triangular_graph.to_matrix()}')

    # Create a graph from an adjacency matrix
    matrix = [[0, 1, 0, 0, 0],  # link from node 0 to node 1
              [0, 0, 1, 0, 0],  # link from node 1 to node 2
              [1, 0, 0, 2.3, 0],  # links from node 2 to node 0 and node 3
              [0, 0, 0, 0, -1],  # link from node 3 to node 4
              [0, 0, 0, 0, 0]]  # node 4 has no links
    g7 = graph()
    g7.from_matrix(matrix)
    print(f'g7: {g7.to_dict()}')

    # Union of two graphs
    g8 = graph({'graph': {0: {1: {'link': 'link1'}}, 1: {2: {'link': 'link2', 'color': 'red'}}}})
    print(f'g8: {g8.to_dict()}')
    g9 = graph({'graph': {1: {2: {'color': 'blue'}}, 2: None}})
    print(f'g9: {g9.to_dict()}')
    g10 = g8.union(g9)
    print(f'g10: {g10.to_dict()}')

    # Intersection of two graphs
    g11 = graph({'graph': {0: {1: {'label': '_1'}}, 1: {2: None}, 2: None, 4: {0: None}}})
    print(f'g11: {g11.to_dict()}')
    g12 = graph({'graph': {0: {1: None}, 1: {'color': 'red'}, 3: None, 4: {0: {'label': '_2'}}}})
    print(f'g12: {g12.to_dict()}')
    g13 = g11.intersect(g12)
    print(f'g13: {g13.to_dict()}')
