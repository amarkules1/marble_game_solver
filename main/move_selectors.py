import copy
import random

import pandas as pd

from main.game import Game


def select_random_move(pos_moves):
    return random.choice(pos_moves)


def follow_best_game(curr_game: Game, best_game: Game):
    if curr_game.moves == best_game.moves[0:len(curr_game.moves)]:
        if random.choice(range(0, curr_game.remaining_marbles)) < 2:
            return select_random_move(curr_game.get_possible_moves())
        return best_game.moves[len(curr_game.moves)]
    return select_random_move(curr_game.get_possible_moves())


def compare_games_center_proximity(game1: Game, game2: Game):
    if game1.dist_score() < game2.dist_score():
        return game1
    return game2


def print_game(game):
    print(f"Game finished with {game.remaining_marbles} marbles left:")
    print(f"moves: {game.moves}")
    print(game.board)
    print(f"dist_score: {game.dist_score()}")


def traverse_node(game: Game, best_game: Game):
    pos_moves = game.get_possible_moves()
    if len(pos_moves) == 0:
        if best_game is None or game.dist_score() < best_game.dist_score():
            print("new best game")
            print_game(game)
            return game
    else:
        for move in pos_moves:
            game_copy = copy.deepcopy(game)
            game_copy.move_marble(move[0], move[1])
            best_game = traverse_node(game_copy, best_game)
    return best_game


def select_top_n(games: list, n: int):
    games.sort(key=lambda x: x.dist_score())
    return games[0:n]


def enumerate_children(game: Game):
    children = list()
    for move in game.get_possible_moves():
        child_game = copy.deepcopy(game)
        child_game.move_marble(move[0], move[1])
        children.append(child_game)
    return children


def get_n_random_children(game: Game, n: int):
    pos_moves = game.get_possible_moves()
    if len(pos_moves) <= n:
        return enumerate_children(game)
    children = list()
    for i in range(0, n):
        child = copy.deepcopy(game)
        move = pos_moves[random.choice(range(0, len(pos_moves)))]
        child.move_marble(move[0], move[1])
        children.append(child)
    return children


def run_generation(parent_games: list, survivor_ct_func, children_per_survivor_func):
    parent_games = list(set(parent_games))
    survivors = select_top_n(parent_games, survivor_ct_func(len(parent_games), parent_games[0].remaining_marbles))
    children = list()
    for survivor in survivors:
        children.extend(get_n_random_children(survivor, children_per_survivor_func(len(parent_games), parent_games[0].remaining_marbles)))
    return children


def games_to_df(games: list):
    return pd.DataFrame.from_records([game.to_dict() for game in games])


def survivor_ct_function_1(parent_game_ct, remaining_marble_ct):
    return 20 - abs(18 - remaining_marble_ct)


def survivor_ct_function_2(parent_game_ct, remaining_marble_ct):
    return (40 - remaining_marble_ct) // 2

def children_per_survivor_func_1(parent_game_ct, remaining_marble_ct):
    return 5


def children_per_survivor_func_2(parent_game_ct, remaining_marble_ct):
    return 10 if remaining_marble_ct > 7 else 1000


def survivor_ct_function_3(parent_game_ct, remaining_marble_ct):
    return 100 if remaining_marble_ct > 7 else 100000

