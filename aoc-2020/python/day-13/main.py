import sys
import math

with open('input.txt') as file:
    start = int(next(file).strip())
    buses = [(int(x), idx) for idx, x in enumerate(next(file).strip().split(',')) if x != 'x']

print('start', start)
print('buses', buses)

# minb = None
# mintime = None
# for b in buses:
#     time = b * ((start // b) + 1)
#     print('b:', b, 'time:', time)
#     if not mintime or time < mintime:
#         minb = b
#         mintime = time

# print('ans:', minb * (mintime - start))

cnt = 1
skip = 1
for b, idx in buses:
    while (cnt + idx) % b:
        cnt += skip
    print('b:', b, 'cnt:', cnt)
    skip = (b * skip) // math.gcd(b, skip)