import os
from itertools import pairwise
from typing import TextIO

import networkx as nx


def parse_input(input_file: TextIO) -> list[list[int]]:
    return [[int(r) for r in line.strip()] for line in input_file]


def build_graph(input_data: list[list[int]]) -> nx.Graph:
    size = len(input_data)
    graph = nx.DiGraph()
    for i, line in enumerate(input_data):
        for j, risk in enumerate(line):
            graph.add_node((i, j), risk=risk)

    for i1, i2 in pairwise(range(size)):
        for j in range(size):
            graph.add_edge((i1, j), (i2, j), risk=graph.nodes[i2, j]["risk"])
            graph.add_edge((i2, j), (i1, j), risk=graph.nodes[i1, j]["risk"])

    for i in range(size):
        for j1, j2 in pairwise(range(size)):
            graph.add_edge((i, j1), (i, j2), risk=graph.nodes[i, j2]["risk"])
            graph.add_edge((i, j2), (i, j1), risk=graph.nodes[i, j1]["risk"])

    return graph, size


def least_risk_path(graph: nx.Graph, size: int) -> int:
    return int(
        nx.shortest_path_length(graph, (0, 0), (size - 1, size - 1), weight="risk")
    )


def inc_risk(risk: int, inc: int) -> int:
    return 1 + ((risk - 1 + inc) % 9)


def grow_map(input_data: list[list[int]]) -> list[list[int]]:
    size = len(input_data)
    return [
        [inc_risk(r, i // size + j // size) for j, r in enumerate(row * 5)]
        for i, row in enumerate(input_data * 5)
    ]


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_15.in") as input_file:
        input_data = parse_input(input_file)

    graph, size = build_graph(input_data)
    print("part 1:", least_risk_path(graph, size))

    bigger_data = grow_map(input_data)
    graph, size = build_graph(bigger_data)
    print("part 2:", least_risk_path(graph, size))
