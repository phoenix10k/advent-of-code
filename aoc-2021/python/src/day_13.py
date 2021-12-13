import os
from dataclasses import dataclass
from enum import Enum, auto
from typing import TextIO
from parse import parse


class Direction(Enum):
    Vertical = "x"
    Horizontal = "y"


@dataclass
class Fold:
    direction: Direction
    position: int


def build_grid(
    positions: set[tuple[int, int]], maxx: int, maxy: int
) -> list[list[bool]]:
    return [
        [(x, y) in positions for x in range(0, maxx + 1)] for y in range(0, maxy + 1)
    ]


def parse_input(input_file: TextIO) -> tuple[list[list[bool]], list[Fold]]:
    positions: set[tuple[int, int]] = set()
    folds: list[Fold] = []
    maxx = 0
    maxy = 0
    parsing_folds = False
    for line in input_file:
        line = line.strip()
        if parsing_folds:
            parsed = parse("fold along {direction}={position:d}", line)
            folds.append(
                Fold(direction=Direction(parsed["direction"]), position=parsed["position"])
            )
        elif line:
            coords = parse("{x:d},{y:d}", line)
            x = coords["x"]
            y = coords["y"]
            positions.add((x, y))
            maxx = max(x, maxx)
            maxy = max(y, maxy)
        else:
            parsing_folds = True

    return build_grid(positions, maxx, maxy), folds


def process_fold(grid: list[list[bool]], fold: Fold) -> list[list[bool]]:
    match fold.direction:
      case Direction.Vertical:
        new_grid: list[list[bool]] = []
        for line in grid:
          assert fold.position >= len(line) // 2
          new_line = line[:fold.position]
          for x in range(fold.position + 1, len(line)):
              new_line[2* fold.position - x] |= line[x]
          new_grid.append(new_line)
        return new_grid
      case Direction.Horizontal:
        assert fold.position >= len(grid) // 2
        new_grid: list[list[bool]] = grid[:fold.position]
        for y in range(fold.position + 1, len(grid)):
          for x in range(len(grid[0])):
            grid[2* fold.position - y][x] |= grid[y][x]
        return new_grid
      case _:
        raise RuntimeError(f"Unknown direction: {fold.direction}")

def print_grid(grid: list[list[bool]]) -> None:
    for line in grid:
        print("".join("#" if c else " " for c in line))


def count_grid(grid: list[list[bool]]) -> int:
    return sum(line.count(True) for line in grid)


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_13.in") as input_file:
        grid, folds = parse_input(input_file)

    grid = process_fold(grid, folds[0])
    print("part 1:", count_grid(grid))
