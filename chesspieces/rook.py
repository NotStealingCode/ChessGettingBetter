from piece import Piece

class Rook(Piece):
    def __init__(self, color, x_coordinates, y_coordinates):
        self.color = color
        self.x_coordinates = x_coordinates
        self.y_coordinates = y_coordinates
        self.name = "Rook"

    def get_possible_moves(self, pieces_location):
        board_pieces_location = pieces_location
        moves = []
        LEFT_OFFSET = -1
        RIGHT_OFFSET = 1
        STARTING_POSITION = 0
        ENDING_POSITION = 7
        enemy = "Black" if self.color == "White" else "White"
        for i in (LEFT_OFFSET, RIGHT_OFFSET):
            x = self.x_coordinates + i
            while STARTING_POSITION <= x <= ENDING_POSITION:
                is_not_empty = board_pieces_location[self.y_coordinates][x].name is not None
                if is_not_empty:
                    if board_pieces_location[self.y_coordinates][x].color == enemy:
                        moves.append((x, self.y_coordinates))
                    break
                moves.append((x, self.y_coordinates))
                x += i


        for i in (LEFT_OFFSET, RIGHT_OFFSET):
            y = self.y_coordinates + i
            while STARTING_POSITION <= y <= ENDING_POSITION:
                is_not_empty = board_pieces_location[y][self.x_coordinates].name is not None
                if is_not_empty:
                    if board_pieces_location[y][self.x_coordinates].color == enemy:
                        moves.append((self.x_coordinates, y))
                    break
                moves.append((self.x_coordinates, y))
                y += i
        return moves