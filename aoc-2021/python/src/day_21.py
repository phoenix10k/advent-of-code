import functools
from dataclasses import dataclass
from itertools import cycle, islice


def play_game(p1_start: int, p2_start: int) -> tuple[int, int, int]:
    p1_score = 0
    p2_score = 0
    rolls = 0
    p1_turn = True
    p1_place = p1_start
    p2_place = p2_start

    die = cycle(range(1, 101))
    while max(p1_score, p2_score) < 1000:
        rolls += 3
        roll = sum(islice(die, 3))
        if p1_turn:
            p1_place += roll
            p1_place = ((p1_place - 1) % 10) + 1
            p1_score += p1_place
            p1_turn = False
        else:
            p2_place += roll
            p2_place = ((p2_place - 1) % 10) + 1
            p2_score += p2_place
            p1_turn = True

    return p1_score, p2_score, rolls


@dataclass(frozen=True)
class State:
    p1_place: int = 0
    p2_place: int = 0
    p1_score: int = 0
    p2_score: int = 0
    p1_turn: int = True


POSSIBLE_ROLLS = [
    (3, 1),
    (4, 3),
    (5, 6),
    (6, 7),
    (7, 6),
    (8, 3),
    (9, 1),
]


def evolve_state(state: State, roll: int) -> State:
    if state.p1_turn:
        new_place = ((state.p1_place + roll - 1) % 10) + 1
        next_state = State(
            new_place, state.p2_place, state.p1_score + new_place, state.p2_score, False
        )
    else:
        new_place = ((state.p2_place + roll - 1) % 10) + 1
        next_state = State(
            state.p1_place, new_place, state.p1_score, state.p2_score + new_place, True
        )
    return next_state


@functools.lru_cache(maxsize=100000)
def calc_wins(state: State) -> tuple[int, int]:
    if state.p1_score >= 21:
        return 1, 0
    if state.p2_score >= 21:
        return 0, 1
    p1_wins = 0
    p2_wins = 0
    for roll, count in POSSIBLE_ROLLS:
        new_state = evolve_state(state, roll)
        p1w, p2w = calc_wins(new_state)
        p1_wins += p1w * count
        p2_wins += p2w * count
    print(f"wins for state {state}: p1:{p1_wins}, p2:{p2_wins}")
    print("cache info:", calc_wins.cache_info())
    return p1_wins, p2_wins


def play_game_2(p1_start: int, p2_start: int) -> tuple[int, int]:
    return calc_wins(State(p1_start, p2_start))


if __name__ == "__main__":
    p1_score, p2_score, rolls = play_game(8, 3)

    print("part 1:", min(p1_score, p2_score) * rolls)

    p1_wins, p2_wins = play_game_2(8, 3)

    print("part 2:", max(p1_wins, p2_wins))
