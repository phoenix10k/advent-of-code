import itertools
import functools
import operator
numbers = []
with open('input.txt') as file:
    for line in file:
        numbers.append(int(line))
combs = itertools.combinations(numbers, 3)
for comb in combs:
    if sum(comb) == 2020:
        print(functools.reduce(operator.mul, comb, 1))