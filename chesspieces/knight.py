from piece import Piece

class Knight(Piece):
    def __init__(self, color, x_coordinates, y_coordinates):
        self.color = color
        self.x_coordinates = x_coordinates
        self.y_coordinates = y_coordinates
        self.name = "Knight"

    def get_possible_moves(self, pieces_location):
        moves = []
        enemy = "Black" if self.color == "White" else "White"
        POSITION_SHIFT_BY_TWO = 2
        POSITION_SHIFT_BY_TWO_OPPOSITE = -2
        POSITION_SHIFT_BY_ONE = 1
        POSITION_SHIFT_BY_ONE_OPPOSITE = -1
        STARTING_POSITION = 0
        ENDING_POSITION = 7
        moves.append((self.x_coordinates + POSITION_SHIFT_BY_TWO, self.y_coordinates + POSITION_SHIFT_BY_ONE))
        moves.append((self.x_coordinates + POSITION_SHIFT_BY_TWO, self.y_coordinates + POSITION_SHIFT_BY_ONE_OPPOSITE))
        moves.append((self.x_coordinates + POSITION_SHIFT_BY_TWO_OPPOSITE, self.y_coordinates + POSITION_SHIFT_BY_ONE))
        moves.append((self.x_coordinates + POSITION_SHIFT_BY_TWO_OPPOSITE, self.y_coordinates + POSITION_SHIFT_BY_ONE_OPPOSITE))
        moves.append((self.x_coordinates + POSITION_SHIFT_BY_ONE, self.y_coordinates + POSITION_SHIFT_BY_TWO))
        moves.append((self.x_coordinates + POSITION_SHIFT_BY_ONE, self.y_coordinates + POSITION_SHIFT_BY_TWO_OPPOSITE))
        moves.append((self.x_coordinates + POSITION_SHIFT_BY_ONE_OPPOSITE, self.y_coordinates + POSITION_SHIFT_BY_TWO))
        moves.append((self.x_coordinates + POSITION_SHIFT_BY_ONE_OPPOSITE, self.y_coordinates + POSITION_SHIFT_BY_TWO_OPPOSITE))
        moves = [(value, key) for (value, key) in moves if key >= STARTING_POSITION and key <= ENDING_POSITION and value >= STARTING_POSITION and value <= ENDING_POSITION]
        moves1 = []
        for possible_moves in moves:
            row = possible_moves[1]
            column = possible_moves[0]
            not_empty = pieces_location[row][column].name is not None
            if not_empty:
                enemy_found = pieces_location[row][column].color == enemy
                if enemy_found:
                    moves1.append(possible_moves)
            else:
                moves1.append(possible_moves)

        moves = moves1
        del moves1
        return moves