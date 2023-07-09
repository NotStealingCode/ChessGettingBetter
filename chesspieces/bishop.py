from piece import Piece

class Bishop(Piece):
    def __init__(self, color, x_coordinates, y_coordinates):
        self.color = color
        self.x_coordinates = x_coordinates
        self.y_coordinates = y_coordinates
        self.name = "Bishop"

    def get_possible_moves(self, pieces_location):
        moves = []
        board_pieces_location = pieces_location
        enemy = "Black" if self.color == "White" else "White"
        LEFT_OFFSET = -1
        RIGHT_OFFSET = 1
        STARTING_POSITION = 0
        ENDING_POSITION = 7
        for i in (LEFT_OFFSET, RIGHT_OFFSET):
            y = self.y_coordinates + RIGHT_OFFSET
            x = self.x_coordinates + i
            x_on_board = STARTING_POSITION <= x <= ENDING_POSITION
            y_on_board = STARTING_POSITION <= y <= ENDING_POSITION
            while x_on_board and y_on_board:
                is_not_empty = board_pieces_location[y][x].name is not None
                if is_not_empty:
                    if board_pieces_location[y][x].color == enemy:
                        moves.append((x, y))
                    break
                moves.append((x, y))
                x += i
                y += RIGHT_OFFSET
                
        for i in (LEFT_OFFSET, RIGHT_OFFSET):
            y = self.y_coordinates + LEFT_OFFSET
            x = self.x_coordinates + i
            x_on_board = STARTING_POSITION <= x <= ENDING_POSITION
            y_on_board = STARTING_POSITION <= y <= ENDING_POSITION
            while x_on_board and y_on_board:
                is_not_empty = board_pieces_location[y][x].name is not None
                if is_not_empty:
                    if board_pieces_location[y][x].color == enemy:
                        moves.append((x, y))
                    break
                moves.append((x, y))
                x += i
                y += LEFT_OFFSET
        return moves