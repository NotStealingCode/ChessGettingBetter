from piece import Piece

class Bishop(Piece):
    def __init__(self, color, x_coordinates, y_coordinates):
        self.color = color
        self.x_coordinates = x_coordinates
        self.y_coordinates = y_coordinates
        self.name = "Bishop"

    def get_possible_moves(self, allies, enemies):
        moves = []
        if self.color == "White":
            white = allies
            black = enemies
            