import os
from typing import List, TextIO
from dataclasses import dataclass
import numpy as np


@dataclass
class Point:
    x: int
    y: int

    @classmethod
    def from_str(cls, string: str) -> "Point":
        x, y = string.split(",")
        return cls(int(x), int(y))


@dataclass
class Line:
    start: Point
    end: Point

    @classmethod
    def from_str(cls, string: str) -> "Line":
        start, end = string.split(" -> ")
        return cls(Point.from_str(start), Point.from_str(end))


class Map:
    def __init__(self, extents: Point) -> None:
        self.array = np.zeros((extents.x, extents.y), dtype=int)

    def draw_straight(self, lines: List[Line]) -> None:
        for line in lines:
            if line.start.x == line.end.x:
                miny = min(line.start.y, line.end.y)
                maxy = max(line.start.y, line.end.y)
                for y in range(miny, maxy + 1):
                    self.array[line.start.x, y] += 1

            if line.start.y == line.end.y:
                minx = min(line.start.x, line.end.x)
                maxx = max(line.start.x, line.end.x)
                for x in range(minx, maxx + 1):
                    self.array[x, line.start.y] += 1

    def print(self) -> None:
        for row in self.array:
            print("".join(str(cell) for cell in row))

    @property
    def danger(self) -> int:
        return len(self.array[np.greater(self.array, 1)])


def parse_input(input: TextIO) -> List[Line]:
    return [Line.from_str(line) for line in input]


def get_extents(lines: List[Line]) -> Point:
    max = Point(0, 0)
    for line in lines:
        if line.start.x > max.x:
            max.x = line.start.x
        if line.end.x > max.x:
            max.x = line.end.x
        if line.start.y > max.y:
            max.y = line.start.y
        if line.end.y > max.y:
            max.y = line.end.y
    return Point(max.x + 1, max.y + 1)


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_05.in") as input_file:
        lines = parse_input(input_file)

    extents = get_extents(lines)
    map = Map(extents)
    map.draw_straight(lines)
    map.print()
    print("danger:", map.danger)
