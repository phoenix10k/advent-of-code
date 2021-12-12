import os

from day_11 import parse_input, print_state, run_sim


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_11.in") as input_file:
        state = parse_input(input_file)
    print_state(state)
    flashes = 0
    for step in range(10):
        state, new_flashes = run_sim(state)
        flashes += new_flashes
        print("step:", step + 1)
        print_state(state)
    assert flashes == 204

    for _ in range(90):
        state, new_flashes = run_sim(state)
        flashes += new_flashes
    assert flashes == 1656


def test_part_2() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_11.in") as input_file:
        state = parse_input(input_file)
