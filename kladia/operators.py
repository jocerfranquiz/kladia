"""
This module contains operations between graphs.
author: @jocerfranquiz
date: 2022-12-31
version: 0.0.1
"""
from kladia.graph import Graph


def union(graph1: Graph, graph2: Graph) -> Graph:
    """Union of two graphs. If nodes do not exist, return empty graph.
    :param graph1: First graph
    :param graph2: Second graph
    :return: Union of two graphs.
    """
    if not isinstance(graph1, Graph):
        raise TypeError("Graph1 must be of type Graph")
    if not isinstance(graph2, Graph):
        raise TypeError("Graph2 must be of type Graph")

    # Dicts of nodes and links
    graph1_nodes = graph1.to_dict()['graph']
    graph2_nodes = graph2.to_dict()['graph']

    if graph1_nodes is not None and graph2_nodes is not None:
        nodes = {}  # Nodes of union graph
        nodes |= graph1_nodes  # Add nodes of graph1

        # Add nodes of graph2
        for node_key in graph2_nodes:
            if node_key in graph1_nodes:  # If node is already in graph1
                if nodes[node_key] is None:  # If node has no links
                    nodes[node_key] = graph2_nodes[node_key]  # Add links of graph2
                else:  # If node has links
                    for link_key in graph2_nodes[node_key]:
                        if nodes[node_key][link_key] is None:  # If link has no properties
                            nodes[node_key][link_key] = graph2_nodes[node_key][link_key]  # Add properties of link
                        else:  # If link has properties
                            nodes[node_key][link_key] |= graph2_nodes[node_key][link_key]
            else:  # If node is not in graph1
                nodes |= {node_key: graph2_nodes[node_key]}
        return Graph({'graph': nodes})
    elif graph1_nodes is None:
        return graph2
    elif graph2_nodes is None:
        return graph1
    else:
        return Graph()

# def intersection(graph1: Graph, graph2: Graph) -> Graph:
#     """Intersection of two graphs
#     :param graph1: First graph
#     :param graph2: Second graph
#     :return: Intersection of two graphs
#     """
#     if not isinstance(graph1, Graph):
#         raise TypeError("Graph1 must be of type Graph")
#     if not isinstance(graph2, Graph):
#         raise TypeError("Graph2 must be of type Graph")
#
#     # Dicts of nodes and links
#     graph1_nodes = graph1.to_dict()['graph']
#     graph2_nodes = graph2.to_dict()['graph']
#
#     if graph1_nodes is not None and graph2_nodes is not None:
#         nodes = {}
#         for node_key in graph1_nodes:
#             if node_key in graph2_nodes:
#                 nodes[node_key] = {}
#                 for link_key in graph1_nodes[node_key]:
#                     if link_key in graph2_nodes[node_key]:
#                         nodes[node_key][link_key] = graph1_nodes[node_key][link_key] & graph2_nodes[node_key][link_key]
#         return Graph({'graph': nodes})
#     else:
#         return Graph()

