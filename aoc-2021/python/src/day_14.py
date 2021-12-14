import os
from collections import defaultdict
from itertools import count, pairwise
from typing import TextIO


def parse_input(input_file: TextIO) -> tuple[dict[str, int], dict[str, str]]:
    polymer = next(input_file).strip()
    next(input_file)  # skip blank line
    rules: dict[str, str] = {}
    for line in input_file:
        k, v = line.strip().split(" -> ")
        rules[k] = v
    polymer_counts: defaultdict[str, int] = defaultdict(int)
    for element in polymer:
        polymer_counts[element] += 1
    for pair in pairwise(polymer):
        polymer_counts["".join(pair)] += 1

    return polymer_counts, rules


def pair_insertion(polymer: dict[str, int], rules: dict[str, str]) -> dict[str, int]:
    polymer_counts: defaultdict[str, int] = defaultdict(int)
    polymer_counts.update(count_elements(polymer))
    for k, v in polymer.items():
        if len(k) == 2:
            polymer_counts[k[0] + rules[k]] += v
            polymer_counts[rules[k] + k[1]] += v
            polymer_counts[rules[k]] += v
    return polymer_counts


def count_elements(polymer: dict[str, int]) -> dict[str, int]:
    return {k: v for k, v in polymer.items() if len(k) == 1}


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_14.in") as input_file:
        polymer, rules = parse_input(input_file)

    for _ in range(10):
        polymer = pair_insertion(polymer, rules)

    counts = count_elements(polymer)

    print("part 1:", max(counts.values()) - min(counts.values()))

    for _ in range(30):
        polymer = pair_insertion(polymer, rules)

    counts = count_elements(polymer)
    print("part 2:", max(counts.values()) - min(counts.values()))
