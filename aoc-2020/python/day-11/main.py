state = []


def print_state():
    count = 0
    for line in state:
        count+= line.count('#')
        #print(line)
    print('count:', count, '\n')


def iter_state():
    new_state = []
    changes = False
    for y in range(len(state)):
        new_state.append('')
        for x in range(len(state[y])):
            neighbours = 0

            for dir_x, dir_y in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1),
                                 (-1, -1), (-1, 0), (-1, 1)]:
                test_y = y
                test_x = x
                while True:
                    test_y += dir_y
                    test_x += dir_x
                    if 0 <= test_y < len(state) and 0 <= test_x < len(state[y]):
                        if state[test_y][test_x] == '#':
                            neighbours += 1
                            break
                        if state[test_y][test_x] == 'L':
                            break
                    else:
                        break

            if state[y][x] == 'L' and neighbours == 0:
                new_state[y] += '#'
                changes = True
            elif state[y][x] == '#' and neighbours >= 5:
                new_state[y] += 'L'
                changes = True
            else:
                new_state[y] += state[y][x]
    return new_state, changes


with open('input.txt') as file:
    for line in file:
        state.append(line.strip())

changes = True
while changes:
    print_state()
    state, changes = iter_state()

print_state
