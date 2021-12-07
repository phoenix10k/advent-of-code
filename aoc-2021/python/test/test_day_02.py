import os

from day_02 import process_directions, process_directions_part_2


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_02.in") as input_file:
        pos, depth = process_directions(input_file)
        assert pos == 15
        assert depth == 10
        assert pos * depth == 150


def test_part_2() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_02.in") as input_file:
        pos, depth = process_directions_part_2(input_file)
        assert pos == 15
        assert depth == 60
        assert pos * depth == 900
