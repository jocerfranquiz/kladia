class GraphSet:
    def __init__(self, id, prop, g_set):
        self.id = id
        self.prop = prop
        self.g_set = g_set

    def to_dict(self):
        return {
            'id': self.id,
            'prop': self.prop,
            'g_set': {id: graph.to_dict() for id, graph in self.g_set.items()}
        }

    @classmethod
    def from_dict(cls, graph_set_dict):
        graph_set = cls(**graph_set_dict)
        for id, graph_dict in graph_set_dict['g_set'].items():
            graph = Graph.from_dict(graph_dict)
            graph_set.g_set[id] = graph
        return graph_set


class Vertex:
    def __init__(self, id, position, prop):
        self.id = id
        self.position = position
        self.prop = prop

    def to_dict(self):
        return {
            'id': self.id,
            'position': self.position,
            'prop': self.prop
        }

    @classmethod
    def from_dict(cls, vertex_dict):
        return cls(**vertex_dict)


class Edge:
    def __init__(self, id, vertices, prop):
        self.id = id
        self.vertices = vertices
        self.prop = prop

    def to_dict(self):
        return {
            'id': self.id,
            'vertices': self.vertices,
            'prop': self.prop
        }

    @classmethod
    def from_dict(cls, edge_dict):
        return cls(**edge_dict)


