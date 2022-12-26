*Kladia:* A simple structure for graphs in Python
-------------------------------------------------

Nested Dictionary
+++++++++++++++++

A **nested dictionary** has values of type dictionary. This means that it is possible to define a contain relation between dictionaries, like this one:

    - ``{0: None}`` has **order 0** (it's not nested)
    - ``{0: {0:None}}`` has **order 1** (it's nested once)
    - ``{0: {0: {0: None}}}`` has **order 2** (it's nested twice)

Hence, the **order** on a nested dictionary is the number of times that is nested.

Nodes and Links
+++++++++++++++

A **node** as a nested dictionary of the form ``{node_key: node_value}``, where:

    1. ``node_key`` is an ``integer``.
    2. ``node_value`` is dictionary that contains node's attributes, or a ``None`` type.
    3. ``node_value`` has order 0 or 1.
    4. ``node_value`` can contain links.

We define a **link** as dictionary of the form ``{link_key: link_value}``, where:

    1. ``link_key`` is an ``integer`` corresponding to a node key.
    2. ``link_value`` is a dictionary that contains link's attributes, or a ``None`` type.
    3. Links CAN NOT contain nodes.
    4. Links CAN NOT contain other links.
    5. Two nodes are **linked** if the ``node_key`` of the first node is in the ``node_value`` of the second node.

The following are node and linked nodes examples:

    - ``{0: None}`` a node with key ``0`` and no attributes
    - ``{0: {"label": "node0"}}`` a node with key ``0`` and an attribute ``"label"`` with value ``"node0"``
    - ``{0: {1: None}}`` node 0 is linked to node 1
    - ``{0: {1: None, "weight": 2}}`` is also linked to node 1, but this link also has an attribute ``"weight"`` with value ``2``
    - ``{0: {1: None, 2: None}}`` node ``0`` is linked to nodes 1 and 2

Graphs
++++++

A **graph** of the form ``{graph_key: graph_value}`` has many properties. Here the most important ones:

    1. ``graph_key`` is an ``integer``.
    2. ``graph_value`` is a dictionary that contains nodes.
    3. ``graph_value`` can contain other graphs or graph's attributes.
    4. ``graph_value`` can be ``None`` type.
    5. ``graph_value`` has order 0 or 1.
    6. Nodes in ``graph_value`` are UNIQUE.
    7. All nodes MUST be linked to the graph.
    8. A graph is **empty** is it has no nodes.

Using Python dictionaries we can construct *the simplest non-empty linked graph* with one node and one link in three steps:

    1. Create a graph ``{0: None}`` (order 0)
    2. Add a node ``{0: {0: None}}`` (order 1)
    2. Add a link to itself ``{0: {0: {0: None}}}`` (order 2)

The following are examples of graphs:

    - ``{0: None}`` is an empty graph
    - ``{0: {0: None}}`` is a graph that contains a node with key ``0``
    - ``{0: {0: None, 1: None}}`` is a graph that contains nodes with keys ``0`` and ``1``
    - ``{0: {0: {1: None}, 1: None}}`` is a graph that contains 2 nodes and a link from node ``0`` to node ``1``
    - ``{0: {0: {1: None}, 1: {0: None}}}`` is a graph that contains 2 nodes and two links: from node 0 to node 1 and from node 1 to node 0
    - ``{0: {0: {0:, None, 1: None}, 1: {0: None, 1: None}}}`` is a **complete graph** (a graph with all possible links between it's nodes). It contains:
        - Two nodes: node ``0`` and node ``1``
        - Two links: from node ``0`` to node ``1`` and from node ``1`` to node ``0``
        - Two **looping links**: from node ``0`` to node ``0`` and from node ``1`` to node ``1``

Under this definition, all graphs are **directed graphs**. In other words, the links are one-way.

    - A directed graph with 2 nodes and 2 links ``{0: {0: {1: None}, 1: {0: None}}}``
    - A directed graph with 3 nodes and 4 links ``{0: {0: {1: None, 2: None}, 1: {0: None}, 2: {0: None}}}``
    - A **directed binary tree** of 3 levels: ``{0: {0: {1: None, 2: None}, 1: {3: None, 4: None}, 2: {5: None, 6: None}, 3: None, 4: None, 5: None, 6: None}}``

This means that an **undirected graph** is a graph with **bidirectional** links. If we want to create an undirected graph, we need to add inverted links. For example:

    - An undirected graph with 2 nodes and 1 link ``{0: {0: {1: None}, 1: {0: None}}}``
    - An undirected graph with 3 nodes and 2 links ``{0: {0: {1: None, 2: None}, 1: {0: None}, 2: {0: None}}}``
    - An undirected **triangle** graph: ``{0: {0: {1: None, 2: None}, 1: {0: None, 2: None}, 2: {0: None, 1: None}}}``
    - A **complete graph** (a triangle plus a vertex): ``{0: {0: {1: None, 2: None}, 1: {0: None, 2: None}, 2: {0: None, 1: None, 3: None}, 3: {2: None}}}``
    - A complete graph with 3 nodes: ``{0: {1: None, 2: None}, 1: {0: None, 2: None}, 2: {0: None, 1: None}}``
    - A complete graph with 4 nodes: ``{0: {1: None, 2: None, 3: None}, 1: {0: None, 2: None, 3: None}, 2: {0: None, 1: None, 3: None}, 3: {0: None, 1: None, 2: None}}``