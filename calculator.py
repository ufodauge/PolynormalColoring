import sympy as sp

from classes.graph import Graph

n = sp.Symbol("n")


def calcPolynormalColoring(graph: Graph) -> sp.core.expr.Expr:
    if graph.hasEdge():
        edge = graph.getRandomEdge()

        # get a new edge-removed graph (copy)
        shortCircuited = graph.shortCircuit(edge)
        # get a new edge-contracted graph (copy)
        contracted = graph.contract(edge)

        return calcPolynormalColoring(shortCircuited) \
            - calcPolynormalColoring(contracted)

    else:
        verticiesCount = graph.getVerticiesCount()
        return n**verticiesCount
