import functools
import operator
from typing import List

map: List[List[int]] = []

with open('input.txt') as file:
    for y, line in enumerate(file):
        map_line: List[int] = []
        for x, char in enumerate(line):
            if char == '.':
                map_line.append(0)
            if char == '#':
                map_line.append(1)
        map.append(map_line)
for line in map:
    for item in line:
        print(item, end='')
    print()

nums = []
for vel_x, vel_y in [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]:
    pos_x = 0
    pos_y = 0
    count = 0
    while pos_y < len(map):
        count += map[pos_y][pos_x % len(map[pos_y])]
        pos_x += vel_x
        pos_y += vel_y

    print(count)
    nums.append(count)

print(functools.reduce(operator.mul, nums, 1))
