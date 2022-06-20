import time

from calculator import calcPolynormalColoring, calcPolynormalColoring2
from classes.graph import Graph

import sympy as sp

n = sp.Symbol("n")

# K_3
graph1 = Graph(
    # verticies
    ["v1", "v2", "v3"],
    # edges
    [["v1", "v2"],
     ["v1", "v3"],
     ["v2", "v3"]])

expected1 = n * (n - 1) * (n - 2)
expected1 = expected1.expand()

# K_5
graph2 = Graph(
    # verticies
    ["v1", "v2", "v3", "v4", "v5"],
    # edges
    [["v1", "v2"],
     ["v1", "v3"],
     ["v1", "v4"],
     ["v1", "v5"],
     ["v2", "v3"],
     ["v2", "v4"],
     ["v2", "v5"],
     ["v3", "v4"],
     ["v3", "v5"],
     ["v4", "v5"]])

expected2 = n * (n - 1) * (n - 2) * (n - 3) * (n - 4)
expected2 = expected2.expand()

# 6-verticies tree
graph3 = Graph(
    # verticies
    ["v1", "v2", "v3", "v4", "v5", "v6"],
    # edges
    [["v1", "v4"],
     ["v2", "v4"],
     ["v3", "v4"],
     ["v5", "v4"],
     ["v5", "v6"]])

expected3 = n * (n - 1)**5
expected3 = expected3.expand()

# 7-verticies cycle
graph4 = Graph(
    # verticies
    ["v1", "v2", "v3", "v4", "v5", "v6", "v7"],
    # edges
    [["v1", "v2"],
     ["v2", "v3"],
     ["v3", "v4"],
     ["v4", "v5"],
     ["v5", "v6"],
     ["v6", "v7"],
     ["v7", "v1"]])

expected4 = (n - 1)**7 + (n - 1) * (-1)**7
expected4 = expected4.expand()

# petersen graph
graph5 = Graph(
    # verticies
    ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9", "v10"],
    # edges
    [["v1", "v6"],
     ["v2", "v7"],
     ["v3", "v8"],
     ["v4", "v9"],
     ["v5", "v10"],
     ["v1", "v2"],
     ["v2", "v3"],
     ["v3", "v4"],
     ["v4", "v5"],
     ["v5", "v1"],
     ["v6", "v8"],
     ["v8", "v10"],
     ["v10", "v7"],
     ["v7", "v9"],
     ["v9", "v6"]])

expected5 = n * (n - 1) * (n - 2) * (n**7 - 12 * n**6 + 67 *
                                     n**5 - 230 * n**4 + 529 * n**3 - 814 * n**2 + 775 * n - 352)
expected5 = expected5.expand()

for tpl in [(graph1, expected1), (graph2, expected2),
            (graph3, expected3), (graph4, expected4), (graph5, expected5)]:
    graph, expected = tpl
    print(graph)
    start_1 = time.time()
    result_1 = calcPolynormalColoring(graph)
    end_1 = time.time()

    start_2 = time.time()
    result_2 = calcPolynormalColoring2(graph)
    end_2 = time.time()

    try:
        assert result_1 == expected
        assert result_2 == expected
    except AssertionError:
        print("!!calcPolynormalColoring and calcPolynormalColoring2 are not equal!!")
        print("expected:", expected)
        print("calcPolynormalColoring:", result_1)
        print("calcPolynormalColoring2:", result_2)
        print("calcPolynormalColoring took", end_1 - start_1, "seconds.")
        print("calcPolynormalColoring2 took", end_2 - start_2, "seconds.")
        print("")
    else:
        print("calcPolynormalColoring:", result_1)
        print("calcPolynormalColoring2:", result_2)
        print("calcPolynormalColoring took", end_1 - start_1, "seconds.")
        print("calcPolynormalColoring2 took", end_2 - start_2, "seconds.")
        print("")

    print()
