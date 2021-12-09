import functools
import operator
import os
from dataclasses import dataclass
from typing import List, TextIO


@dataclass
class Point:
    x: int
    y: int
    z: int


def parse_map(file: TextIO) -> List[List[Point]]:
    return [
        [Point(x, y, int(z)) for x, z in enumerate(line.strip())]
        for y, line in enumerate(file)
    ]


def calc_lows(map: List[List[Point]]) -> List[Point]:
    lows = []
    maxx = len(map[0]) - 1
    maxy = len(map) - 1
    for line in map:
        for p in line:
            if p.x > 0 and map[p.y][p.x - 1].z <= p.z:
                continue
            if p.x < maxx and map[p.y][p.x + 1].z <= p.z:
                continue
            if p.y > 0 and map[p.y - 1][p.x].z <= p.z:
                continue
            if p.y < maxy and map[p.y + 1][p.x].z <= p.z:
                continue
            lows.append(p)
    return lows


def calc_basins(lows: List[Point], map: List[List[Point]]) -> List[int]:
    """Returns a list of basin sizes corresponding to the `lows` list."""
    basins = [0] * len(lows)
    maxx = len(map[0]) - 1
    maxy = len(map) - 1
    for line in map:
        for p in line:
            if p.z == 9:
                continue
            while p not in lows:
                if p.x > 0 and map[p.y][p.x - 1].z < p.z:
                    p = Point(p.x - 1, p.y, map[p.y][p.x - 1].z)
                if p.x < maxx and map[p.y][p.x + 1].z < p.z:
                    p = Point(p.x + 1, p.y, map[p.y][p.x + 1].z)
                if p.y > 0 and map[p.y - 1][p.x].z < p.z:
                    p = Point(p.x, p.y - 1, map[p.y - 1][p.x].z)
                if p.y < maxy and map[p.y + 1][p.x].z < p.z:
                    p = Point(p.x, p.y + 1, map[p.y + 1][p.x].z)

            ix = lows.index(p)
            basins[ix] += 1
    return basins


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_09.in") as input_file:
        map = parse_map(input_file)

    lows = calc_lows(map)
    print("part 1:", sum(p.z + 1 for p in lows))

    basins = calc_basins(lows, map)
    print("part 2:", functools.reduce(operator.mul, sorted(basins)[-3:], 1))
