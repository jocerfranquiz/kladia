
from kladia.graph import graph

if __name__ == '__main__':
    g = graph()  # create an empty graph
    g.add(0, {'color': 'red'})  # add a node with a property
    g.add(1, {'color': 'blue'})  # add another node with a property
    g.add((0, 1), {'weight': 1.0})  # add a looping link with a property

    print(g.to_dict())

    # Test add_node
    g1 = graph()
    g1.add(0, {'name': 'Node 0'})
    g1.add(2)
    print(f'g1: {g1.to_dict()}')
    try:
        g2 = graph({'graph': {0: {3: {'label': 'node3'}}, 1: None, 3: None, 4: None}})
        print(f'g2: {g2.to_dict()}')
    except Exception as e:
        print(f'g2: {e}')
    try:
        g3 = graph({'grap': {0: None}})
    except Exception as e:
        print(f'g3 error: {e}')

    # Test add for links
    g4 = graph()
    g4.add((1, 2), {'label': 'link1'})
    g4.add((2, 3))
    g4.add((4, 4))
    print(f'g4: {g4.to_dict()}')

    # Test delete_node
    g5 = graph({'graph': {0: {3: {'label': 'node3'}}, 1: None, 3: None, 4: None}})
    g5.dlt(0)
    print(f'g5: {g5.to_dict()}')

    # Test delete link
    g6 = graph({'graph': {0: {3: {'label': 'node3'}}, 1: None, 3: None, 4: None}})
    g6.dlt((0, 3))
    print(f'g6: {g6.to_dict()}')

    # Test nodes
    g7 = graph({'graph': {0: {3: {'label': 'node3'}}, 1: None, 2: None, 3: None}})
    print(f'g7 nodes: {g7.nodes()}')

    # Test links
    triangular_graph = graph({'graph': {
        0: {1: {'label': 'link1'}},
        1: {2: {'label': 'link2'}},
        2: {0: {'label': 'link3'}},
    }})

    # Test to_matrix
    print(f'Triangular graph: {triangular_graph.to_dict()}')
    print(f'triangular_graph nodes: {triangular_graph.nodes()}')
    print(f'triangular_graph links: {triangular_graph.links()}')
    print(f'triangular_graph array: {triangular_graph.to_matrix()}')

    # test empty graph to_matrix
    g8 = graph()
    print(f'g8 array: {g8.to_matrix()}')