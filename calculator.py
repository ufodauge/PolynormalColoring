import sympy as sp
from classes.graph import Graph


class ProgressData:
    def __init__(self, depth: int):
        self.depthProgress = []

    def update(self, depth: int):
        if len(self.depthProgress) <= depth:
            self.depthProgress.append(0)
        self.depthProgress[depth] += 1

    def print(self):
        # print all progress data
        for i in range(len(self.depthProgress)):
            print("depth {}: {}          ".format(i, self.depthProgress[i]))

        print("\033[{}F".format(len(self.depthProgress) + 1))


def calcPolynormalColoring(
        graph: Graph,
        depth: int = 0,
        pd: ProgressData = ProgressData(0)) -> sp.core.expr.Expr:
    n: sp.core.symbol.Symbol = sp.symbols("n")
    pd.update(depth)
    pd.print()

    if graph.hasEdge():
        edge: list[str, str] = graph.getRandomEdge()

        # get a new edge-removed graph (copy)
        shortCircuited = graph.shortCircuit(edge)
        # get a new edge-contracted graph (copy)
        contracted = graph.contract(edge)

        return calcPolynormalColoring(shortCircuited, depth + 1, pd) + \
            - calcPolynormalColoring(contracted, depth + 1, pd)

    else:
        verticiesCount = graph.getVerticiesCount()
        return n**verticiesCount


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
            expr += n**verticiesCount * sign

    return expr
