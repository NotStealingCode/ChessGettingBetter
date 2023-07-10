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
        
            