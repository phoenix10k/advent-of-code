import copy
import functools
import itertools
import operator
import os

import pytest
from day_18 import Number, parse_input


def test_reduce() -> None:
    num = Number.from_string("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")
    num.reduce()
    assert num == Number.from_string("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")


def test_magnitude() -> None:
    assert Number.from_string("[[1,2],[[3,4],5]]").magnitude == 143
    assert Number.from_string("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]").magnitude == 1384
    assert Number.from_string("[[[[1,1],[2,2]],[3,3]],[4,4]]").magnitude == 445
    assert Number.from_string("[[[[3,0],[5,3]],[4,4]],[5,5]]").magnitude == 791
    assert Number.from_string("[[[[5,0],[7,4]],[5,5]],[6,6]]").magnitude == 1137
    assert (
        Number.from_string(
            "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"
        ).magnitude
        == 3488
    )


def test_add_1() -> None:
    sum_result: Number = functools.reduce(
        operator.add,
        [
            Number.from_string("[1,1]"),
            Number.from_string("[2,2]"),
            Number.from_string("[3,3]"),
            Number.from_string("[4,4]"),
        ],
    )
    assert sum_result == Number.from_string("[[[[1,1],[2,2]],[3,3]],[4,4]]")


def test_add_2() -> None:
    sum_result: Number = functools.reduce(
        operator.add,
        [
            Number.from_string("[1,1]"),
            Number.from_string("[2,2]"),
            Number.from_string("[3,3]"),
            Number.from_string("[4,4]"),
            Number.from_string("[5,5]"),
        ],
    )
    assert sum_result == Number.from_string("[[[[3,0],[5,3]],[4,4]],[5,5]]")


def test_add_3() -> None:
    sum_result: Number = functools.reduce(
        operator.add,
        [
            Number.from_string("[1,1]"),
            Number.from_string("[2,2]"),
            Number.from_string("[3,3]"),
            Number.from_string("[4,4]"),
            Number.from_string("[5,5]"),
            Number.from_string("[6,6]"),
        ],
    )
    assert sum_result == Number.from_string("[[[[5,0],[7,4]],[5,5]],[6,6]]")


@pytest.mark.parametrize(
    ["lhs", "rhs", "res"],
    [
        (
            "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
            "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
            "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]",
        ),
    ],
)
def test_part_1_breakdown(lhs: str, rhs: str, res: str) -> None:
    add = Number.from_string(lhs) + Number.from_string(rhs)
    assert add == Number.from_string(res)


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_18.in") as input_file:
        number_list = parse_input(input_file)

    sum_result: Number = functools.reduce(operator.add, number_list)
    assert sum_result == Number.from_string(
        "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"
    )
    assert sum_result.magnitude == 4140


def test_part_2() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_18.in") as input_file:
        number_list = parse_input(input_file)

    maxmag = 0
    for lhs, rhs in itertools.permutations(number_list, 2):
        lhs = copy.deepcopy(lhs)
        rhs = copy.deepcopy(rhs)
        maxmag = max(maxmag, (lhs + rhs).magnitude)

    assert maxmag == 3993
