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
        advance_once = self.y_coordinates - 1 if self.color == "White" else self.y_coordinates + 1
        advance_twice = self.y_coordinates - 2 if self.color == "White" else self.y_coordinates + 2
        starting_position = 6 if self.color == "White" else 1
        ending_position = 0 if self.color == "White" else 7
        enemy = "Black" if self.color == "White" else "White"
        MAX_RIGHT = 7
        MAX_LEFT = 0
        if self.y_coordinates != ending_position:
            if self.y_coordinates == starting_position:
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
            
            EXPECTED_NUMBER_OF_MOVES = 2
            if len(moves) == EXPECTED_NUMBER_OF_MOVES:
                for piece_location in board_pieces_locations[advance_twice]:
                    if moves[1] == ((piece_location.x_coordinates, piece_location.y_coordinates)):
                        is_not_empty = piece_location.name is not None
                        if is_not_empty:
                            moves.remove((self.x_coordinates, advance_twice))
                            break
            
            LEFT_OFFSET = -1
            RIGHT_OFFSET = 1
            if self.x_coordinates < MAX_RIGHT:
                if board_pieces_locations[advance_once][self.x_coordinates + RIGHT_OFFSET].name is not None:
                    attack_right = board_pieces_locations[advance_once][self.x_coordinates + RIGHT_OFFSET].color == enemy
                    if attack_right:
                        moves.append((self.x_coordinates + RIGHT_OFFSET, advance_once))
            
            if self.x_coordinates > MAX_LEFT:
                if board_pieces_locations[advance_once][self.x_coordinates + LEFT_OFFSET].name is not None:
                    attack_left = board_pieces_locations[advance_once][self.x_coordinates + LEFT_OFFSET].color == enemy
                    if attack_left:
                        moves.append((self.x_coordinates + LEFT_OFFSET, advance_once))
                
        return moves

            

            
            





