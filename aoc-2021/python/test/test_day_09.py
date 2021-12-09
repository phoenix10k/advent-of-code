import os

from day_09 import calc_basins, parse_map, calc_lows


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_09.in") as input_file:
        map = parse_map(input_file)

    low_points = calc_lows(map)
    assert len(low_points) == 4
    assert sum(p.z + 1 for p in low_points) == 15

def test_part_2() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_09.in") as input_file:
        map = parse_map(input_file)

    lows = calc_lows(map)
    basins = calc_basins(lows, map)
    assert len(basins) == 4
    assert sorted(basins) == [3, 9, 9, 14]
