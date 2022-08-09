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

