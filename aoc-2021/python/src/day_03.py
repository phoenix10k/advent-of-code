import operator
import os
from typing import Any, Callable, Iterable, List, Tuple


def parse_input(input: Iterable[str]) -> Tuple[int, List[int]]:
    num_bits = 0
    numbers = []
    for line in input:
        if num_bits:
            assert num_bits == len(line.strip())
        else:
            num_bits = len(line.strip())
        numbers.append(int(line, base=2))
    return num_bits, numbers


def count_ones(num_bits: int, numbers: List[int]) -> List[int]:
    ones = [0] * num_bits
    for n in numbers:
        for i in range(num_bits):
            if n & (1 << num_bits - (i + 1)):
                ones[i] += 1
    return ones


def calc_gamma(ones: List[int], num_count: int) -> Tuple[int, int]:
    gamma = 0
    epsilon = 0
    for o in ones:
        if o > num_count / 2:
            gamma += 1
        else:
            epsilon += 1
        gamma <<= 1
        epsilon <<= 1
    gamma >>= 1
    epsilon >>= 1
    return gamma, epsilon


def calc_life_support(
    num_bits: int,
    numbers: List[int],
    ones: List[int],
    num_count: int,
    op: Callable[[Any, Any], bool],
) -> int:
    filt_list = numbers.copy()
    for i in range(num_bits):
        filt_list = list(
            filter(
                lambda n: (n & (1 << num_bits - (i + 1)) != 0)
                == (op(ones[i], num_count / 2)),
                filt_list,
            )
        )
        if len(filt_list) == 1:
            return filt_list[0]
        else:
            ones = count_ones(num_bits, filt_list)
            num_count = len(filt_list)
    raise RuntimeError("No answer")


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_03.in") as input_file:
        num_bits, numbers = parse_input(input_file)
        print("num_bits:", num_bits)
        ones = count_ones(num_bits, numbers)
        print("ones:", ones)

        gamma, epsilon = calc_gamma(ones, len(numbers))
        print("gamma:", gamma)
        print("epsilon:", epsilon)
        print("power:", gamma * epsilon)

        oxygen = calc_life_support(num_bits, numbers, ones, len(numbers), operator.ge)
        print("oxygen:", oxygen)

        co2 = calc_life_support(num_bits, numbers, ones, len(numbers), operator.lt)
        print("co2:", co2)
        print("life support:", oxygen * co2)
