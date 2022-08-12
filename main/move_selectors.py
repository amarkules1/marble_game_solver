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


def dist_score(game:Game):
    game_sum = 0
    for i in range(0, 7):
        for j in range(0, 7):
            if game.board[i][j] == 1:
                game_sum = game_sum + abs(3 - i)
                game_sum = game_sum + abs(3 - j)
    return game_sum


def compare_games_center_proximity(game1: Game, game2: Game):
    if dist_score(game1) < dist_score(game2):
        return game1
    return game2

