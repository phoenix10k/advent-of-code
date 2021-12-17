from day_17 import optimise_height, Box, State


def test_part_1() -> None:
    assert optimise_height(Box(20, 30, -10, -5)) == (State(6, 9), 45)
