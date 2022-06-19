import sympy as sp
from classes.graph import Graph



def calcPolynormalColoringOptimized(graph: Graph) -> sp.core.expr.Expr:
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



def calcPolynormalColoring(graph: Graph) -> sp.core.expr.Expr:
    n: sp.core.symbol.Symbol = sp.symbols("n")
    if graph.hasEdge():
        edge: list[str, str] = graph.getRandomEdge()

        # get a new edge-removed graph (copy)
        shortCircuited = graph.shortCircuit(edge)
        # get a new edge-contracted graph (copy)
        contracted = graph.contract(edge)

        return calcPolynormalColoring(shortCircuited) \
            - calcPolynormalColoring(contracted)

    else:
        verticiesCount = graph.getVerticiesCount()
        return n**verticiesCount
