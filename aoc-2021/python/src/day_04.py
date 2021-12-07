import os
from typing import Iterable, List, Tuple, TextIO
from dataclasses import dataclass


@dataclass
class Cell:
    value: int
    called: bool = False


class Board:
    rows: List[List[Cell]]

    def __init__(self) -> None:
        self.rows = []

    def add_row(self, row: Iterable[int]) -> None:
        new_row = [Cell(v) for v in row]
        if self.rows:
            assert len(new_row) == len(self.rows[0])
        self.rows.append(new_row)

    def mark(self, value: int) -> None:
        for row in self.rows:
            for cell in row:
                if cell.value == value:
                    cell.called = True

    @property
    def win(self) -> bool:
        if any(all(cell.called for cell in row) for row in self.rows):
            return True
        else:
            return any(
                all(self.rows[i][j].called for i in range(len(self.rows)))
                for j in range(len(self.rows[0]))
            )

    @property
    def score(self) -> int:
        return sum(cell.value for row in self.rows for cell in row if not cell.called)


def parse_input(input_file: TextIO) -> Tuple[List[int], List[Board]]:
    draw = [int(d) for d in next(input_file).split(",")]
    next(input_file)  # skip blank line
    board = Board()
    boards = []
    for line in input_file:
        if line.strip():
            board.add_row(int(v) for v in line.split())
        else:
            boards.append(board)
            board = Board()
    return draw, boards


def get_winning_score(draw: Iterable[int], boards: List[Board]) -> int:
    for d in draw:
        for board in boards:
            board.mark(d)
            if board.win:
                return board.score * d
    raise RuntimeError("No winners")


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    with open("../data/day_04.in") as input_file:
        draw, boards = parse_input(input_file)

    print("wining score:", get_winning_score(draw, boards))
