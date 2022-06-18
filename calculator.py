import sympy as sp

from classes.graph import Graph

n = sp.Symbol("n")


def calcPolynormalColoring(graph: Graph, depth: int) -> sp.core.expr.Expr:
    if graph.hasEdge():
        edge = graph.getRandomEdge()

        print("  " * depth + "edge: {}".format(edge))

        # get a new edge-removed graph (copy)
        shortCircuited = graph.shortCircuit(edge)
        # get a new edge-contracted graph (copy)
        contracted = graph.contract(edge)

        print("  " * depth + "shortCircuited:", shortCircuited)
        print("  " * depth + "contracted:", contracted)

        return calcPolynormalColoring(shortCircuited, depth + 1) \
            - calcPolynormalColoring(contracted, depth + 1)

    else:
        verticiesCount = graph.getVerticiesCount()
        return n**verticiesCount
