import functools
import math
import operator
from dataclasses import dataclass
from enum import Enum, IntEnum, auto
from typing import Dict, List, TextIO, Tuple


class EdgeIndex(IntEnum):
    TOP = 0
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3


@dataclass
class EdgeMatch:
    edge_index: EdgeIndex
    other_tile: int
    other_edge_index: EdgeIndex
    flip: bool


@dataclass
class Tile:
    tile_id: int
    data: List[str]
    edges: List[str]
    edge_matches: List[EdgeMatch]

    def __init__(self) -> None:
        self.data = []
        self.edges = []
        self.edge_matches = []
        pass

    def read(self, stream: TextIO) -> None:
        self.tile_id = int(next(stream)[5:-2])
        for line in stream:
            if line.strip():
                self.data.append(line.strip())
            else:
                break

        self.edges.append(self.data[0])
        self.edges.append(''.join(r[-1] for r in self.data))
        self.edges.append(self.data[-1][::-1])
        self.edges.append(''.join(r[0] for r in self.data)[::-1])


class Transform(IntEnum):
    IDENTITY = 0  #  [[1 0] [0 1]]
    CCW_90 = 1  #  [[0 -1] [1 0]]
    CCW_180 = 2  #  [[-1 0] [0 -1]]
    CCW_270 = 3  #  [[0 1] [-1 0]]
    FLIP_X = 4  #  [[-1 0] [0 1]]
    FLIP_Y = 5  #  [[1 0] [0 -1]]
    FLIP_XY = 6  #  [[0 1] [1 0]]
    FLIP_NXY = 7  #  [[0 -1] [-1 0]]


@dataclass
class MapTile:
    tile: Tile
    transform: Transform


tiles: Dict[int, Tile] = {}
with open('input.txt') as file:
    try:
        while True:
            tile = Tile()
            tile.read(file)
            tiles[tile.tile_id] = tile
    except StopIteration:
        pass

print(tiles)

corners: List[Tile] = []
sides: List[Tile] = []
middles: List[Tile] = []
for tile in tiles.values():
    matches = 0
    for idx, edge in enumerate(tile.edges):
        redge = edge[::-1]
        for othert in tiles.values():
            if othert != tile:
                for otheridx, otheredge in enumerate(othert.edges):
                    if otheredge == edge:
                        matches += 1
                        tile.edge_matches.append(
                            EdgeMatch(EdgeIndex(idx), othert.tile_id,
                                      EdgeIndex(otheridx), False))
                    if otheredge == redge:
                        matches += 1
                        tile.edge_matches.append(
                            EdgeMatch(EdgeIndex(idx), othert.tile_id,
                                      EdgeIndex(otheridx), True))
    if matches == 2:
        corners.append(tile)
    elif matches == 3:
        sides.append(tile)
    elif matches == 4:
        middles.append(tile)

print('corners:', len(corners))
print('sides:', len(sides))
print('middles:', len(middles))

print('corner product:',
      functools.reduce(operator.mul, [t.tile_id for t in corners], 1))

map_tiles: List[List[MapTile]] = [[]]
image: List[str] = []
monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ',
]

t_per_side = int(math.sqrt(len(tiles)))

# solve top left corner
edge_matches = sorted(e.edge_index for e in corners[0].edge_matches)
if edge_matches == [1, 2]:
    rot = Transform.IDENTITY
elif edge_matches == [2, 3]:
    rot = Transform.CCW_90
elif edge_matches == [0, 3]:
    rot = Transform.CCW_180
elif edge_matches == [0, 1]:
    rot = Transform.CCW_270
else:
    raise RuntimeError('Huh?')
map_tiles[0].append(MapTile(corners[0], rot))


def inverse(transform: Transform) -> Transform:
    if transform == Transform.CCW_90:
        return Transform.CCW_270
    if transform == Transform.CCW_270:
        return Transform.CCW_90
    return transform


def rotate_edge(edge: EdgeIndex, transform: Transform) -> EdgeIndex:
    if transform == Transform.IDENTITY:
        return edge
    if transform in (Transform.CCW_90, Transform.CCW_180, Transform.CCW_270):
        return EdgeIndex((4 + edge - transform) % 4)
    if transform == Transform.FLIP_X:
        if edge == EdgeIndex.RIGHT:
            return EdgeIndex.LEFT
        if edge == EdgeIndex.LEFT:
            return EdgeIndex.RIGHT
        return edge
    if transform == Transform.FLIP_Y:
        if edge == EdgeIndex.TOP:
            return EdgeIndex.BOTTOM
        if edge == EdgeIndex.BOTTOM:
            return EdgeIndex.TOP
        return edge
    if transform == Transform.FLIP_XY:
        if edge == EdgeIndex.TOP:
            return EdgeIndex.RIGHT
        if edge == EdgeIndex.RIGHT:
            return EdgeIndex.TOP
        if edge == EdgeIndex.BOTTOM:
            return EdgeIndex.LEFT
        if edge == EdgeIndex.LEFT:
            return EdgeIndex.BOTTOM
    if transform == Transform.FLIP_NXY:
        if edge == EdgeIndex.TOP:
            return EdgeIndex.LEFT
        if edge == EdgeIndex.RIGHT:
            return EdgeIndex.BOTTOM
        if edge == EdgeIndex.BOTTOM:
            return EdgeIndex.RIGHT
        if edge == EdgeIndex.LEFT:
            return EdgeIndex.TOP

    raise RuntimeError(f"Bad transform: {transform}")


