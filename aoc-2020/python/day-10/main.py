import math
import functools

numbers = []

with open('input.txt') as file:
    for line in file:
        numbers.append(int(line))

numbers = [0] + sorted(numbers)
print(numbers)
deltas = {1: 0, 2: 0, 3: 1}
for i in range(0, len(numbers) - 1):
    deltas[numbers[i + 1] - numbers[i]] += 1

print(deltas)
print(deltas[1] * deltas[3])


@functools.lru_cache
def arrangements(idx):
    if len(numbers[idx:]) > 3 and numbers[idx + 3] - numbers[idx] <= 3:
        return arrangements(idx + 1) + arrangements(idx + 2) + arrangements(idx + 3)
    if len(numbers[idx:]) > 2 and numbers[idx + 2] - numbers[idx] <= 3:
        return arrangements(idx + 1) + arrangements(idx + 2)
    if len(numbers[idx:]) > 1 and numbers[idx + 1] - numbers[idx] <= 3:
        return arrangements(idx + 1)
    if len(numbers[idx:]) == 1:
        return 1
    raise RuntimeError("Bang")


print(arrangements(0))