state = [[]]
len_x = 0
len_y = 0
len_z = 1
orig_x = 0
orig_y = 0
orig_z = 0
z = 0

with open('input.txt') as file:
    for y, line in enumerate(file):
        len_y += 1
        len_x = len(line.strip())
        state[z].append(line.strip())

def print_state():
    for z, plane in enumerate(state):
        print('z=', z - orig_z)
        for row in plane:
            print(row)


def count_neighbours(x, y, z):
    count = 0
    orig_state = '.'
    for test_z in range(z - 1, z + 2):
        for test_y in range(y - 1, y + 2):
            for test_x in range(x - 1, x + 2):
                if 0 <= test_x < len_x and 0 <= test_y < len_y and 0 <= test_z < len_z:
                    if test_x == x and test_y == y and test_z == z:
                        orig_state = state[test_z][test_y][test_x]
                    elif state[test_z][test_y][test_x] == '#':
                        count += 1
    return count, orig_state


def iter_state():
    global len_x, len_y, len_z, orig_x, orig_y, orig_z, state
    new_state = []
    for z in range(len_z + 2):
        new_state.append([])
        for y in range(len_y + 2):
            new_state[z].append('')
            for x in range(len_x + 2):
                count, old_state = count_neighbours(x - 1, y - 1, z - 1)
                if old_state == '.' and count == 3:
                    new_state[z][y] += '#'
                elif old_state == '#' and count not in (2, 3):
                    new_state[z][y] += '.'
                else:
                    new_state[z][y] += old_state
    state = new_state

    orig_x += 1
    orig_y += 1
    orig_z += 1
    len_x += 2
    len_y += 2
    len_z += 2


print('iter:', 0)
print_state()

for i in range(1, 7):
    print('iter:', i)
    iter_state()
    print_state()

count = 0
for plane in state:
    for row in plane:
        count += row.count('#')

print('count:', count)
