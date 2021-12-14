import os
from collections import defaultdict

from day_14 import pair_insertion, parse_input


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_14.in") as input_file:
        polymer, rules = parse_input(input_file)

    assert polymer == "NNCB"
    polymer = pair_insertion(polymer, rules)
    assert polymer == "NCNBCHB"
    polymer = pair_insertion(polymer, rules)
    assert polymer == "NBCCNBBBCBHCB"
    polymer = pair_insertion(polymer, rules)
    assert polymer == "NBBBCNCCNBBNBNBBCHBHHBCHB"
    polymer = pair_insertion(polymer, rules)
    assert polymer == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    polymer = pair_insertion(polymer, rules)
    assert len(polymer) == 97
    for _ in range(5):
        polymer = pair_insertion(polymer, rules)
    assert len(polymer) == 3073

    counts: defaultdict[str, int] = defaultdict(int)
    for c in polymer:
        counts[c] += 1

    assert counts["B"] == 1749
    assert counts["C"] == 298
    assert counts["H"] == 161
    assert counts["N"] == 865
