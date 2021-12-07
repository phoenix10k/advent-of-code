import os

from day_05 import Map, get_extents, parse_input


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_05.in") as input_file:
        lines = parse_input(input_file)

    extents = get_extents(lines)
    map = Map(extents)
    map.draw_straight(lines)
    assert map.danger == 5


def test_part_2() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_05.in") as input_file:
        lines = parse_input(input_file)
