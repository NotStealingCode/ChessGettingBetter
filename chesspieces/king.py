from piece import Piece

class King(Piece):
    def __init__(self, color, x_coordinates, y_coordinates):
        self.color = color
        self.x_coordinates = x_coordinates
        self.y_coordinates = y_coordinates
        self.name = "King"

    def get_possible_moves(self, pieces_location):
        moves = []
        enemy = "Black" if self.color == "White" else "White"
        SHIFT_POSITION_BY_ONE = 1
        SHIFT_POSITION_BY_ONE_OPPOSITE = -1

        moves.append((self.x_coordinates + SHIFT_POSITION_BY_ONE, self.y_coordinates))
        moves.append((self.x_coordinates + SHIFT_POSITION_BY_ONE, self.y_coordinates + SHIFT_POSITION_BY_ONE))
        moves.append((self.x_coordinates + SHIFT_POSITION_BY_ONE, self.y_coordinates + SHIFT_POSITION_BY_ONE_OPPOSITE))
        moves.append((self.x_coordinates + SHIFT_POSITION_BY_ONE_OPPOSITE, self.y_coordinates))
        moves.append((self.x_coordinates + SHIFT_POSITION_BY_ONE_OPPOSITE, self.y_coordinates + SHIFT_POSITION_BY_ONE))
        moves.append((self.x_coordinates + SHIFT_POSITION_BY_ONE_OPPOSITE, self.y_coordinates + SHIFT_POSITION_BY_ONE_OPPOSITE))
        moves.append((self.x_coordinates, self.y_coordinates + SHIFT_POSITION_BY_ONE))
        moves.append((self.x_coordinates, self.y_coordinates + SHIFT_POSITION_BY_ONE_OPPOSITE))

        moves = [(value, key) for (value, key) in moves if key >= 0 and key <= 7 and value >= 0 and value <= 7]
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


        
            