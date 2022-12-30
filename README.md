# Kladia  🌿 A simple and minimal graph library based on Python dictionaries

The main goal of this library is to provide a simple and easy to use graph data structures. 
Kladia graphs are simple enough to be adapted to any other libraries and frameworks.

## Ok, but how?

Using **ONLY Python dictionaries** we can easily construct **the simplest non-empty linked graph** with one node and one link in three steps:

    1. Create a graph {'graph': None}
    2. Add a node {'graph': {0: None}}
    2. Add a link of the node to itself {'graph': {0: {0: None}}}

Then, we can replace the ``None`` values with desired properties or data. For example, we can add a node with a
property ``{'graph': {0: {'color': 'red'}}}`` or a link with a property ``{'graph': {0: {0: {'weight': 1}}}}``.

*Kladia* helps you to create and manipulate these graphs in a simple way.

    from kladia import graph
    
    g = graph()  # create an empty graph
    g.add(0, {'color': 'red'})  # add a node with a property
    g.add((0, 0), {'weight': 1})  ## add a looping link with a property
    
    print({g.to_dict()})  # {'graph': {0: {'color': 'red', 0: {'weight': 1}}}}
    
For convenience, Graph class only manage dictionaries for graphs, nodes and links. Properties has not restrictions whatsoever. 
Feel free to review the notes in [NOTES.rst](https://github.com/jocerfranquiz/kladia/blob/main/NOTES.rst) for more information.

## Why everything is a dictionary?

Using dictionaries and integer labels, we can traverse the graph faster than using an object-oriented approach. You can work only with the structure of the graph, without worrying about the properties for faster operations. For example, this is A **directed binary tree** of 3 levels:
```
print(binary_tree_graph.to_dict())

{
'graph': {
    0: {1: None, 2: None}, 
    1: {3: None, 4: None}, 
    2: {5: None, 6: None}, 
    3: None, 
    4: None, 
    5: None, 
    6: None
    }
}
```
## Other features:
    - Kladia graphs are up to order 2 nested Python dictionaries (dicts of dicts of dicts)
    - Graphs are represented as a dictionary of nodes, where each node is a dictionary of links (edges), commomly knoewd as [adjacency list](https://en.wikipedia.org/wiki/Adjacency_list)
    - Graphs are directed by default. To create an undirected graph, just add the same link in both directions
    - Graphs, nodes and links can have a custom **properties** dictionary to store any kind of data, such as weights, labels, etc.

## Why the name Kladia?

**Kladia**  🌿 is the latinization of the greek word **κλαδιά**, that means *branch* or *twig*. It is also the name of a genus of plants that includes
the *olive tree*.

## TODOs

- [ ] implement ``from_dict`` method
- [ ] implement ``to_matrix`` method to convert a graph to a adjacency matrix
- [ ] implement operations on graphs, e.g. union, intersection, difference, etc.
- [ ] implement traversal algorithms, e.g. BFS, DFS, etc.
- [ ] implement search algorithms, e.g. BFS, DFS, etc.
- [ ] implement the shortest path algorithm (Dijkstra's algorithm)
- [ ] implement minimum spanning tree (MST) algorithm (Kruskal's algorithm)
- [ ] implement maximum flow problem (Ford-Fulkerson algorithm)
- [ ] implement minimum cut set (min cut) problem (Karger's algorithm)
- [ ] implement bipartite matching  (https://en.wikipedia.org/wiki/Bipartite_graph)
- [ ] implement strongly connected components (SCC) (https://en.wikipedia.org/wiki/Strongly_connected_component)
- [ ] implement topological sort (DAG) (https://en.wikipedia.org/wiki/Topological_sorting)
- [ ] implement transitive closure (Warshall's algorithm)
- [ ] implement unit tests for all methods and functions using pytest (https://docs.pytest.org/en/latest/)
- [ ] implement documentation using Sphinx (https://www.sphinx-doc.org/en/master/)
- [ ] implement examples using Jupyter Notebook (https://jupyter.org/)
- [ ] implement visualization using GraphViz (https://graphviz.readthedocs.io/en/stable/)
- [ ] implement a web interface using Flask (https://flask.palletsprojects.com/en/1.1.x/)
- 