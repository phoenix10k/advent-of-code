import os

from day_06 import run_sim


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_06.in") as input_file:
        fish_list = [int(f) for f in next(input_file).split(",")]
    fish = {k: 0 for k in range(9)}
    for f in fish_list:
        fish[f] += 1

    for i in range(80):
        fish = run_sim(fish)
        print(f"day {i}: {fish}")

    assert sum(fish.values()) == 5934

    for i in range(256 - 80):
        fish = run_sim(fish)
        print(f"day {i}: {fish}")

    assert sum(fish.values()) == 26984457539
