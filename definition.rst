*Kladia:* A simple structure for graphs in Python
-------------------------------------------------

Dictionaries
++++++++++++

In Python a **dictionary** is a data structure that associates keys with values of the form
``{key1: value1, key2: value2, ...}``. For example, the following are dictionaries:
    - ``{0: None}`` with keys ``0`` and values ``None``
    - ``{"a": 1, 'b': 2}`` with keys ``"a"`` and ``"b"`` and values ``1`` and ``2``
    - ``{"l1": [1, 2, 3], 2: [4, 5, 6]}`` with keys ``"l1"`` and ``2`` and values ``[1, 2, 3]``
      and ``[4, 5, 6]``.

A **nested dictionary** has values of type dictionary. For example, the following are nested dictionaries:
    - ``{1: {2: 3, 4: 5}}`` is a dictionary inside a dictionary
    - ``{1: {2: {3: 4, 5: 6}}}`` is a dictionary, inside a dictionary, inside a dictionary

This means that it is possible to define a contain relation between dictionaries, like this one:
    - ``{0: None}`` has **order 0** (it's not nested)
    - ``{0: {0:None}}`` has **order 1** (it's nested once)
    - ``{0: {0: {0: None}}}`` has **order 2** (it's nested twice)

Hence, the **order** of a dictionary is the number of times it is nested.

Graph
+++++

Mathematically, a **graph** is a set of **nodes** or **vertices**, and a set of **edges** or **links**.
Graphs can be represented in *Python* using nested dictionaries of order less than 3. The following are examples of graphs:

    - ``{0: None}`` is an empty graph
    - ``{0: {0: None}}`` is a graph that contains a **node** with key ``0``
    - ``{0: {0: None, 1: None}}`` is a graph that contains nodes with keys ``0`` and ``1``
    - ``{0: {0: {1: None}, 1: None}}`` is a graph that contains 2 nodes and a **link** from node ``0`` to node ``1``
    - ``{0: {0: {1: None}, 1: {0: None}}}`` is a graph that contains 2 nodes and two links: from node 0 to node 1 and from node 1 to node 0
    - ``{0: {0: {0:, None, 1: None}, 1: {0: None, 1: None}}}`` is a **complete graph** (a graph with all possible links between it's nodes). It contains:
        - Two nodes: node ``0`` and node ``1``
        - Two links: from node ``0`` to node ``1`` and from node ``1`` to node ``0``
        - Two **looping links**: from node ``0`` to node ``0`` and from node ``1`` to node ``1``

We define a **node** as a nested dictionary of the form ``{node_key: node_value}``, where:

    1. ``node_key`` is an ``integer``.
    2. ``node_value`` is dictionary that contains links to other nodes or node's attributes, or a ``None`` type.
    3. ``node_value`` has order 0 or 1.
    4. Two nodes are **linked** if the ``node_key`` of the first node is in the ``node_value`` of the second node.
    5. Links CAN NOT contain nodes.

The following are node examples:
    - ``{0: None}`` a node with key ``0`` and no attributes
    - ``{0: {"label": "node0"}}`` a node with key ``0`` and an attribute ``"label"`` with value ``"node0"``
    - ``{0: {1: None}}`` node 0 is linked to node 1
    - ``{0: {1: None, "weight": 2}}`` is also linked to node 1, but this link also has an attribute ``"weight"`` with value ``2``
    - ``{0: {1: None, 2: None}}`` node ``0`` is linked to nodes 1 and 2

Properties of a Graph
+++++++++++++++++++++

A **graph** of the form ``{graph_key: graph_value}`` has many properties. Here the most important ones:

    1. ``graph_key`` is an ``integer``.
    2. ``graph_value`` is a dictionary that contains nodes.
    3. ``graph_value`` can contain other graphs or graph's attributes.
    4. ``graph_value`` can be ``None`` type.
    5. ``graph_value`` has order 0 or 1.
    6. Nodes in ``graph_value`` are UNIQUE.
    7. All nodes MUST be linked to the graph.

We can construct a simple graph with one node and one link the following way:

    1. Create a node ``{0: None}`` (order 0)
    2. Add a link to itself ``{0: {0: None}}`` (order 1)
    3. Create a graph ``{0: {0: {0: None}}}`` (order 2)

This is the simplest non-empty linked graph. A graph is **empy** is it has no nodes.

Let's see some more examples:

    - ``{0: None}`` is an empty graph
    - ``{0: {0: None}}`` is a graph that contains a node 0
    - ``{0: {0: None, 1: None}}`` is a graph that contains nodes 0 and 1
    - ``{0: {0: {1: None}, 1: None}}`` is a graph that contains 2 nodes and a link from node 0 to node 1
    - ``{0: {0: {1: None}, 1: {0: None}}}`` is a graph that contains 2 nodes and two links: from node 0 to node 1 and from node 1 to node 0
    - ``{0: {0: {0:, None, 1: None}, 1: {0: None, 1: None}}}`` contains:
        - Two nodes: node 0 and node 1
        - Two links: from node 0 to node 1 and from node 1 to node 0
        - Two looping links: from node 0 to node 0 and from node 1 to node 1

The following of dictionaries ARE NOT GRAPHS, because they violate the properties defined before:

    - ``{0: {0: None, 1: None, 2: {3: None, 4: None}}}`` is NOT a graph, because node 2 is linked to nodes 3 and 4, but they are **not to the graph**.
    - ``{0: {0: None, 1: None, 1: {0: None, 1: None}}`` is NOT a graph because node 1 is repeated.
    - ``{0: {0: None, 1: None, 2: {3: None, 4: None, 5: {6: None, 7: None}}}}`` is NOT a graph because:
        - It has order 3
        - Node 2 is linked to nodes 3,4, and 5, but **not to the graph**
        - Node 5 links to nodes 6 and 7 are order 3 and this is not allowed.
        - Node 5 is linked to nodes 6 and 7, but they are **not to the graph**

Under this definition, all graphs are **directed graphs**. In other words, the links are one-way. If we want to create a bidirectional graph, we need to add the inverse link. For example:

    - A directed graph with 2 nodes and 2 links ``{0: {0: {1: None}, 1: {0: None}}}``
    - A directed graph with 3 nodes and 4 links ``{0: {0: {1: None, 2: None}, 1: {0: None}, 2: {0: None}}}``
    - A **triangle** graph: ``{0: {0: {1: None, 2: None}, 1: {0: None, 2: None}, 2: {0: None, 1: None}}}`` this is a bidirectional graph with 3 nodes and 6 links
    - A **complete graph** (a triangle plus a vertex): ``{0: {0: {1: None, 2: None}, 1: {0: None, 2: None}, 2: {0: None, 1: None, 3: None}, 3: {2: None}}}`` this is a bidirectional graph with 4 nodes and 12 links

This means that an **undirected graph** is a **directed graph** with **bidirectional** links. For example:

    - A undirected graph with 2 nodes and 1 link ``{0: {0: {1: None}, 1: {0: None}}}`` is a directed graph with 2 nodes and 2 links
    - A undirected graph with 3 nodes and 2 links ``{0: {0: {1: None, 2: None}, 1: {0: None}, 2: {0: None}}}`` is a directed graph with 3 nodes and 4 links

A graph is **complete** if it has **all** the possible links. For example:

    - A complete graph with 3 nodes: ``{0: {1: None, 2: None}, 1: {0: None, 2: None}, 2: {0: None, 1: None}}``
    - A complete graph with 4 nodes: ``{0: {1: None, 2: None, 3: None}, 1: {0: None, 2: None, 3: None}, 2: {0: None, 1: None, 3: None}, 3: {0: None, 1: None, 2: None}}``