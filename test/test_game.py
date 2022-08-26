from main.game import Game


def test_is_marble_at_position_true():
    target = Game()

    assert target.is_marble_at_position((0, 3))


def test_is_marble_at_position_no_marble():
    target = Game()

    assert not target.is_marble_at_position((4, 4))


def test_is_marble_at_position_ob():
    target = Game()

    assert not target.is_marble_at_position((0, 0))


def test_get_possible_moves():
    target = Game()

    actual = target.get_possible_moves()

    assert len(actual) == 4


def test_game_equality_same():
    game1 = Game()
    moves1 = game1.get_possible_moves()
    game1.move_marble(moves1[0][0], moves1[0][1])
    game2 = Game()
    moves2 = game2.get_possible_moves()
    game2.move_marble(moves2[0][0], moves2[1][1])

    assert game1 == game2


def test_game_equality_dif_len():
    game1 = Game()
    moves = game1.get_possible_moves()
    game1.move_marble(moves[0][0], moves[0][1])

    assert game1 != Game()


def test_game_equality_dif_moves():
    game1 = Game()
    moves1 = game1.get_possible_moves()
    game1.move_marble(moves1[0][0], moves1[0][1])
    game2 = Game()
    moves2 = game2.get_possible_moves()
    game2.move_marble(moves2[1][0], moves2[1][1])

    assert game1 != game2
