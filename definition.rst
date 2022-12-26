A simple structure for graphs in Python
---------------------------------------

In **Python** we define a **graph** as a data structure of *special* nested dictionaries of the form ``{node_key: node_value}`` called **node**, where:

    - ``node_key`` is an ``integer``.
    - ``node_value`` is a dictionary that contains other nodes or node's attributes. It can be ``None`` type.

For now, let's assume that ``node_value = None``, and focus on the nodes themselves and their **linked** structure. It can be ``None``.
For example:
    - This is a graph with 1 **node**: ``{0: None}``
    - This is a graph with two nodes: ``{0: None, 1: None}``
    - This is a graph with a node **linked** another: ``{0: {1: None}}``

With this simple instructions we can create more complex graphs. For example:

    - A node linked to itself: ``{0: {0: None}}``
    - Two nodes with looping links: ``{0: {1: None}, 1: {0: None}}``
    - Two nodes with looping links to themselves: ``{0: {0: None}, 1: {1: None}}``
    - A node linked to two other nodes: ``{0: {1: None, 2: None}}``
    - A graph with three nodes: ``{0: None, 1: None, 2: None}``
    - A graph with two nodes linked to each other: ``{0: {1: None}, 1: {0: None}}``
    - A graph with two nodes linked to each other and a third node: ``{0: {1: None}, 1: {0: None}, 2: None}``
    - A graph with two nodes linked to each other and a third node linked to the first node: ``{0: {1: None, 2: None}, 1: {0: None}, 2: {0: None}}``
    - A **directed binary tree** of 3 levels: ``{0: {1: None, 2: None}, 1: {3: None, 4: None}, 2: {5: None, 6: None}}``

Under this definition, all graphs are **directed graphs**. In other words, the links are **one-way**. If we want to create a **bidirectional** graph, we need to add the **inverse** link. For example:

    - A graph with two nodes linked to each other: ``{0: {1: None}, 1: {0: None}}``
    - A graph with two nodes linked to each other and a third node: ``{0: {1: None}, 1: {0: None}, 2: None}``
    - A graph with two nodes linked to each other and a third node linked to the first node: ``{0: {1: None, 2: None}, 1: {0: None}, 2: {0: None}}``

This means that an **undirected graph** is a **directed graph** with **bidirectional** links. For example:

    - A triangle graph: ``{0: {1: None, 2: None}, 1: {0: None, 2: None}, 2: {0: None, 1: None}}``
    - An undirected binary tree of 3 levels: ``{0: {1: None, 2: None}, 1: {0: None, 3: None, 4: None}, 2: {0: None, 5: None, 6: None}, 3: {1: None}, 4: {1: None}, 5: {2: None}, 6: {2: None}}``

