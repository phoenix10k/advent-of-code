import os

import numpy as np
from day_06 import run_sim


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_06.in") as input_file:
        fish = np.array([int(f) for f in next(input_file).split(",")])

    for i in range(80):
        fish = run_sim(fish)
        print(f"day {i}: {fish}")

    assert len(fish) == 5934

    for i in range(256 - 80):
        fish = run_sim(fish)
        print(f"day {i}: {fish}")

    assert len(fish) == 26984457539
