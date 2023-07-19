from piece import Piece
from chesspieces.bishop import Bishop
from chesspieces.rook import Rook

class Queen(Piece):
    def __init__(self, color, x_coordinates, y_coordinates):
        self.color = color
        self.x_coordinates = x_coordinates
        self.y_coordinates = y_coordinates
        self.name = "Queen"

    def get_possible_moves(self, pieces_location):
        rook = Rook(self.color, self.x_coordinates, self.y_coordinates)
        bishop = Bishop(self.color, self.x_coordinates, self.y_coordinates)
        moves = []
        moves_rook = rook.get_possible_moves(pieces_location)
        moves_bishop = bishop.get_possible_moves(pieces_location)
        moves = moves_rook + moves_bishop
        return moves

        
            