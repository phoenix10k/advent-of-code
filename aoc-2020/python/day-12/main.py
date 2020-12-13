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
wayx = 10
wayy = 1
for inst, dist in instructions:
    if inst == 'F':
        posx += wayx * dist
        posy += wayy * dist
    elif inst =='N':
        wayy += dist
    elif inst == 'S':
        wayy -= dist
    elif inst == 'E':
        wayx += dist
    elif inst == 'W':
        wayx -= dist
    elif inst == 'L':
        for i in range(dist//90):
            tmp = wayx
            wayx = -wayy
            wayy = tmp
    elif inst == 'R':
        for i in range(dist//90):
            tmp = wayx
            wayx = wayy
            wayy = -tmp
    else:
        raise RuntimeError(f"Bad inst {inst}")

print(abs(posx) + abs(posy))