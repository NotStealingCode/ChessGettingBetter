from piece import Piece

class Pawn(Piece):
    def __init__(self, color, x_coordinates, y_coordinates):
        self.color = color
        self.x_coordinates = x_coordinates
        self.y_coordinates = y_coordinates
        self.name = "Pawn"
    
    def get_possible_moves(self, allies, enemies):
        moves = []
        if self.color == "White":
            white = allies
            black = enemies
            if self.y_coordinates == 1:
                moves.append(self.x_coordinates, self.y_coordinates + 1)
                moves.append(self.x_coordinates, self.y_coordinates + 2)
            else:
                moves.append(self.x_coordinates, self.y_coordinates + 1)
            
            



