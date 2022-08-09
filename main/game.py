def is_distance_2_apart(source, dest):
    if source[0] == dest[0]:
        return abs(source[1] - dest[1]) == 2
    elif source[1] == dest[1]:
        return abs(source[0] - dest[0]) == 2
    return False


def get_middle_position(source, dest):
    return (source[0] + dest[0]) // 2, (source[1] + dest[1]) // 2


class Game:
    moves: list
    board: list
    remaining_marbles = 49

    def __init__(self):
        self.moves = list()
        self.board = list()
        self.board.append([2, 2, 2, 1, 1, 1, 2, 2, 2])
        self.board.append([2, 2, 2, 1, 1, 1, 2, 2, 2])
        self.board.append([2, 2, 1, 1, 1, 1, 1, 2, 2])
        self.board.append([1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.board.append([1, 1, 1, 1, 0, 1, 1, 1, 1])
        self.board.append([1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.board.append([2, 2, 1, 1, 1, 1, 1, 2, 2])
        self.board.append([2, 2, 2, 1, 1, 1, 2, 2, 2])
        self.board.append([2, 2, 2, 1, 1, 1, 2, 2, 2])

    def is_marble_at_position(self, pos):
        return self.is_in_bounds(pos) and self.board[pos[0]][pos[1]] == 1

    def is_valid_move(self, source, dest):
        if not self.is_in_bounds(source):
            return False
        if not self.is_in_bounds(dest):
            return False
        if not self.is_marble_at_position(source):
            return False
        if self.is_marble_at_position(dest):
            return False
        if not self.is_marble_at_position(get_middle_position(source, dest)):
            return False
        return is_distance_2_apart(source, dest)

    def record_move(self, source, dest):
        self.moves.append((source, dest))
        self.remaining_marbles = self.remaining_marbles - 1

    def move_marble(self, source, dest):
        if self.is_valid_move(source, dest):
            self.board[dest[0]][dest[1]] = 1
            self.board[source[0]][source[1]] = 0
            middle_pos = get_middle_position(source, dest)
            self.board[middle_pos[0]][middle_pos[1]] = 0
            self.record_move(source, dest)
            return True
        return False

    def is_in_bounds(self, pos):
        if 0 <= pos[0] < 9 and 0 <= pos[1] < 9:
            return self.board[pos[0]][pos[1]] != 2
        return False


    def get_possible_moves(self):
        pos_moves = list()
        for i in range(0, 9):
            for j in range(0, 9):
                if self.is_in_bounds((i, j)) and not self.is_marble_at_position((i, j)):
                    if self.is_marble_at_position((i, j - 1)) and self.is_marble_at_position((i, j - 2)):
                        pos_moves.append(((i, j - 2), (i, j)))
                    if self.is_marble_at_position((i, j + 1)) and self.is_marble_at_position((i, j + 2)):
                        pos_moves.append(((i, j + 2), (i, j)))
                    if self.is_marble_at_position((i - 1, j)) and self.is_marble_at_position((i - 2, j)):
                        pos_moves.append(((i - 2, j), (i, j)))
                    if self.is_marble_at_position((i + 1, j)) and self.is_marble_at_position((i + 2, j)):
                        pos_moves.append(((i + 2, j), (i, j)))

        return pos_moves
