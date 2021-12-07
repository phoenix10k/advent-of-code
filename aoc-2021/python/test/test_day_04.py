import os

from day_04 import get_losing_score, get_winning_score, parse_input


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_04.in") as input_file:
        draw, boards = parse_input(input_file)

    assert draw == [
        7,
        4,
        9,
        5,
        11,
        17,
        23,
        2,
        0,
        14,
        21,
        24,
        10,
        16,
        13,
        6,
        15,
        25,
        12,
        22,
        18,
        20,
        8,
        19,
        3,
        26,
        1,
    ]
    assert len(boards) == 3

    assert get_winning_score(draw, boards) == 4512


def test_part_2() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_04.in") as input_file:
        draw, boards = parse_input(input_file)

    assert get_losing_score(draw, boards) == 1924
