from copy import deepcopy
from random import choice


class Graph:
    """
    グラフを表現するクラス
    """
    def __init__(self, edges: dict[list[str, str]]) -> None:
        self.edges = deepcopy(edges)

    def remove(self, edge: str) -> dict[list[str, str]]:
        newEdges: dict[list[str, str]] = deepcopy(self.edges)
        newEdges.pop(edge)

        return newEdges

    def shortCircuit(self, edge: str):
        newEdges: dict[list[str, str]] = self.remove(edge)

        return Graph(newEdges)

    def contract(self, edge: str):
        # edge について
        # 一つの頂点に接続されていた辺を
        # もう一方の頂点に接続する
        v1: str = self.edges[edge][0]
        v2: str = self.edges[edge][1]

        newEdges: dict[list[str, str]] = self.remove(edge)

        for edge in newEdges:
            if v1 in newEdges[edge]:
                newEdges[edge][0] = v2

        return Graph(newEdges)

    def getVerticiesCount(self) -> int:
        verticies = []
        for edge in self.edges:
            verticies.append(self.edges[edge][0])
            verticies.append(self.edges[edge][1])

        return len(set(verticies))

    def hasEdge(self) -> bool:
        return len(self.edges) > 0

    def getRandomEdge(self) -> str:
        return choice(self.edges.keys())


if __name__ == "__main__":
    graph1 = Graph({
        "e1": ["v1", "v2"],
        "e2": ["v1", "v3"],
        "e3": ["v2", "v3"],
        "e4": ["v2", "v4"],
        "e5": ["v3", "v4"],
        "e6": ["v3", "v5"],
        "e7": ["v4", "v5"],
    })
    graph2 = Graph({
        "e1": ["v1", "v2"],
        "e2": ["v1", "v3"],
        "e3": ["v2", "v3"],
        "e4": ["v2", "v4"],
        "e5": ["v3", "v4"],
        "e6": ["v3", "v5"],
        "e7": ["v4", "v5"],
    })
    print(graph1.getVerticiesCount(), graph2.getVerticiesCount())

    graph3 = graph1.remove("e1")
    print(graph3.getVerticiesCount(), graph2.getVerticiesCount())

    graph4 = graph2.contract("e1")
    print(graph1.getVerticiesCount(), graph4.getVerticiesCount())
