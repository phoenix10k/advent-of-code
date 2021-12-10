import os

from day_10 import calc_se_score, calc_middle_complete_score


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_10.in") as input_file:
        assert calc_se_score(input_file) == 26397


def test_part_2() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_10.in") as input_file:
        assert calc_middle_complete_score(input_file) == 288957
