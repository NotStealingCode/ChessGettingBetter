from piece import Piece
from chesspieces.bishop import Bishop
from chesspieces.rook import Rook

class Queen(Piece):
    def __init__(self, color, x_coordinates, y_coordinates):
        self.color = color
        self.x_coordinates = x_coordinates
        self.y_coordinates = y_coordinates
        self.name = "Queen"
        self.rook = Rook(color, x_coordinates, y_coordinates)
        self.bishop = Bishop(color, x_coordinates, y_coordinates)

    def get_possible_moves(self, pieces_location):
        moves = []
        moves_rook = self.rook.get_possible_moves(pieces_location)
        moves_bishop = self.bishop.get_possible_moves(pieces_location)
        moves = moves_rook + moves_bishop
        return moves

        
            