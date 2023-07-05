from piece import Piece

class Empty(Piece):
    def __init__(self, x_coordinates, y_coordinates):
        self.x_coordinates = x_coordinates
        self.y_coordinates = y_coordinates