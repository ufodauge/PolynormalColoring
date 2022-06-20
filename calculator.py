# import asyncio
import sympy as sp
from classes.graph import Graph


class ProgressData:
    def __init__(self, depth: int):
        self.depthProgress = []
        self.depthProgressMax = []

    def update(self, depth: int):
        i = len(self.depthProgress)
        while i <= depth:
            self.depthProgress.append(0)
            self.depthProgressMax.append(0)
            self.depthProgressMax[i] = 2 ** i
            i += 1
            print("\033[1E")
        self.depthProgress[depth] += 1

    def updateAllBelow(self, depth: int):
        for i in range(depth, len(self.depthProgress)):
            if len(self.depthProgress) <= i:
                self.depthProgress.append(0)
                self.depthProgressMax.append(0)
                self.depthProgressMax[i] = 2 ** i
                print("\033[1E")
            self.depthProgress[i] += 2 ** (i - depth)

    def print(self):
        # print all progress data
        print("\033[{}F".format(len(self.depthProgress) + 1))
        for i in range(len(self.depthProgress)):
            percent = self.depthProgress[i] / self.depthProgressMax[i] * 100
            progressInt = int(percent / 2)
            print(
                "{:3d} |".format(i)
                + "#" * (progressInt)
                + " " * (50 - progressInt)
                + "| {:.6f}%".format(percent),
            )
            # print("depth {}: {}".format(i, self.depthProgress[i]) + " " * 10)


def calcPolynormalColoring(
    graph: Graph, depth: int = 0, pd: ProgressData = ProgressData(0)
) -> sp.core.expr.Expr:
    n: sp.core.symbol.Symbol = sp.symbols("n")
    if graph.hasEdge():
        edge: list[str, str] = graph.getRandomEdge()

        # get a new edge-removed graph (copy)
        shortCircuited = graph.shortCircuit(edge)
        # get a new edge-contracted graph (copy)
        contracted = graph.contract(edge)

        result = calcPolynormalColoring(
            shortCircuited, depth + 1, pd
        ) - calcPolynormalColoring(contracted, depth + 1, pd)

        pd.update(depth)
        pd.print()
        return result

    else:
        pd.updateAllBelow(depth)

        verticiesCount = graph.getVerticiesCount()
        pd.print()
        return n ** verticiesCount


def calcPolynormalColoring2(graph: Graph) -> sp.core.expr.Expr:
    n: sp.core.symbol.Symbol = sp.symbols("n")
    stack: list[tuple[Graph, int]] = [(graph, sp.Integer(1))]
    expr: sp.core.expr.Expr = sp.Integer(0)
    while stack:
        tpl = stack.pop()
        graph = tpl[0]
        sign = tpl[1]
        if graph.hasEdge():
            edge: list[str, str] = graph.getRandomEdge()

            # get a new edge-removed graph (copy)
            shortCircuited: Graph = graph.shortCircuit(edge)
            # get a new edge-contracted graph (copy)
            contracted: Graph = graph.contract(edge)

            stack.append((shortCircuited, sign))
            stack.append((contracted, -sign))

        else:
            verticiesCount: int = graph.getVerticiesCount()
            expr += n ** verticiesCount * sign

    return expr
