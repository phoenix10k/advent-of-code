import os
from typing import List, Tuple


def parse_line(line: str) -> Tuple[List[str], List[str]]:
    lhs, rhs = line.split(" | ")
    return lhs.split(), rhs.split()


def calc_part_1(inputs: Tuple[List[str], List[str]]) -> int:
    return sum(1 for _, nums in inputs for num in nums if len(num) in (2, 3, 4, 7))


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_08.in") as input_file:
        inputs = [parse_line(line) for line in input_file]

    print("part 1:", calc_part_1(inputs))
