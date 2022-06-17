from calculator import calcPolynormalColoring
from classes.graph import Graph

# グラフの構成
# こんなやつ
# v1 -e1- v2
# |     / |
# e2  e3  e4
# |  /    |
# v3 -e5- v4
# \      /
#  e6  e7
#   \ /
#   v5

graph = Graph(
    # verticies
    ["v1", "v2", "v3", "v4", "v5"],
    # edges
    [["v1", "v2"],
     ["v1", "v3"],
     ["v2", "v3"],
     ["v2", "v4"],
     ["v3", "v4"],
     ["v3", "v5"],
     ["v4", "v5"]])

print(calcPolynormalColoring(graph))
