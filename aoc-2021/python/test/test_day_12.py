import os

from day_12 import parse_input, count_paths, count_paths_2


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_12_1.in") as input_file:
        caves = parse_input(input_file)
    assert count_paths(caves) == 10
    with open("data/test_day_12_2.in") as input_file:
        caves = parse_input(input_file)
    assert count_paths(caves) == 19
    with open("data/test_day_12_3.in") as input_file:
        caves = parse_input(input_file)
    assert count_paths(caves) == 226


def test_part_2() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_12_1.in") as input_file:
        caves = parse_input(input_file)
    assert count_paths_2(caves) == 36
    with open("data/test_day_12_2.in") as input_file:
        caves = parse_input(input_file)
    assert count_paths_2(caves) == 103
    with open("data/test_day_12_3.in") as input_file:
        caves = parse_input(input_file)
    assert count_paths_2(caves) == 3509
