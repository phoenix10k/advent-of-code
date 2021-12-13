import os

from day_13 import count_grid, parse_input, print_grid, process_fold


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_13.in") as input_file:
        grid, folds = parse_input(input_file)

    print_grid(grid)
    grid = process_fold(grid, folds[0])
    print_grid(grid)
    assert count_grid(grid) == 17
