import os

from day_08 import parse_line, calc_part_1, calc_part_2


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_08.in") as input_file:
        inputs = [parse_line(line) for line in input_file]

    assert calc_part_1(inputs) == 26

def test_part_2() -> None:
    input = parse_line('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf')
    assert calc_part_2([input]) == 5353

    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_08.in") as input_file:
        inputs = [parse_line(line) for line in input_file]

    assert calc_part_2(inputs) == 61229

