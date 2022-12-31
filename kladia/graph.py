"""
This module contains all the classes and functions for the construction of graphs.
author: @jocerfranquiz
date: 2022-12-31
version: 0.0.1
"""


def graph(graph_dict: dict = None):
    """This function returns a Graph instance
    :param graph_dict: A dictionary with the graph data
    """
    if graph_dict is None:
        return Graph()
    else:
        return Graph(graph_dict)


class Graph:
    """Graph class private methods"""

    def __init__(self, graph_dict: dict = None) -> None:
        """Initialize graph with empty dict
        of the form {"graph": None}
        """

        if graph_dict is not None:
            keys = list(graph_dict.keys())
            if len(keys) == 1 and keys[0] == 'graph':
                self.__label = keys[0]
            else:
                raise ValueError("Incorrect graph format")
            if self.__validate_graph(graph_dict):
                self.__label = 'graph'
                self.__graph = graph_dict
            else:
                raise ValueError("Incorrect graph format")
        else:
            self.__label = 'graph'
            self.__graph = {self.__label: None}

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

    def to_matrix(self) -> list:
        """Get graph as adjacency matrix. If nodes do not exist, return empty matrix.
        :return: Adjacency matrix
        :rtype: list
        """
        nodes = self.__graph[self.__label]
        if nodes is None:
            return []
        else:
            matrix = []
            for i in range(len(nodes)):
                matrix.append([0] * len(nodes))  # Initialize matrix with 0s
            for from_node in nodes:
                if nodes[from_node] is not None:
                    for to_node in nodes[from_node]:
                        matrix[from_node][to_node] = 1  # Set 1 if link exists
            return matrix

    def __validate_graph(self, graph_dict) -> bool:
        """Validate graph
        :param graph_dict: Graph to validate
        :return: True if valid, False otherwise
        """

        # Graph must be of type dict
        if not isinstance(graph_dict, dict):
            raise TypeError("Graph must be of type dict")

        # Graph must have 'graph' key
        if self.__label not in graph_dict:
            raise ValueError(f'Graph key must be "{self.__label}"')

        # Graph keys must be of type str
        if not all(isinstance(key, int) or isinstance(key, str) for key in graph_dict):
            raise TypeError("Graph keys must be of type int or str")

        # Graph values must be of type dict or None
        if not all(isinstance(value, dict) or value is None for value in graph_dict.values()):
            raise TypeError("Graph values must be of type dict or None")
        return True
