import os

import numpy as np
import numpy.typing as npt


def run_sim(fish: npt.NDArray[np.int_]) -> npt.NDArray[np.int_]:
    next_fish: npt.NDArray[np.int_] = fish - 1
    births: npt.NDArray[np.bool_] = next_fish < 0
    next_fish = np.where(births, 6, next_fish)
    num_births = np.count_nonzero(births)
    new_fish = np.full(num_births, 8)
    return np.concatenate((next_fish, new_fish))  # type: ignore


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_06.in") as input_file:
        fish = np.array([int(f) for f in next(input_file).split(",")], dtype=int)

    for i in range(256):
        fish = run_sim(fish)
        print(f"day {i}: {len(fish)}")
