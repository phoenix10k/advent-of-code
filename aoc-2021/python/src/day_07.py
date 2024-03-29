import os
from typing import List, Optional


def tri(n: int) -> int:
    return n * (n + 1) // 2


def calc_fuel(positions: List[int], target: int) -> int:
    return sum(abs(p - target) for p in positions)


def calc_fuel_2(positions: List[int], target: int) -> int:
    return sum(tri(abs(p - target)) for p in positions)


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_07.in") as input_file:
        positions = [int(f) for f in next(input_file).split(",")]

    min_pos = min(positions)
    max_pos = max(positions)

    best_fuel: Optional[int] = None
    for p in range(min_pos, max_pos + 1):
        f = calc_fuel(positions, p)
        if best_fuel is None or f < best_fuel:
            best_fuel = f

    print("Best Fuel:", best_fuel)

    best_fuel = None
    for p in range(min_pos, max_pos + 1):
        f = calc_fuel_2(positions, p)
        if best_fuel is None or f < best_fuel:
            best_fuel = f
    print("Best Fuel 2:", best_fuel)
