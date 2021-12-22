import copy
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


@dataclass
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
    next_state = copy.copy(state)
    if next_state.p1_turn:
        next_state.p1_place += roll
        next_state.p1_place = ((next_state.p1_place - 1) % 10) + 1
        next_state.p1_score += next_state.p1_place
        next_state.p1_turn = False
    else:
        next_state.p2_place += roll
        next_state.p2_place = ((next_state.p2_place - 1) % 10) + 1
        next_state.p2_score += next_state.p2_place
        next_state.p1_turn = True
    return next_state


def play_game_2(p1_start: int, p2_start: int) -> tuple[int, int]:
    p1_wins = 0
    p2_wins = 0

    states = [(State(p1_start, p2_start), 1)]
    win_states: list[tuple[State, int]] = []
    while states:
        states = [
            (evolve_state(state[0], roll[0]), roll[1] * state[1])
            for roll in POSSIBLE_ROLLS
            for state in states
        ]
        win_states.extend(
            s for s in states if s[0].p1_score >= 21 or s[0].p2_score >= 21
        )
        states = [s for s in states if s[0].p1_score < 21 and s[0].p2_score < 21]
        print("states:", states)
        print("win_states:", win_states)

    p1_wins = sum(s[1] for s in win_states if s[0].p1_score >= 21)
    p2_wins = sum(s[1] for s in win_states if s[0].p2_score >= 21)

    return p1_wins, p2_wins


if __name__ == "__main__":
    p1_score, p2_score, rolls = play_game(8, 3)

    print("part 1:", min(p1_score, p2_score) * rolls)

    p1_wins, p2_wins = play_game_2(8, 3)

    print("part 2:", max(p1_wins, p2_wins))
