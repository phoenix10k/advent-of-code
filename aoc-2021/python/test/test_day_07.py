import os

from day_07 import calc_fuel, calc_fuel_2


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_07.in") as input_file:
        positions = [int(f) for f in next(input_file).split(",")]

    assert calc_fuel(positions, 2) == 37
    assert calc_fuel(positions, 1) == 41
    assert calc_fuel(positions, 3) == 39


def test_part_2() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_07.in") as input_file:
        positions = [int(f) for f in next(input_file).split(",")]

    assert calc_fuel_2(positions, 5) == 168
    assert calc_fuel_2(positions, 2) == 206
