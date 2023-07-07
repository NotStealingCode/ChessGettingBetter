from piece import Piece

class Pawn(Piece):
    def __init__(self, color, x_coordinates, y_coordinates):
        self.color = color
        self.x_coordinates = x_coordinates
        self.y_coordinates = y_coordinates
        self.name = "Pawn"
    
    def get_possible_moves(self, pieces_location):
        board_pieces_locations = pieces_location
        moves = []
        if self.color == "White":
            advance_once = self.y_coordinates + 1
            advance_twice = self.y_coordinates + 2
            if self.y_coordinates == 1:
                moves.append((self.x_coordinates, advance_once))
                moves.append((self.x_coordinates, advance_twice))
            else:
                moves.append((self.x_coordinates, advance_once))
            
            for piece in board_pieces_locations[advance_once]:
                is_not_empty = piece.name is not None
                is_occupied = moves[0] == (piece.x_coordinates, piece.y_coordinates)
                if is_occupied and is_not_empty:
                    moves = []
                    break
        
            if len(moves) == 2:
                for piece_location in board_pieces_locations[advance_twice]:
                    is_occupied = moves[1] == (piece_location.x_coordinates, piece_location.y_coordinates)
                    is_not_empty = piece_location is not None
                    if is_occupied and is_not_empty:
                        moves.remove((self.x_coordinates, advance_twice))





