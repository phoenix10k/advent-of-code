import os
from typing import Dict, List, Set, Tuple


true_digit_segments: Dict[int, Set[str]] = {
    0: {"a", "b", "c", "e", "f", "g"},
    1: {"c", "f"},
    2: {"a", "c", "d", "e", "g"},
    3: {"a", "c", "d", "f", "g"},
    4: {"b", "c", "d", "f"},
    5: {"a", "b", "d", "f", "g"},
    6: {"a", "b", "d", "e", "f", "g"},
    7: {"a", "c", "f"},
    8: {"a", "b", "c", "d", "e", "f", "g"},
    9: {"a", "b", "c", "d", "f", "g"},
}
true_digits: Dict[str, int] = {
    "".join(sorted(v)): k for k, v in true_digit_segments.items()
}


def parse_line(line: str) -> Tuple[List[Set[str]], List[Set[str]]]:
    lhs, rhs = line.split(" | ")
    return [set(c) for c in lhs.split()], [set(d) for d in rhs.split()]


def calc_part_1(inputs: List[Tuple[List[Set[str]], List[Set[str]]]]) -> int:
    return sum(1 for _, nums in inputs for num in nums if len(num) in (2, 3, 4, 7))


def calc_display(combs: List[Set[str]], digits: List[Set[str]]) -> int:
    decode_map: Dict[str, int] = {}
    five_segs: List[Set[str]] = []  # 2, 3, 5
    six_segs: List[Set[str]] = []  # 0, 6, 9

    # Phase 1, unique length digits
    for comb in combs:
        if len(comb) == 2:
            one = comb
            decode_map["".join(sorted(comb))] = 1
        if len(comb) == 3:
            seven = comb
            decode_map["".join(sorted(comb))] = 7
        if len(comb) == 4:
            four = comb
            decode_map["".join(sorted(comb))] = 4
        if len(comb) == 5:
            five_segs.append(comb)
        if len(comb) == 6:
            six_segs.append(comb)
        if len(comb) == 7:
            eight = comb
            decode_map["".join(sorted(comb))] = 8
    assert len(five_segs) == 3
    assert len(six_segs) == 3

    # Phase 2, build segment map
    cf = one
    acf = seven
    bcdf = four
    abcdefg = eight
    adg = five_segs[0].intersection(five_segs[1]).intersection(five_segs[2])
    abfg = six_segs[0].intersection(six_segs[1]).intersection(six_segs[2])
    a = acf - cf
    assert len(a) == 1
    dg = adg - a
    bd = bcdf - cf
    b = bd - dg
    assert len(b) == 1
    d = bd - b
    assert len(d) == 1
    g = dg - d
    assert len(g) == 1
    bf = abfg - adg
    f = bf - b
    assert len(f) == 1
    c = cf - f
    assert len(c) == 1
    cde = abcdefg - abfg
    de = cde - c
    e = de - d
    assert len(e) == 1

    # Phase 3, complete decode_map
    decode_map["".join(sorted(a.union(c).union(d).union(e).union(g)))] = 2
    decode_map["".join(sorted(a.union(c).union(d).union(f).union(g)))] = 3
    decode_map["".join(sorted(a.union(b).union(d).union(f).union(g)))] = 5
    decode_map["".join(sorted(a.union(b).union(c).union(e).union(f).union(g)))] = 0
    decode_map["".join(sorted(a.union(b).union(d).union(e).union(f).union(g)))] = 6
    decode_map["".join(sorted(a.union(b).union(c).union(d).union(f).union(g)))] = 9

    ans = 0
    for d in digits:
        ans += decode_map["".join(sorted(d))]
        ans *= 10
    ans //= 10
    return ans


def calc_part_2(inputs: List[Tuple[List[Set[str]], List[Set[str]]]]) -> int:
    total = 0
    for combs, digits in inputs:
        total += calc_display(combs, digits)
    return total


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_08.in") as input_file:
        inputs = [parse_line(line) for line in input_file]

    print("part 1:", calc_part_1(inputs))
    print("part 2:", calc_part_2(inputs))
