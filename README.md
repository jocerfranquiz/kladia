# Kladia 🌿

### A simple and minimal graph library based on Python dictionaries

**Kladia** is a library that provides a simple and easy way to work with graph data structures in Python. 
**Kladia graphs** are dictionaries simple enough to be used and adapted to any other libraries and frameworks.

## Ok, but how?

Using **ONLY Python dictionaries** we can easily construct a simple **two node directed graph** in 4 steps:

1. Create a graph ``{'graph': None}``
2. Add a node ``{'graph': {0: None}}``
3. Add another node ``{'graph': {0: None, 1: None}}``
4. Add a link from node 0 to node 1 ``{'graph': {0: {1: None}, 1: None}}``

Then, we can replace the ``None`` values with desired properties or data. For example, we can add a node with a
property ``{'graph': {0: {'color': 'red'}}}`` or a link with a property ``{'graph': {0: {1: {'weight': 1.0}}}}``.

*Kladia* helps you to create and manipulate these graphs in a simple way.

```
from kladia.graph import graph

g = graph()  # create an empty graph
g.add(0, {'color': 'red'})  # add a node with a property
g.add(1, {'color': 'blue'})  # add another node with a property
g.add((0, 1), {'weight': 1.0})  # add a looping link with a property

print(g.to_dict())
```

Which will print (without the comments):

```
{
    'graph': {
        0: {                    # node 0
            'color': 'red',     # node 0 property
            1: {'weight': 1.0}  # link to node 1
        }, 
        1: {                    # node 1
            'color': 'blue'     # node 1 property
        }
    }
}
```

For convenience, the Graph class only manage dictionaries for graphs, nodes and links. 
By design **Properties has no restrictions whatsoever**.

Feel free to review the notes in [NOTES.rst](https://github.com/jocerfranquiz/kladia/blob/main/docs/NOTES.rst) for more information.

More examples can be found in the [examples](https://github.com/jocerfranquiz/kladia/tree/main/examples) folder.

## Why everything is a dictionary?

Using dictionaries and integer labels, we can traverse the graph faster than using an object-oriented approach. 
You can work only with the structure of the graph, without worrying about the properties for faster operations. 
For example, this is a **directed binary tree** of 3 levels:

```
{
    'graph': {
        0: {1: None, 2: None},      # Node 0 is linked to nodes 1 and 2
        1: {3: None, 4: None},      # Node 1 is linked to nodes 3 and 4
        2: {5: None, 6: None},      # Node 2 is linked to nodes 5 and 6
        3: None,                    # Node 3 is a leaf
        4: None,                    # Node 4 is a leaf
        5: None,                    # Node 5 is a leaf
        6: None                     # Node 6 is a leaf
    }
}
```

## Other features:
*Kladia* graphs are:
- Up to order 2 nested Python dictionaries (dicts, of dicts, of dicts)
- Represented as a dictionary of nodes (vertices), where each node is a dictionary of links (edges), commonly known as [adjacency list](https://en.wikipedia.org/wiki/Adjacency_list)
- Directed by default. To create an undirected graph, just add the same link in both directions

Graphs, nodes and links can have custom **properties** dictionary to store any kind of data, such as weights, labels, etc.

## Why the name Kladia?

**Kladia**  🌿 is the latinization of the greek word **κλαδιά**, that means *branch* or *twig*. It is also the name of a genus of plants that includes
the *olive tree*.

## TODOs

- [x] implement ``to_matrix`` method to convert a graph to a adjacency matrix
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
