import os

from day_10 import calc_se_score


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_10.in") as input_file:
        assert calc_se_score(input_file) == 26397
