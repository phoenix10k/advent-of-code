import os

from day_08 import parse_line, calc_part_1


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_08.in") as input_file:
        inputs = [parse_line(line) for line in input_file]

    assert calc_part_1(inputs) == 26
