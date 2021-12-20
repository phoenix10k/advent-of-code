import os

from day_19 import build_map, max_dist, parse_input


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_19.in") as input_file:
        scanners = parse_input(input_file)

    full_map = build_map(scanners)
    assert len(full_map) == 79


def test_part_2() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_19.in") as input_file:
        scanners = parse_input(input_file)

    build_map(scanners)
    assert max_dist(scanners) == 3621
