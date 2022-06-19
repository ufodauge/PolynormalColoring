from copy import deepcopy
from random import choice


class Graph:
    """
    グラフを表現するクラス
    """

    def __init__(self, verticies: list[str],
                 edges: list[list[str, str]]) -> None:
        self.verticies = deepcopy(verticies)
        self.edges = deepcopy(edges)

        # remove duplicate edges
        for i in range(len(self.edges)):
            try:
                for j in range(i + 1, len(self.edges)):
                    if set(self.edges[i]) == set(self.edges[j]):
                        self.edges[j] = None

                self.edges = [e for e in self.edges if e is not None]
            except IndexError:
                pass

        # remove self-loop
        for e in self.edges:
            if e[0] == e[1]:
                self.edges.remove(e)

    def __str__(self) -> str:
        return "Graph(verticies={}, edges={})"\
            .format(self.verticies, self.edges)

    def remove(self, edge: list[str, str]) -> list[str, str]:
        newEdges: list[str, str] = deepcopy(self.edges)
        newEdges.remove(edge)

        return newEdges

    def shortCircuit(self, edge: list[str, str]):
        edge = deepcopy(edge)
        newEdges: list[str, str] = self.remove(edge)

        return Graph(self.verticies, newEdges)

    def contract(self, edge: list[str, str]):
        edge = deepcopy(edge)
        v1: str = edge[0]
        v2: str = edge[1]

        # 当該辺を削除
        newEdges: list[str, str] = self.remove(edge)
        # v2 を削除
        newVerticies: list[str] = deepcopy(self.verticies)
        if v2 in newVerticies:
            newVerticies.remove(v2)
        else:
            newVerticies.remove(v1)

        # v2 に接続されている辺を全て v1 に接続する
        for edge in newEdges:
            if edge[0] == v2:
                edge[0] = v1
            if edge[1] == v2:
                edge[1] = v1

        # remove duplicate edges
        for i in range(len(newEdges)):
            try:
                for j in range(i + 1, len(newEdges)):
                    if set(newEdges[i]) == set(newEdges[j]):
                        newEdges[j] = None

                newEdges = [e for e in newEdges if e is not None]
            except IndexError:
                pass

        # remove self-loop
        for e in newEdges:
            if e[0] == e[1]:
                newEdges.remove(e)

        return Graph(newVerticies, newEdges)

    def getVerticiesCount(self) -> int:
        return len(self.verticies)

    def hasEdge(self) -> bool:
        return len(self.edges) > 0

    def getRandomEdge(self) -> list:
        return choice(self.edges)

    def getFirstEdge(self) -> list:
        return self.edges[0]


if __name__ == "__main__":
    graph1 = Graph(
        # verticies
        ['v1', 'v2', 'v3'],
        # edges
        [['v1', 'v2'], ['v1', 'v2'], ['v3', 'v1'], ['v2', 'v3']])
    graph2 = Graph(
        # verticies
        ['v1', 'v2', 'v3'],
        # edges
        [['v1', 'v2'], ['v3', 'v1'], ['v2', 'v3'], ['v1', 'v2']])

    print(graph1)
    print(graph2)

    # v1 -e1- v2
    # |       |
    # e2      e4
    # |       |
    # v3 -e5- v4
    # \      /
    #  e6  e7
    #   \ /
    #   v5
    graph3 = graph1.shortCircuit(["v2", "v3"])
    print(graph3)

    # v1
    # |
    # e2
    # |
    # v2 -e5- v4
    # \      /
    #  e6  e7
    #   \ /
    #   v5
    graph4 = graph2.contract(["v2", "v3"])
    print(graph4)
