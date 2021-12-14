import os

from day_14 import count_elements, pair_insertion, parse_input


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_14.in") as input_file:
        polymer, rules = parse_input(input_file)

    for _ in range(10):
        polymer = pair_insertion(polymer, rules)

    counts = count_elements(polymer)

    assert counts["B"] == 1749
    assert counts["C"] == 298
    assert counts["H"] == 161
    assert counts["N"] == 865


def test_part_2() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_14.in") as input_file:
        polymer, rules = parse_input(input_file)

    for _ in range(40):
        polymer = pair_insertion(polymer, rules)

    counts = count_elements(polymer)

    assert counts["B"] == 2192039569602
    assert counts["H"] == 3849876073
