import random

from main.game import Game


def select_random_move(pos_moves):
    return random.choice(pos_moves)


def follow_best_game(curr_game: Game, best_game: Game):
    if curr_game.moves == best_game.moves[0:len(curr_game.moves)]:
        if random.choice(range(0, curr_game.remaining_marbles)) == 0:
            return select_random_move(curr_game.get_possible_moves())
        return best_game.moves[len(curr_game.moves)]
    return select_random_move(curr_game.get_possible_moves())
