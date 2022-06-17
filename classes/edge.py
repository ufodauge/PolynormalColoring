class Edge:
    def __init__(self, v1, v2):
        v1.addEdge(self)
        v2.addEdge(self)
        self.v1 = v1
        self.v2 = v2

    def getVerticies(self):
        return [self.v1, self.v2]

    def remove(self):
        # 接続情報を削除
        self.v1.removeEdge(self)
        self.v2.removeEdge(self)

    def contract(self):
        # 接続情報を削除
        self.v1.removeEdge(self)
        self.v2.removeEdge(self)

        # v2の全ての辺をv1に接続し、
        # v2からは消去
        edges = self.v2.getAllEdges()
        for edge in edges:
            self.v1.addEdge(edge)
            self.v2.removeEdge(edge)
