"""
This module contains all the classes and functions for the construction of graphs.
author: @jocerfranquiz
date: 2022-12-31
version: 0.0.1
"""


class Graph:
    """Graph class
    :param graph: Graph to initialize with. Defaults to None.
    """

    def __init__(self, graph=None) -> None:
        """Initialize graph
        :param graph:  to initialize with. Defaults to None.
        """

        self.__label = 'graph'
        self.__graph = {self.__label: None}

        if graph is not None:
            if self.__validate_graph(graph):
                self.__graph |= graph

    def to_dict(self) -> dict:
        """Get graph
        :return: Graph
        """
        return self.__graph

    def add(self, obj: int or (int, int), properties: dict or None = None) -> None:
        """Add node or link to graph
        :param obj: Node key (int) or link (int, int) to add
        :param properties: Node or link's properties. Defaults to None.
        """
        if isinstance(obj, int):
            self.__add_node(obj, properties)
        elif isinstance(obj, tuple):
            self.__add_link(obj, properties)
        else:
            raise TypeError("Object must be of type int or tuple")

    def dlt(self, obj: int or (int, int)) -> None:
        """Delete node or link from graph
        :param obj: Node key (int) or link (int, int) to delete
        """
        if isinstance(obj, int):
            self.__dlt_node(obj)
        elif isinstance(obj, tuple):
            self.__dlt_link(obj)
        else:
            raise TypeError("Object must be of type int or tuple")

    def __add_node(self, node_key: int, properties: dict or None = None) -> None:
        """Add node to graph
        :param node_key: Node's key
        :param properties: Node's properties. Defaults to None.
        """
        if not isinstance(node_key, int):
            raise TypeError("Node's key must be of type int")
        if properties is not None and not isinstance(properties, dict):
            raise TypeError("Properties must be of type dict")

        nodes = self.__graph[self.__label]
        if nodes is None:
            self.__graph[self.__label] = {node_key: properties}
        else:
            if node_key not in nodes:
                self.__graph[self.__label] |= {node_key: properties}
            else:
                raise ValueError("Node already exists")

    def __add_link(self, link: tuple, properties: dict or None = None) -> None:
        """Add link to graph. If nodes do not exist, they will be added with properties=None.
        :param link: Link to add
        :param properties: Link properties. Defaults to None.
        """
        if not isinstance(link, tuple):
            raise TypeError("Link must be of type tuple")
        if not all(isinstance(node, int) for node in link):
            raise TypeError("Node's keys must be of type int")
        if properties is not None and not isinstance(properties, dict):
            raise TypeError("Properties must be of type dict")

        from_node, to_node = link
        nodes = self.__graph[self.__label]
        if nodes is None:
            self.__graph[self.__label] = {from_node: {to_node: properties}}
        else:
            if from_node not in nodes:
                self.__graph[self.__label] |= {from_node: {to_node: properties}}
            else:
                if nodes[from_node] is None:
                    self.__graph[self.__label][from_node] = {to_node: properties}
                else:
                    if to_node not in nodes[from_node]:
                        self.__graph[self.__label][from_node] |= {to_node: properties}
                    else:
                        raise ValueError("This link already exists")

            # Add to_node if not already in graph

            if to_node not in nodes:
                self.__graph[self.__label] |= {to_node: None}

    def __dlt_node(self, node_key: int) -> None:
        """Delete node from graph
        :param node_key: Node's key to delete
        """
        if not isinstance(node_key, int):
            raise TypeError("Node's key must be of type int")

        nodes = self.__graph[self.__label]
        if nodes is None:
            raise ValueError("Graph is empty, nothing to delete")
        else:
            if node_key in nodes:
                del self.__graph[self.__label][node_key]
                for key in nodes:
                    if key != self.__label and nodes[key] is not None and node_key in nodes[key]:
                        del self.__graph[self.__label][key][node_key]
            else:
                raise ValueError("Node does not exist")

    def __dlt_link(self, link: (int, int)) -> None:
        """Delete link from graph
        :param link: Link to delete
        """
        if not isinstance(link, tuple):
            raise TypeError("Link must be of type tuple")
        if not all(isinstance(key, int) for key in link):
            raise TypeError("Node's keys must be of type int")

        from_node, to_node = link
        nodes = self.__graph[self.__label]
        if nodes is None:
            raise ValueError("Graph is empty, nothing to delete")
        else:
            if from_node in nodes:
                if to_node in nodes[from_node]:
                    del self.__graph[self.__label][from_node][to_node]
                    self.__graph[self.__label][from_node] = None \
                        if len(self.__graph[self.__label][from_node]) == 0 \
                        else self.__graph[self.__label][from_node]
                else:
                    raise ValueError("Link does not exist")
            else:
                raise ValueError("Link does not exist")

    def nodes(self) -> list:
        """Get all nodes in graph
        :return: List of nodes
        """
        nodes = self.__graph[self.__label]
        if nodes is None:
            return []
        else:
            return list(nodes.keys())

    def links(self) -> list:
        """Get all the links in graph
        :return: List of links
        """
        _links = []
        nodes = self.__graph[self.__label]
        if nodes is not None:
            for key in nodes:
                if nodes[key] is not None:
                    for to_node in nodes[key]:
                        _links.append((key, to_node))
        return _links

    def __validate_graph(self, graph) -> bool:
        """Validate graph
        :param graph: Graph to validate
        :return: True if valid, False otherwise
        """

        # Graph must be of type dict
        if not isinstance(graph, dict):
            raise TypeError("Graph must be of type dict")

        # Graph must have GRAPH_LABEL key
        if self.__label not in graph:
            raise ValueError(f'Graph key must be "{self.__label}"')

        # Graph keys must be of type str
        if not all(isinstance(key, int) or isinstance(key, str) for key in graph):
            raise TypeError("Graph keys must be of type int or str")

        # Graph values must be of type dict or None
        if not all(isinstance(value, dict) or value is None for value in graph.values()):
            raise TypeError("Graph values must be of type dict or None")
        return True


