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

graph = Graph({
    "e1": ["v1", "v2"],
    "e2": ["v1", "v3"],
    "e3": ["v2", "v3"],
    "e4": ["v2", "v4"],
    "e5": ["v3", "v4"],
    "e6": ["v3", "v5"],
    "e7": ["v4", "v5"],
})

print(calcPolynormalColoring(graph))
