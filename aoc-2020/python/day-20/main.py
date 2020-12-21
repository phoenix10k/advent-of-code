import functools
import operator

class Tile:
    def __init__(self):
        self.id = ''
        self.data = []
        self.edges = []

    def __repr__(self):
        repr = str(self.id) + '\n'
        for row in self.data:
            repr += row + '\n'
        repr += 'edges:\n'
        for edge in self.edges:
            repr += edge + '\n'
        return repr + '\n'

    def read(self, stream):
        self.id = int(next(stream)[5:-2])
        for line in stream:
            if line.strip():
                self.data.append(line.strip())
            else:
                break

        self.edges.append(self.data[0])
        self.edges.append(self.data[-1])
        self.edges.append(''.join(r[0] for r in self.data))
        self.edges.append(''.join(r[-1] for r in self.data))


tiles = []
with open('input.txt') as file:
    try:
        while True:
            tile = Tile()
            tile.read(file)
            tiles.append(tile)
    except StopIteration:
        pass

print(tiles)

corners = []
for tile in tiles:
    matches = 0
    for edge in tile.edges:
        redge = edge[::-1]
        if any(edge in othert.edges or redge in othert.edges for othert in tiles if othert != tile):
            matches += 1
    if matches < 3:
        corners.append(tile)

print(corners)
print(functools.reduce(operator.mul, [t.id for t in corners], 1))
