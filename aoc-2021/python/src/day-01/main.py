import os
from itertools import pairwise, tee
from typing import Iterable, Tuple

def calc_increases(input: Iterable[int]) -> int:
  return sum(1 for l, r in pairwise(input) if r > l)

def calc_windows(input: Iterable[int]) -> Iterable[Tuple[int, int, int]]:
    a, b, c = tee(input, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)

if __name__ == '__main__':
  os.chdir(os.path.dirname(__file__))
  
  with open('input.txt') as input_file:
    input = [int(l) for l in input_file]

  print(calc_increases(input))
  print(calc_increases(sum(w) for w in calc_windows(input)))
