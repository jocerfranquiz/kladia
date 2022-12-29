from utils import get_size


class Graph(object):
    def __init__(self, graph=None, properties=None):
        """Initialize graph
        Args:
            graph (dict, optional): Graph to initialize with. Defaults to None.
            properties (dict, optional): Properties of graph. Defaults to None.
        """

        self.__graph = {}

        if graph is None:
            if properties is None:
                self.__graph |= {'graph': None}
            else:
                if self.validate_properties(properties):
                    self.__graph |= properties
        else:
            if self.validate_graph(graph):
                self.__graph |= graph
                if properties is not None and self.validate_properties(properties):
                    self.__graph = properties

    def add_node(self, node):
        """Add node to graph
        :param node: Node to add
            node (dict): node of the form {node_key: node_value}
            with node_key (int) being the key of the node to add
        :return:
            None
        """
        # Validate node
        if not isinstance(node, dict):
            raise TypeError("Node must be of type dict")
        if len(node) != 1:
            raise ValueError("Node must be of form {node_key: node_value}")
        if not isinstance(list(node.keys())[0], int):
            raise TypeError("Node key must be of type int")
        if not (isinstance(list(node.values())[0], dict) or list(node.values())[0] is not None):
            raise TypeError("Node value must be of type dict or None")

        # Add node to graph
        if node not in self.__graph:
            self.__graph |= node

    def add_edge(self, edge, properties=None):
        """Add edge to graph
        :param properties: Properties of edge
        :param edge: Edge to add
            edge (dict): edge of the form {node_key: node_value}
            with node_key (int) being the key of the node to add
        :return: None
        """

        # Validate edge
        if not isinstance(edge, tuple):
            raise TypeError("Edge must be of type tuple")
        if len(edge) != 2:
            raise ValueError("Edge must be of form (node_key_1, node_key_2)")
        if not (isinstance(edge[0], int) or not isinstance(edge[1], int)):
            raise TypeError("Node_keys must be of type int")

        # Validate properties
        if properties is not None and self.validate_properties(properties):
            raise TypeError("Properties must be of type dict")

        from_node = edge[0]
        to_node = edge[1]

        # Add edge to graph
        if from_node not in self.__graph:
            # Add from_node to graph with edge as value
            self.__graph |= {from_node: {to_node: properties}}
        else:
            # Add edge to from_node
            if self.__graph[from_node] is None:
                self.__graph[from_node] = {to_node: properties}
            else:
                if to_node not in self.__graph[from_node]:
                    self.__graph[from_node] |= {to_node: properties}
                else:
                    raise ValueError("Edge already exists")

        # Add to_node if not already in graph
        if to_node not in self.__graph:
            self.__graph |= {to_node: None}

    def get_dict(self):
        return self.__graph

    # validate graph
    @staticmethod
    def validate_graph(graph):
        """Validate graph
        :param graph: Graph to validate
        :return: True if valid, False otherwise
        """

        # Validate graph
        if not isinstance(graph, dict):
            raise TypeError("Graph must be of type dict")

        # Validate graph properties
        if 'graph' in graph:
            if not isinstance(graph['graph'], dict):
                raise TypeError("Graph properties must be of type dict")

        # Validate nodes
        for node in graph:
            if node != 'graph':
                if not isinstance(node, int):
                    raise TypeError("Node key must be of type int")
                if not (isinstance(graph[node], dict) or graph[node] is None):
                    raise TypeError("Node value must be of type dict or None")

                # Validate edges
                for edge in graph[node]:
                    if not isinstance(edge, int):
                        raise TypeError("Edge key must be of type int")
                    if not (isinstance(graph[node][edge], dict) or graph[node][edge] is None):
                        raise TypeError("Edge value must be of type dict or None")

        return True

    # Validate properties of the graph
    @staticmethod
    def validate_properties(properties):
        """Validate properties of the graph
        :param properties: properties of the graph
        :return: True if properties are valid, False otherwise
        """
        if not isinstance(properties, dict):
            raise TypeError("Properties must be of type dict")
        if not all(isinstance(k, str) for k in properties.keys()):
            raise TypeError("Property keys must be of type str")
        return True

    def get_size(self):
        """Get size of graph
        :return: Size of graph
        """
        return get_size(self.__graph)

    def nodes(self):
        """Get nodes of graph
        :return: Nodes of graph
        """
        nodes = []
        for node in self.__graph:
            if node != 'graph':
                nodes.append(node)
        return nodes

    def edges(self):
        """Get edges of graph
        :return: Edges of graph
        """
        edges = []
        for node in self.__graph:
            if node != 'graph' and self.__graph[node] is not None:
                for edge in self.__graph[node]:
                    edges.append((node, edge))
        return edges


if __name__ == "__main__":
    g = Graph()
    g.add_edge((0, 1))
    g.add_edge((0, 2))
    g.add_edge((0, 3))
    g.add_edge((1, 2))
    g.add_edge((1, 3))
    g.add_edge((2, 3))
    try:
        g.add_edge((0, 1))
    except Exception as e:
        print(e)
    print(g.get_dict())
    print(f"nodes: {g.nodes()}\nedges: {g.edges()}")
    print(round(get_size(g) / 1024, 2), "KB")
