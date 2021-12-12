import os
from typing import Any, TextIO

import numpy as np
import numpy.typing as npt


def parse_input(input_file: TextIO) -> npt.NDArray[np.int_]:
    return np.array([[int(c) for c in line.strip()] for line in input_file])


def run_sim(state: npt.NDArray[np.int_]) -> tuple[npt.NDArray[np.int_], int]:
    maxdim = len(state)
    state += 1
    old_flashes: set[tuple[Any, ...]] = set()
    while True:
        flashes = {tuple(i) for i in np.transpose(np.nonzero(state > 9))}
        new_flashes = flashes - old_flashes
        old_flashes = flashes
        if not new_flashes:
            break
        print("new_iter")
        for f in new_flashes:
            print("flash at:", f)
            for j in range(-1, 2):
                for i in range(-1, 2):
                    y = f[0] + j
                    x = f[1] + i
                    if x >= 0 and x < maxdim and y >= 0 and y < maxdim:
                        state[y][x] += 1
    if flashes:
        iy, ix = zip(*list(flashes))
        state[np.array(iy), np.array(ix)] = 0
    return state, len(flashes)


def print_state(state: npt.NDArray[np.int_]) -> None:
    for line in state:
        print(line)


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_11.in") as input_file:
        state = parse_input(input_file)
    flashes = 0
    for step in range(100):
        state, new_flashes = run_sim(state)
        flashes += new_flashes
    print("part 1:", flashes)
    step += 1
    while True:
        state, flashes = run_sim(state)
        step += 1
        if flashes == 100:
            break
    print("part 2:", step)