class Graph:
    def __init__(self, id, prop):
        self.id = id
        self.prop = prop
        self.vertices = {}
        self.edges = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, list):
            for v in vertex:
                self.vertices[v.id] = v
        else:
            self.vertices[vertex.id] = vertex

    def add_edge(self, edge):
        if isinstance(edge, list):
            for e in edge:
                self.edges[e.id] = e
        else:
            self.edges[edge.id] = edge

    def del_edge(self, edge):
        if isinstance(edge, list):
            for e in edge:
                del self.edges[e.id]
        else:
            del self.edges[edge.id]

    def get_vertex_list(self):
        return {'vertices': self.vertices, 'edges': None}

    def get_edge_list(self):
        return {'vertices': None, 'edges': self.edges}

    def del_vertex(self, vertex):
        if isinstance(vertex, list):
            for v in vertex:
                # Delete the vertex from the vertices dictionary
                del self.vertices[v.id]
                # Find the edges that are related to the vertex and delete them
                for e in self.edges.values():
                    if v.id in e.vertices:
                        del self.edges[e.id]
        else:
            # Delete the vertex from the vertices dictionary
            del self.vertices[vertex.id]
            # Find the edges that are related to the vertex and delete them
            for e in self.edges.values():
                if vertex.id in e.vertices:
                    del self.edges[e.id]

    def to_dict(self):
        return {
            'id': self.id,
            'prop': self.prop,
            'vertices': {id: vertex.to_dict() for id, vertex in self.vertices.items()},
            'edges': {id: edge.to_dict() for id, edge in self.edges.items()}
        }

    @classmethod
    def from_dict(cls, graph_dict):
        graph = cls(**graph_dict)
        for id, vertex_dict in graph_dict['vertices'].items():
            vertex = Vertex.from_dict(vertex_dict)
            graph.add_vertex(vertex)
        for id, edge_dict in graph_dict['edges'].items():
            edge = Edge.from_dict(edge_dict)
            graph.add_edge(edge)
        return graph

    @staticmethod
    def union(G1, G2):
        """
        Return the union of two graphs G1 and G2.
        The union of two graphs is a new graph that contains all the vertices and edges
        from both G1 and G2.
        """
        # Create a new Graph object
        G = Graph()
        # Add the vertices and edges from G1 and G2 to the new graph
        G.add_vertex([v for v in G1.vertices.values()])
        G.add_vertex([v for v in G2.vertices.values()])
        G.add_edge([e for e in G1.edges.values()])
        G.add_edge([e for e in G2.edges.values()])
        return G

    @staticmethod
    def inter(G1, G2):
        """
        Return the intersection of two graphs G1 and G2.
        The intersection of two graphs is a new graph that contains only the vertices and edges
        that are common to both G1 and G2.
        """
        # Create a new Graph object
        G = Graph()
        # Add the vertices from G1 and G2 that are common to both graphs
        G.add_vertex([v for v in G1.vertices.values() if v in G2.vertices.values()])
        # Add the edges from G1 and G2 that are common to both graphs
        G.add_edge([e for e in G1.edges.values() if e in G2.edges.values()])
        return G

    @staticmethod
    def c_prd(G1, G2):
        """
        Return the Cartesian product of two graphs G1 and G2.
        The Cartesian product of two graphs is a new graph that has a vertex for each
        possible combination of vertices from G1 and G2.
        """
        # Create a new Graph object
        G = Graph()
        # Add the vertices to the new graph
        for v1 in G1.vertices.values():
            for v2 in G2.vertices.values():
                G.add_vertex(Vertex((v1.id, v2.id), (v1.position, v2.position), (v1.prop, v2.prop)))
        # Add the edges to the new graph
        for e1 in G1.edges.values():
            for e2 in G2.edges.values():
                # Get the start and end vertices for the edge
                start = (G1.vertices[e1.vertices[0]], G2.vertices[e2.vertices[0]])
                end = (G1.vertices[e1.vertices[1]], G2.vertices[e2.vertices[1]])
                G.add_edge(Edge((e1.id, e2.id), (start, end), (e1.prop, e2.prop)))
        return G

    @staticmethod
    def t_prd(G1, G2):
        """
        Return the tensor product of two graphs G1 and G2.
        The tensor product of two graphs is a new graph that has a vertex for each
        possible combination of vertices from G1 and G2, and an edge between any two
        vertices that are connected by an edge in either G1 or G2.
        """
        # Create a new Graph object
        G = Graph()
        # Add the vertices to the new graph
        for v1 in G1.vertices.values():
            for v2 in G2.vertices.values():
                G.add_vertex(Vertex((v1.id, v2.id), (v1.position, v2.position), (v1.prop, v2.prop)))
        # Add the edges to the new graph
        for v1 in G1.vertices.values():
            for v2 in G2.vertices.values():
                # Check if v1 and v2 are connected by an edge in G1
                for e1 in G1.edges.values():
                    if v1.id in e1.vertices and v2.id in e1.vertices:
                        G.add_edge(Edge((e1.id, 0), ((v1.id, v2.id), (v1.id, v2.id)), (e1.prop, 0)))
                # Check if v1 and v2 are connected by an edge in G2
                for e2 in G2.edges.values():
                    if v1.id in e2.vertices and v2.id in e2.vertices:
                        G.add_edge(Edge((0, e2.id), ((v1.id, v2.id), (v1.id, v2.id)), (0, e2.prop)))
        return G

    @staticmethod
    def s_prd(G1, G2):
        """
        Return the strong product of two graphs G1 and G2.
        The strong product of two graphs is a new graph that is the union of the
        Cartesian product and the tensor product of G1 and G2.
        """
        # Get the Cartesian product of G1 and G2
        G_c_prd = Graph.c_prd(G1, G2)
        # Get the tensor product of G1 and G2
        G_t_prd = Graph.t_prd(G1, G2)
        # Return the union of the Cartesian product and the tensor product
        return Graph.union(G_c_prd, G_t_prd)

    @staticmethod
    def get_connected_components(self):
        """
        Return the connected components of the graph as a GraphSet object.
        A connected component is a subgraph of the graph in which every two vertices are
        connected to each other by paths, and which is connected to no other vertices outside
        the subgraph.
        """
        # Create a GraphSet object to store the connected components
        graph_set = GraphSet(0, 0, {})
        # Keep track of the vertices that have been visited
        visited_vertices = set()
        # Iterate through the vertices of the graph
        for v in self.vertices.values():
            # If the vertex has not been visited yet, explore its connected component
            if v not in visited_vertices:
                # Create a new Graph object to store the connected component
                component = Graph(0, 0, {}, {})
                # Explore the connected component starting at vertex v
                component = self._explore_connected_component(v, component, visited_vertices)
                # Add the connected component to the GraphSet object
                graph_set.g_set[len(graph_set.g_set)] = component
        return graph_set

    def _explore_connected_component(self, vertex, component, visited_vertices):
        """
        Explore the connected component of the graph starting at the given vertex, and store it
        in the given Graph object.
        """
        # Add the vertex to the connected component
        component.add_vertex(vertex)
        # Mark the vertex as visited
        visited_vertices.add(vertex)
        # Explore the neighbors of the vertex
        for neighbor in self._get_neighbors(vertex):
            # If the neighbor has not been visited yet, explore its connected component
            if neighbor not in visited_vertices:
                component = self._explore_connected_component(neighbor, component, visited_vertices)
        return component

    def _get_neighbors(self, vertex):
        """
        Return the neighbors of the given vertex.
        """
        neighbors = []
        # Iterate through the edges of the graph
        for edge in self.edges.values():
            # If the vertex is one of the endpoints of the edge, add the other endpoint as a neighbor
            if vertex.id == edge.vertices[0]:
                neighbors.append(self.vertices[edge.vertices[1]])
            elif vertex.id == edge.vertices[1]:
                neighbors.append(self.vertices[edge.vertices[0]])
        return neighbors