if __name__ == '__main__':
    g = Graph()  # create an empty graph
    g.add(0, {'color': 'red'})  # add a node with a property
    g.add(1, {'color': 'blue'})  # add another node with a property
    g.add((0, 1), {'weight': 1.0})  # add a looping link with a property

    print(g.to_dict())

    # Test add_node
    g1 = Graph()
    g1.add(0, {'name': 'Node 0'})
    g1.add(2)
    print(f'g1: {g1.to_dict()}')
    try:
        g2 = Graph({'graph': {0: {3: {'label': 'node3'}}, 1: None, 3: None, 4: None}})
        print(f'g2: {g2.to_dict()}')
    except Exception as e:
        print(f'g2: {e}')
    try:
        g3 = Graph({'grap': {0: None}})
    except Exception as e:
        print(f'g3 error: {e}')

    # Test add for links
    g4 = Graph()
    g4.add((1, 2), {'label': 'link1'})
    g4.add((2, 3))
    g4.add((4, 4))
    print(f'g4: {g4.to_dict()}')

    # Test delete_node
    g5 = Graph({'graph': {0: {3: {'label': 'node3'}}, 1: None, 3: None, 4: None}})
    g5.dlt(0)
    print(f'g5: {g5.to_dict()}')

    # Test delete link
    g6 = Graph({'graph': {0: {3: {'label': 'node3'}}, 1: None, 3: None, 4: None}})
    g6.dlt((0, 3))
    print(f'g6: {g6.to_dict()}')

    # Test nodes
    g7 = Graph({'graph': {0: {3: {'label': 'node3'}}, 1: None, 2: None, 3: None}})
    print(f'g7 nodes: {g7.nodes()}')

    # Test links
    triangular_graph = Graph({'graph': {
        0: {1: {'label': 'link1'}},
        1: {2: {'label': 'link2'}},
        2: {0: {'label': 'link3'}},
    }})
    print(f'triangular_graph links: {triangular_graph.links()}')
