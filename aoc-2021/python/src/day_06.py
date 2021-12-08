import os
from typing import Dict


def run_sim(fish: Dict[int, int]) -> Dict[int, int]:
    new_fish = {}
    for i in range(9):
        new_fish[i] = fish.get(i + 1, 0)
    new_fish[6] += fish.get(0, 0)
    new_fish[8] = fish.get(0, 0)
    return new_fish


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_06.in") as input_file:
        fish_list = [int(f) for f in next(input_file).split(",")]
    fish = {k: 0 for k in range(9)}
    for f in fish_list:
        fish[f] += 1

    for i in range(256):
        fish = run_sim(fish)
        print(f"day {i}: ({sum(fish.values())}) {fish}")