if __name__ == "__main__":
    # Create a Graph object
    G = Graph(0, 0, {}, {})
    # Add vertices to the graph
    G.add_vertex(Vertex(0, (0, 0), 0))
    G.add_vertex(Vertex(1, (1, 0), 1))
    G.add_vertex(Vertex(2, (0, 1), 2))
    G.add_vertex(Vertex(3, (1, 1), 3))
    G.add_vertex(Vertex(4, (2, 1), 4))
    # Add edges to the graph
    G.add_edge(Edge(0, (0, 1), 0))
    G.add_edge(Edge(1, (1, 2), 1))
    G.add_edge(Edge(2, (2, 3), 2))
    G.add_edge(Edge(3, (3, 4), 3))
    G.add_edge(Edge(4, (0, 2), 4))
    G.add_edge(Edge(5, (1, 3), 5))
    G.add_edge(Edge(6, (2, 4), 6))
    G.add_edge(Edge(7, (0, 3), 7))
    G.add_edge(Edge(8, (1, 4), 8))
    G.add_edge(Edge(9, (0, 4), 9))
    # Print the graph
    print(G)
    # Print the connected components of the graph
    print(G.get_connected_components(G))

    # Create a GraphSet object
    GS = GraphSet(0, 0, {})
    # Add graphs to the GraphSet object
    GS.add_graph(G)
    GS.add_graph(G)
    GS.add_graph(G)
    # Print the GraphSet object
    print(GS)



##########################################################################################

    # 1. Create a graph with 4 vertices
    G = Graph(0, 0, {}, {})
    v1 = Vertex(1, (1, 1), 0)
    v2 = Vertex(2, (2, 2), 0)
    v3 = Vertex(3, (3, 3), 0)
    v4 = Vertex(4, (4, 4), 0)
    G.add_vertex([v1, v2, v3, v4])
    G.add_edge([Edge(1, (1, 2), 0), Edge(2, (1, 3), 0), Edge(3, (1, 4), 0), Edge(4, (2, 3), 0), Edge(5, (2, 4), 0),
                Edge(6, (3, 4), 0)])

    # 2. Delete a vertex
    G.del_vertex([v3])

    # 3. Check if the graph is connected
    if G.get_connected_components().g_set:
        print("The graph is connected.")
    else:
        print("The graph is not connected.")


