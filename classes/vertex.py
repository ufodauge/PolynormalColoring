class Vertex:
    def __init__(self):
        self.edges = []

    def addEdge(self, edge):
        self.edges.append(edge)

    def removeEdge(self, edge):
        self.edges.remove(edge)

    def getAllEdges(self):
        return self.edges[:]

        