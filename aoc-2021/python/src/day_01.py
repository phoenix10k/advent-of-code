import os
from itertools import pairwise, tee
from typing import Iterable, Tuple


def count_increases(input: Iterable[int]) -> int:
    return sum(1 for l, r in pairwise(input) if r > l)


def get_windows(input: Iterable[int]) -> Iterable[Tuple[int, int, int]]:
    a, b, c = tee(input, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)


def calc_part_2(input: Iterable[int]) -> int:
    return count_increases(sum(w) for w in get_windows(input))


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    with open("../data/day_01.in") as input_file:
        input = [int(l) for l in input_file]

    print("part 1:", count_increases(input))
    print("part 2:", calc_part_2(input))
