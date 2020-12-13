instructions=[]

with open('input.txt') as file:
    for line in file:
        inst = line[0]
        dist = int(line[1:].strip())
        if inst in ('L', 'R') and dist % 90:
            raise RuntimeError("not right angle")
        instructions.append((inst, dist))

dir = 0  # 0=E, 1=S. 2=W, 3=N
dirs = 'ESWN'
posx = 0
posy = 0
for inst, dist in instructions:
    if inst == 'F':
        inst = dirs[dir]

    if inst =='N':
        posy += dist
    elif inst == 'S':
        posy -= dist
    elif inst == 'E':
        posx += dist
    elif inst == 'W':
        posx -= dist
    elif inst == 'L':
        dir -= dist//90
        dir = dir % 4
    elif inst == 'R':
        dir += dist//90
        dir = dir % 4
    else:
        raise RuntimeError(f"Bad inst {inst}")

print(abs(posx) + abs(posy))