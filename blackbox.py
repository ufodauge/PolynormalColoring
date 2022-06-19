import time

from tqdm import tqdm
from calculator import calcPolynormalColoring, calcPolynormalColoringOptimized
from classes.graph import Graph
import random


def blackboxTest():
    for i in range(100):
        verticies: list[str] = []
        edges: list[str, str] = []

        # verticies
        for i in range(random.randint(1, 10)):
            verticies.append("v" + str(i + 1))

        # edges
        for i in range(random.randint(1, 30)):
            v1: str = random.choice(verticies)
            v2: str = random.choice(verticies)
            if v1 != v2:
                edges.append([v1, v2])

        graph: Graph = Graph(verticies, edges)

        # validate results of calcPolynormalColoring
        try:
            results = []
            time_opt = 0
            time_nonopt = 0
            for j in tqdm(range(100)):
                start = time.time()
                results.append(calcPolynormalColoringOptimized(graph))
                time_opt += time.time() - start

                start = time.time()
                results.append(calcPolynormalColoring(graph))
                time_nonopt += time.time() - start

            # check if all results are the same
            if len(set(results)) == 1:
                print(
                    "OK time_opt={} time_nonopt={}".format(
                        time_opt, time_nonopt))

            else:
                print("NG")
                print(results)
                print(graph)
                break

        except Exception as e:
            print(e)
            print(results)
            print(graph)
            break


if __name__ == "__main__":
    blackboxTest()
