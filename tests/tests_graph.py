"""
Tests for the graph module.
author: @jocerfranquiz
date: 2022-12-02
version: 0.0.1
"""

import pytest
from src.kladia.graph import graph, from_nodes_and_links


# Path: tests\tests_graph.py
# Compare this snippet from kladia\graph_examples.py:

# Test Graph class
def test_graph():
    # Create a simple 2 node graph
    g = graph()  # create an empty graph
    g.add(0, {'color': 'red'})  # add a node with a property
    g.add(1, {'color': 'blue'})  # add another node with a property
    g.add((0, 1), {'weight': 1.0})  # add a looping link with a property
    assert g.to_dict() == {'graph': {0: {1: {'weight': 1.0}, 'color': 'red'}, 1: {'color': 'blue'}}}
    assert g.nodes() == {0: None, 1: {'color': 'blue'}}
    assert g.links() == {(0, 1): {'weight': 1.0}}
    assert g.to_matrix() == [[0, 1], [0, 0]]

    # A graph must be a dictionary with a single key 'graph'
    with pytest.raises(Exception):
        graph({'grap': {0: None}})

    # Delete a node
    g = graph({'graph': {0: {3: {'label': 'node3'}}, 1: None, 3: None, 4: None}})
    g.dlt(0)
    assert g.to_dict() == {'graph': {1: None, 3: None, 4: None}}

    # Delete a link
    g = graph({'graph': {0: {3: {'label': 'node3'}}, 1: None}})
    g.dlt((0, 3))
    assert g.to_dict() == {'graph': {0: None, 1: None}}

    # Union of two graphs
    a = graph({'graph': {0: {1: {'link': 'link1'}}, 1: {2: {'link': 'link2', 'color': 'red'}}}})
    b = graph({'graph': {1: {2: {'color': 'blue'}}, 2: None}})
    assert a.union(b).to_dict() == {'graph': {0: {1: {'link': 'link1'}}, 1: {2: {'link': 'link2', 'color': 'blue'}}, 2: None}}

    # Intersection of two graphs
    a = graph({'graph': {0: {1: {'label': '_1'}}, 1: {2: None}, 2: None, 4: {0: None}}})
    b = graph({'graph': {0: {1: None}, 1: {'color': 'red'}, 3: None, 4: {0: {'label': '_2'}}}})
    assert a.intersect(b).to_dict() == {'graph': {0: {1: {'label': '_1'}}, 1: {'color': 'red'}, 4: {0: {'label': '_2'}}}}

    # Test from_matrix
    g = graph()
    g.from_matrix([[0, 1], [0, 0]])
    assert g.to_dict() == {'graph': {0: {1: {'weight': 1}}, 1: None}}

    # Test from_nodes_and_links
    g = from_nodes_and_links({0: None, 1: {'color': 'blue'}}, {(0, 1): {'weight': 1.0}})
    assert g.to_dict() == {'graph': {0: {1: {'weight': 1.0}}, 1: {'color': 'blue'}}}


# Run the tests script
if __name__ == '__main__':
    pytest.main()
