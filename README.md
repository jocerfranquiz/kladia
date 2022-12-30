# Kladia  🌿

A simple and minimal graph library based on Python dictionaries. The main goal of this library is to provide 
a simple and easy to use graph data structure and data manipulation methods. THe structure is simple enough to 
be adapted to any other graph library.

## But how?

Using Python dictionaries we can construct *the simplest non-empty linked graph* with one node and one link in three steps:

    1. Create a graph ``{'graph': None}``
    2. Add a node ``{'graph': {0: None}}``
    2. Add a link to itself ``{'graph': {0: {0: None}}}``

Then, we can replace the ``None`` values with desired properties or data. For example, we can add a node with a
property ``{'graph': {0: {'color': 'red'}}}`` or a link with a property ``{'graph': {0: {0: {'weight': 1}}}}``.

Kladia helps you to create and manipulate these graphs in a simple way.

## Why Kladia?

**Kladia**  🌿 is the latinisation of the greek word **κλαδιά**, that means *branch* or *twig*. It is also the name of a genus of plants that includes
the *olive tree*.

## TODOs

- TODO: implement operations on graphs, e.g. union, intersection, difference, etc.
- TODO: implement traversal algorithms, e.g. BFS, DFS, etc.
- TODO: implement search algorithms, e.g. BFS, DFS, etc.
- TODO: implement the shortest path algorithm (Dijkstra's algorithm)
- TODO: implement minimum spanning tree (MST) algorithm (Kruskal's algorithm)
- TODO: implement maximum flow problem (Ford-Fulkerson algorithm)
- TODO: implement minimum cut set (min cut) problem (Karger's algorithm)
- TODO: implement bipartite matching  (https://en.wikipedia.org/wiki/Bipartite_graph)
- TODO: implement strongly connected components (SCC) (https://en.wikipedia.org/wiki/Strongly_connected_component)
- TODO: implement topological sort (DAG) (https://en.wikipedia.org/wiki/Topological_sorting)
- TODO: implement transitive closure (Warshall's algorithm)
- TODO: implement unit tests for all methods and functions using pytest (https://docs.pytest.org/en/latest/)
- TODO: implement documentation using Sphinx (https://www.sphinx-doc.org/en/master/)
- TODO: implement examples using Jupyter Notebook (https://jupyter.org/)
- TODO: implement visualization using GraphViz (https://graphviz.readthedocs.io/en/stable/)

