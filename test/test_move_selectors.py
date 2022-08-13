from main.game import Game
from main.move_selectors import traverse_node


def test_traverse_node():
    game = Game()

    best_game = traverse_node(game, None)
