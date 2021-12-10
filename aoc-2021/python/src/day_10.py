import os
from typing import List, TextIO

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

complete_scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

closing_chars = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


class MySyntaxError(RuntimeError):
    def __init__(self, message: str, invalid_char: str) -> None:
        super().__init__(message)
        self.invalid_char = invalid_char


def parse_line(line: str) -> List[str]:
    stack = []
    for c in line:
        if c in closing_chars.keys():
            stack.append(closing_chars[c])
        else:
            expected = stack.pop()
            if c != expected:
                raise MySyntaxError(f"Expected {expected}, but found {c}", c)
    return stack


def calc_se_score(file: TextIO) -> int:
    score = 0
    for line in file:
        try:
            parse_line(line.strip())
        except MySyntaxError as se:
            score += scores[se.invalid_char]
    return score


def calc_complete_score(stack: List[str]) -> int:
    score = 0
    for char in reversed(stack):
        score *= 5
        score += complete_scores[char]
    return score


def calc_middle_complete_score(file: TextIO) -> int:
    scores = []
    for line in file:
        try:
            stack = parse_line(line.strip())
        except MySyntaxError as se:
            pass
        else:
            scores.append(calc_complete_score(stack))
    return sorted(scores)[len(scores) // 2]


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_10.in") as input_file:
        score = calc_se_score(input_file)

    print("part 1:", score)

    with open("../data/day_10.in") as input_file:
        score = calc_middle_complete_score(input_file)

    print("part 2:", score)
