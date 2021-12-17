from day_17 import Box, State, count_successes, optimise_height


def test_part_1() -> None:
    assert optimise_height(Box(20, 30, -10, -5)) == (State(6, 9), 45)


def test_part_2() -> None:
    assert count_successes(Box(20, 30, -10, -5)) == (112)
