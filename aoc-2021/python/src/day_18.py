import ast
import copy
import functools
import itertools
import operator
import os
from typing import Any, Optional, TextIO, Union


class Number:
    left: Union["Number", int]
    right: Union["Number", int]
    parent: Optional["Number"] = None
    is_left: bool = False

    def __init__(self, left: Union["Number", int], right: Union["Number", int]) -> None:
        self.left = left
        if isinstance(self.left, Number):
            self.left.parent = self
            self.left.is_left = True

        self.right = right
        if isinstance(self.right, Number):
            self.right.parent = self
            self.right.is_left = False

    @classmethod
    def from_string(cls, string: str) -> "Number":
        tree = ast.literal_eval(string)
        assert isinstance(tree, list)
        return Number.from_list(tree)

    @classmethod
    def from_list(cls, tree: list[Any]) -> "Number":
        assert (len(tree)) == 2
        left: Union["Number", int] = (
            tree[0] if isinstance(tree[0], int) else Number.from_list(tree[0])
        )
        right: Union["Number", int] = (
            tree[1] if isinstance(tree[1], int) else Number.from_list(tree[1])
        )
        return Number(left, right)

    def add_left(self, val: int, from_left: bool, from_above: bool) -> None:
        if from_left:
            if self.parent:
                self.parent.add_left(val, self.is_left, False)
        elif isinstance(self.left, Number):
            if from_above:
                self.left.add_left(val, False, True)
            else:
                self.left.add_right(val, True, True)
        else:
            self.left += val

    def add_right(self, val: int, from_left: bool, from_above: bool) -> None:
        if not from_left:
            if self.parent:
                self.parent.add_right(val, self.is_left, False)
        elif isinstance(self.right, Number):
            if from_above:
                self.right.add_right(val, True, True)
            else:
                self.right.add_left(val, False, True)
        else:
            self.right += val

    def explode(self, depth: int = 0) -> bool:
        if depth == 4:
            assert self.parent is not None
            assert isinstance(self.left, int)
            assert isinstance(self.right, int)
            self.parent.add_left(self.left, self.is_left, False)
            self.parent.add_right(self.right, self.is_left, False)
            if self.is_left:
                self.parent.left = 0
            else:
                self.parent.right = 0
            # print(f"exploding [{self.left},{self.right}]")
            return True
        if isinstance(self.left, Number):
            if self.left.explode(depth + 1):
                return True
        if isinstance(self.right, Number):
            if self.right.explode(depth + 1):
                return True
        return False

    def split(self) -> bool:
        if isinstance(self.left, int):
            if self.left > 9:
                lhs = self.left // 2
                rhs = self.left - lhs
                # print(f"splitting {self.left} to [{lhs},{rhs}]")
                self.left = Number(lhs, rhs)
                self.left.parent = self
                self.left.is_left = True
                return True
        elif self.left.split():
            return True
        if isinstance(self.right, int):
            if self.right > 9:
                lhs = self.right // 2
                rhs = self.right - lhs
                # print(f"splitting {self.right} to [{lhs},{rhs}]")
                self.right = Number(lhs, rhs)
                self.right.parent = self
                self.right.is_left = False
                return True
        elif self.right.split():
            return True
        return False

    def reduce(self) -> None:
        while True:
            if not self.explode():
                if not self.split():
                    return

    @property
    def magnitude(self) -> int:
        lmag = self.left.magnitude if isinstance(self.left, Number) else self.left
        rmag = self.right.magnitude if isinstance(self.right, Number) else self.right
        return 3 * lmag + 2 * rmag

    def __add__(self, other: "Number") -> "Number":
        res = Number(self, other)
        res.reduce()
        return res

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Number):
            return self.left == other.left and self.right == other.right
        return False

    def __repr__(self) -> str:
        return f"[{repr(self.left)},{repr(self.right)}]"


def parse_input(input_file: TextIO) -> list[Number]:
    return [Number.from_string(line.strip()) for line in input_file]


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_18.in") as input_file:
        number_list = parse_input(input_file)

    print(
        "part 1:", functools.reduce(operator.add, copy.deepcopy(number_list)).magnitude
    )

    maxmag = 0
    for lhs, rhs in itertools.permutations(number_list, 2):
        lhs = copy.deepcopy(lhs)
        rhs = copy.deepcopy(rhs)
        maxmag = max(maxmag, (lhs + rhs).magnitude)
    print("part 2:", maxmag)
