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
            if self.validate_graph(graph_dict):
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

    def nodes(self) -> dict or None:
        """Get all nodes in graph
        :return: dict of nodes
        """

        if self.__graph[self.__label] is None:
            return None
        else:
            _nodes = {}
            # iterate over all nodes
            for node_k, node_p in self.__graph[self.__label].items():
                # if node has properties
                if node_p is not None:
                    for prop_k, prop_v in node_p.items():
                        # if the property is not a link
                        if not isinstance(prop_k, int):
                            _nodes |= {node_k: {prop_k: prop_v}}
                        else:
                            _nodes |= {node_k: None}
                else:
                    # if node has no properties, just copy the node
                    _nodes |= {node_k: None}
            return _nodes

    def links(self) -> dict[[int, int], dict]:
        """Get all the links in graph
        :return: dict of links with keys (from_node, to_node) and properties as values
        """
        if self.__graph[self.__label] is None:
            return {}
        else:
            _links = {}
            # iterate over all nodes
            for node_k, node_p in self.__graph[self.__label].items():
                # if node has properties
                if node_p is not None:
                    for prop_k, prop_v in node_p.items():
                        # if the property is a link
                        if isinstance(prop_k, int):
                            _links |= {(node_k, prop_k): prop_v}
                            # _links[node_k] = {prop_k: prop_v}
            return _links

    def to_matrix(self) -> list[list[float]]:
        """Get graph as adjacency matrix. If nodes do not exist, return empty matrix.
        :return: Adjacency matrix
        :rtype: list
        """
        nodes = self.__graph[self.__label]
        if nodes is None:
            return []
        else:
            matrix = []
            # fill matrix with 0s
            for i in range(len(nodes)):
                matrix.append([0.0] * len(nodes))
            # get links
            links = self.links()
            # iterate over all links
            for link, prop in links.items():
                # get link's nodes
                from_node, to_node = link
                # get link's weight if it exists
                weight = float(prop['weight']) if prop is not None and 'weight' in prop else 1.0
                # add weight to matrix
                matrix[from_node][to_node] = weight
        return matrix

    def from_matrix(self, matrix: list) -> None:
        """Set graph from adjacency matrix
        :param matrix: Adjacency matrix
        """
        if not isinstance(matrix, list):
            raise TypeError("Matrix must be of type list")
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError("Matrix must be of type list of lists")
        if not all(all(isinstance(element, int) or isinstance(element, float) for element in row) for row in matrix):
            raise TypeError("Matrix must be of type list of lists of ints or floats")
        if not all(len(row) == len(matrix) for row in matrix):
            raise ValueError("Matrix must be square")

        self.__graph[self.__label] = None
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] != 0.0:
                    self.add((i, j), {'weight': matrix[i][j]})

    def validate_graph(self, graph_dict) -> bool:
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

    def copy(self):
        """Copy graph
        :return: New instance with a copy of graph
        """
        return Graph(self.__graph[self.__label])

    def union(self, g: object) -> object:
        """Union of two graphs
        :param g: Graph to union with
        :return: Same graph instance with union of two graphs
        """
        if not isinstance(g, Graph):
            raise TypeError("Graph must be of type Graph")

        g_nodes = g.to_dict()['graph']
        b_nodes = self.__graph[self.__label]

        if b_nodes is None and g_nodes is None:
            return self
        elif b_nodes is not None and g_nodes is None:
            return self
        elif b_nodes is None and g_nodes is not None:
            self.__graph[self.__label] = g_nodes
            return self
        else:
            # iterate over all nodes in g
            for node_k, node_p in g_nodes.items():
                # if node does not exist in b
                if node_k not in b_nodes:
                    # add node to b
                    b_nodes |= {node_k: node_p}
                else:
                    # if node has properties
                    if node_p is not None:
                        # iterate over all properties of node in g
                        for prop_k, prop_v in node_p.items():
                            # if property is not a link
                            if not isinstance(prop_k, int):
                                # if property does not exist in b
                                if prop_k not in b_nodes[node_k]:
                                    # add property to b
                                    b_nodes[node_k] |= {prop_k: prop_v}
                                else:
                                    # if property exists in b, overwrite it
                                    b_nodes[node_k][prop_k] = prop_v
                            # if property is a link
                            else:
                                # iterate over all properties of link in g
                                for link_prop_k, link_prop_v in prop_v.items():
                                    # if property does not exist in b
                                    if link_prop_k not in b_nodes[node_k][prop_k]:
                                        # add property to b
                                        b_nodes[node_k][prop_k] |= {link_prop_k: link_prop_v}
                                    else:
                                        # if property exists in b, overwrite it
                                        b_nodes[node_k][prop_k][link_prop_k] = link_prop_v
            self.__graph[self.__label] = b_nodes
            return self
