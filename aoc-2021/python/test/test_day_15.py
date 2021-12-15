import os

import networkx as nx
from day_15 import least_risk_path, parse_input


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_15.in") as input_file:
        graph, size = parse_input(input_file)

    assert least_risk_path(graph, size) == 40
