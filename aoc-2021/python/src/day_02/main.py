import os
from typing import Iterable, Tuple

def process_directions(directions: Iterable[str]) -> Tuple[int, int]:
  pos = 0
  depth = 0
  for dir in directions:
    match dir.split():
      case ["forward", dist]:
        pos += int(dist)
      case ["up", dist]:
        depth -= int(dist)
      case ["down", dist]:
        depth += int(dist)
      case _:
        raise RuntimeError(f"Invalid direction: {dir}")
  return pos, depth
      
      
def process_directions_part_2(directions: Iterable[str]) -> Tuple[int, int]:
  pos = 0
  aim = 0
  depth = 0
  for dir in directions:
    match dir.split():
      case ["forward", dist]:
        pos += int(dist)
        depth += aim * int(dist)
      case ["up", dist]:
        aim -= int(dist)
      case ["down", dist]:
        aim += int(dist)
      case _:
        raise RuntimeError(f"Invalid direction: {dir}")
  return pos, depth
      
if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("input.txt") as input_file:
      pos, depth = process_directions_part_2(input_file)
      print(f"Pos: {pos}, Depth: {depth}")
      print(f"mult: {pos*depth}")