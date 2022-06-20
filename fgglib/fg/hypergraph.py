class Hypergraph:
    # DEFINITION
    # A hypergraph is a 5-Tuple <V, E, att, labV, labE> where
    # • V is a finite set of nodes
    # • E is a finite set of hyperedges
    # • att maps each edge to zero or more endpoint nodes, not necessarily distinct
    # • labV assigns labels to nodes
    # • labE assigns labels to edges

    def __init__(self) -> None:
        self.V = set()
        self.E = set()
        self.att = dict()
        self.labV = dict()
        self.labE = dict()

    # direct constructor for testing
    def __init__(self,_V,_E,_att,_labV,_labE) -> None:
        self.V = _V
        self.E = _E
        self.att = _att
        self.labV = _labV
        self.labE = _labE

    def add_edge(self, edge, lab_edge = None):
        """ adds the edge to E and also to att. And if label is given the label is assigned to the edge  """
        self.E.add(edge)
        self.att[edge] = []
        if lab_edge is not None:
            self.label_edge(edge,lab_edge)

    def add_vertex(self, vertex, lab_vertex = None):
        """ adds the edge to V and if label is given the label is assigned to the vertex """
        self.V.add(vertex)
        if lab_vertex is not None:
            self.label_vertex(vertex, lab_vertex)

    def map_edge(self, edge, nodes) -> None:
        """ maps an edge to nodes. """
        if isinstance(nodes, int):
            self.att[edge].append([nodes])
        else:
            self.att[edge].append(list(nodes))

    def label_edge(self, edge, lab_edge):
        """ assigns label to the edge """
        self.labE[edge] = lab_edge

    def label_vertex(self, vertex, lab_vertex):
        """ assigns label to the vertex """
        self.labV[vertex] = lab_vertex