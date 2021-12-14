import os
from collections import defaultdict
from itertools import pairwise
from typing import TextIO


def parse_input(input_file: TextIO) -> tuple[str, dict[str, str]]:
    polymer = next(input_file).strip()
    next(input_file)  # skip blank line
    rules: dict[str, str] = {}
    for line in input_file:
        k, v = line.strip().split(" -> ")
        rules[k] = v
    return polymer, rules


def pair_insertion(polymer: str, rules: dict[str, str]) -> str:
    output = polymer[0]
    for pair in pairwise(polymer):
        output += rules["".join(pair)] + pair[1]
    return output


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_14.in") as input_file:
        polymer, rules = parse_input(input_file)

    for _ in range(10):
        polymer = pair_insertion(polymer, rules)

    counts: defaultdict[str, int] = defaultdict(int)
    for c in polymer:
        counts[c] += 1

    print("part 1:", max(counts.values()) - min(counts.values()))