def calculate_transform(edge_match: EdgeMatch,
                        transform: Transform) -> Transform:
    orig_flip = transform in (Transform.FLIP_X, Transform.FLIP_Y,
                              Transform.FLIP_XY, Transform.FLIP_NXY)
    orig_edge = rotate_edge(edge_match.edge_index, transform)
    need_flip = orig_flip == edge_match.flip
    if orig_edge == EdgeIndex.RIGHT:
        if edge_match.other_edge_index == EdgeIndex.TOP:
            return Transform.FLIP_NXY if need_flip else Transform.CCW_90
        if edge_match.other_edge_index == EdgeIndex.RIGHT:
            return Transform.FLIP_X if need_flip else Transform.CCW_180
        if edge_match.other_edge_index == EdgeIndex.BOTTOM:
            return Transform.FLIP_XY if need_flip else Transform.CCW_270
        if edge_match.other_edge_index == EdgeIndex.LEFT:
            return Transform.FLIP_Y if need_flip else Transform.IDENTITY
    if orig_edge == EdgeIndex.BOTTOM:
        if edge_match.other_edge_index == EdgeIndex.TOP:
            return Transform.FLIP_X if need_flip else Transform.IDENTITY
        if edge_match.other_edge_index == EdgeIndex.RIGHT:
            return Transform.FLIP_XY if need_flip else Transform.CCW_90
        if edge_match.other_edge_index == EdgeIndex.BOTTOM:
            return Transform.FLIP_Y if need_flip else Transform.CCW_180
        if edge_match.other_edge_index == EdgeIndex.LEFT:
            return Transform.FLIP_NXY if need_flip else Transform.CCW_270
    raise RuntimeError(f"Bad orig edge {orig_edge}")


# solve top edge
for x in range(1, t_per_side):
    prev_tile = map_tiles[0][x - 1]
    edge_match = next(
        e for e in prev_tile.tile.edge_matches
        if rotate_edge(e.edge_index, prev_tile.transform) == EdgeIndex.RIGHT)
    map_tiles[0].append(
        MapTile(tiles[edge_match.other_tile],
                calculate_transform(edge_match, prev_tile.transform)))

# solve each row
for y in range(1, t_per_side):
    map_tiles.append([])
    for x in range(t_per_side):
        prev_tile = map_tiles[y - 1][x]
        edge_match = next(e for e in prev_tile.tile.edge_matches
                          if rotate_edge(e.edge_index, prev_tile.transform) ==
                          EdgeIndex.BOTTOM)
        map_tiles[y].append(
            MapTile(tiles[edge_match.other_tile],
                    calculate_transform(edge_match, prev_tile.transform)))


def render_tile(tile: MapTile, y: int) -> None:
    if tile.transform == Transform.IDENTITY:
        for i in range(8):
            image[(y * 8) + i] += ''.join(tile.tile.data[i + 1][1:-1])
    if tile.transform == Transform.CCW_90:
        for i in range(8):
            image[(y * 8) + i] += ''.join(
                [r[8 - i] for r in tile.tile.data[1:-1]])
    if tile.transform == Transform.CCW_180:
        for i in range(8):
            image[(y * 8) + i] += ''.join(tile.tile.data[8 - i][-2:0:-1])
    if tile.transform == Transform.CCW_270:
        for i in range(8):
            image[(y * 8) + i] += ''.join(
                [r[i + 1] for r in tile.tile.data[-2:0:-1]])
    if tile.transform == Transform.FLIP_X:
        for i in range(8):
            image[(y * 8) + i] += ''.join(tile.tile.data[i + 1][-2:0:-1])
    if tile.transform == Transform.FLIP_Y:
        for i in range(8):
            image[(y * 8) + i] += ''.join(tile.tile.data[8 - i][1:-1])
    if tile.transform == Transform.FLIP_XY:
        for i in range(8):
            image[(y * 8) + i] += ''.join(
                [r[8 - i] for r in tile.tile.data[-2:0:-1]])
    if tile.transform == Transform.FLIP_NXY:
        for i in range(8):
            image[(y * 8) + i] += ''.join(
                [r[i + 1] for r in tile.tile.data[1:-1]])


for y in range(t_per_side):
    for _ in range(8):
        image.append('')
    for x in range(t_per_side):
        render_tile(map_tiles[y][x], y)

print('\nImage:')
for row in image:
    print(row)


def match(x: int, y: int, t: Transform) -> bool:
    for my, row in enumerate(monster):
        for mx, char in enumerate(row):
            if t == Transform.IDENTITY:
                image_char = image[y + my][x + mx]
            if t == Transform.CCW_90:
                image_char = image[x + mx][len(image) - (1 + y + my)]
            if t == Transform.CCW_180:
                image_char = image[len(image) - (1 + y + my)][len(image) -
                                                              (1 + x + mx)]
            if t == Transform.CCW_270:
                image_char = image[len(image) - (1 + x + mx)][y + my]
            if t == Transform.FLIP_X:
                image_char = image[y + my][len(image) - (1 + x + mx)]
            if t == Transform.FLIP_Y:
                image_char = image[len(image) - (1 + y + my)][x + mx]
            if t == Transform.FLIP_XY:
                image_char = image[x + mx][y + my]
            if t == Transform.FLIP_NXY:
                image_char = image[len(image) - (1 + x + mx)][len(image) -
                                                              (1 + y + my)]

            if char == '#' and image_char != '#':
                return False

    return True


all_hash = sum(line.count('#') for line in image)

for t in Transform:
    print('transform:', t)
    count = 0
    for y in range(len(image) - len(monster)):
        for x in range(len(image[0]) - len(monster[0])):
            if match(x, y, t):
                print('match at', x, y)
                count += 1

    print('count:', count)
    print('all_others:', all_hash - count * 15)

print(map_tiles[-1][0])