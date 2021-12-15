import os

import networkx as nx
from day_15 import build_graph, grow_map, least_risk_path, parse_input


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_15.in") as input_file:
        graph, size = build_graph(parse_input(input_file))

    assert least_risk_path(graph, size) == 40


def test_part_2() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_15.in") as input_file:
        input_data = parse_input(input_file)

    bigger_data = grow_map(input_data)
    graph, size = build_graph(bigger_data)

    assert least_risk_path(graph, size) == 315
