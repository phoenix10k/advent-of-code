import sys

with open('input.txt') as file:
    start = int(next(file).strip())
    buses = [int(x) for x in next(file).strip().split(',') if x != 'x']

print('start', start)
print('buses', buses)

minb = None
mintime = None
for b in buses:
    time = b * ((start // b) + 1)
    print('b:', b, 'time:', time)
    if not mintime or time < mintime:
        minb = b
        mintime = time

print('ans:', minb * (mintime - start))

