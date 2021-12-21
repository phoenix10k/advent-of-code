import os

from day_20 import count_pixels, enhance, parse_input


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_20.in") as input_file:
        image, program = parse_input(input_file)

    image = enhance(image, program)
    image = enhance(image, program)

    assert count_pixels(image) == 35


def test_part_2() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_20.in") as input_file:
        image, program = parse_input(input_file)

    for _ in range(50):
        image = enhance(image, program)

    assert count_pixels(image) == 3351
