from day_21 import play_game, play_game_2


def test_part_1() -> None:

    p1_score, p2_score, rolls = play_game(4, 8)
    assert p2_score == 745
    assert rolls == 993


def test_part_2() -> None:

    p1_wins, p2_wins = play_game_2(4, 8)
    assert p1_wins == 444356092776315
    assert p2_wins == 341960390180808
