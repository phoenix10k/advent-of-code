import os
import operator

from day_03 import parse_input, count_ones, calc_gamma, calc_life_support


def test_part_1() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_03.in") as input_file:
        num_bits, numbers = parse_input(input_file)
        assert num_bits == 5
        ones = count_ones(num_bits, numbers)

        gamma, epsilon = calc_gamma(ones, len(numbers))
        assert gamma == 22
        assert epsilon == 9
        assert gamma * epsilon == 198


def test_part_2() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_03.in") as input_file:
        num_bits, numbers = parse_input(input_file)
        ones = count_ones(num_bits, numbers)

        oxygen = calc_life_support(num_bits, numbers, ones, len(numbers), operator.ge)
        assert oxygen == 23
        co2 = calc_life_support(num_bits, numbers, ones, len(numbers), operator.lt)
        assert co2 == 10
        assert oxygen * co2 == 230
