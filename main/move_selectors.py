import copy
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


def print_game(game):
    print(f"Game finished with {game.remaining_marbles} marbles left:")
    print(f"moves: {game.moves}")
    print(game.board)
    print(f"dist_score: {dist_score(game)}")


def traverse_node(game: Game, best_game: Game):
    pos_moves = game.get_possible_moves()
    if len(pos_moves) == 0:
        if best_game is None or dist_score(game) < dist_score(best_game):
            print("new best game")
            print_game(game)
            return game
    else:
        for move in pos_moves:
            game_copy = copy.deepcopy(game)
            game_copy.move_marble(move[0], move[1])
            best_game = traverse_node(game_copy, best_game)
    return best_game
