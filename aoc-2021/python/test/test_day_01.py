import os

from day_01 import count_increases, calc_part_2


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_01.in") as input_file:
        input = [int(l) for l in input_file]
    assert count_increases(input) == 7


def test_part_2() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_01.in") as input_file:
        input = [int(l) for l in input_file]
    assert calc_part_2(input) == 5
