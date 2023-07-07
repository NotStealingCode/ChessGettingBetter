from board_pieces import BoardPieces
from pawn import Pawn

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board_pieces = [
            [BoardPieces.BLACK_ROOK, BoardPieces.BLACK_KNIGHT, BoardPieces.BLACK_BISHOP, BoardPieces.BLACK_QUEEN, BoardPieces.BLACK_KING, BoardPieces.BLACK_BISHOP, BoardPieces.BLACK_KNIGHT, BoardPieces.BLACK_ROOK],
            [BoardPieces.BLACK_PAWN, BoardPieces.BLACK_PAWN, BoardPieces.BLACK_PAWN, BoardPieces.BLACK_PAWN, BoardPieces.BLACK_PAWN, BoardPieces.BLACK_PAWN, BoardPieces.BLACK_PAWN, BoardPieces.BLACK_PAWN],
            [BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY],
            [BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY],
            [BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY],
            [BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY, BoardPieces.EMPTY],
            [BoardPieces.WHITE_PAWN, BoardPieces.WHITE_PAWN, BoardPieces.WHITE_PAWN, BoardPieces.WHITE_PAWN, BoardPieces.WHITE_PAWN, BoardPieces.WHITE_PAWN, BoardPieces.WHITE_PAWN, BoardPieces.WHITE_PAWN],
            [BoardPieces.WHITE_ROOK, BoardPieces.WHITE_KNIGHT, BoardPieces.WHITE_BISHOP, BoardPieces.WHITE_QUEEN, BoardPieces.WHITE_KING, BoardPieces.WHITE_BISHOP, BoardPieces.WHITE_KNIGHT, BoardPieces.WHITE_ROOK]
        ]
        self.white_pieces = [BoardPieces.WHITE_PAWN, BoardPieces.WHITE_ROOK, BoardPieces.WHITE_KNIGHT, BoardPieces.WHITE_BISHOP, BoardPieces.WHITE_QUEEN, BoardPieces.WHITE_KING, BoardPieces.WHITE_BISHOP, BoardPieces.WHITE_KNIGHT, BoardPieces.WHITE_ROOK]
        self.black_pieces = [BoardPieces.BLACK_ROOK, BoardPieces.BLACK_KNIGHT, BoardPieces.BLACK_BISHOP, BoardPieces.BLACK_QUEEN, BoardPieces.BLACK_KING, BoardPieces.BLACK_BISHOP, BoardPieces.BLACK_KNIGHT, BoardPieces.BLACK_ROOK, BoardPieces.BLACK_PAWN]
        self.board_setup()

    def board_setup(self):
        for y, item in enumerate(self.board_pieces):
            for x, piece in enumerate(item):
                match piece.value:
                    case 11:
                        black_pawn = Pawn("Black", x, y)
                        self.board_pieces[y][x] = black_pawn
                    case 12:
                        black_pawn = Pawn("Black", x, y)
                        self.board_pieces[y][x] = black_pawn
                    case 13:
                        black_pawn = Pawn("Black", x, y)
                        self.board_pieces[y][x] = black_pawn
                    case 14:
                        black_pawn = Pawn("Black", x, y)
                        self.board_pieces[y][x] = black_pawn
                    case 15:
                        black_pawn = Pawn("Black", x, y)
                        self.board_pieces[y][x] = black_pawn
                    case 16:
                        black_pawn = Pawn("Black", x, y)
                        self.board_pieces[y][x] = black_pawn
                    case 1:
                        white_pawn = Pawn("White", x, y)
                        self.board_pieces[y][x] = white_pawn
                    case 2:
                        white_pawn = Pawn("White", x, y)
                        self.board_pieces[y][x] = white_pawn
                    case 3:
                        white_pawn = Pawn("White", x, y)
                        self.board_pieces[y][x] = white_pawn
                    case 4:
                        white_pawn = Pawn("White", x, y)
                        self.board_pieces[y][x] = white_pawn
                    case 5:
                        white_pawn = Pawn("White", x, y)
                        self.board_pieces[y][x] = white_pawn
                    case 6:
                        white_pawn = Pawn("White", x, y)
                        self.board_pieces[y][x] = white_pawn
                    case 0:
                        white_pawn = Pawn("White", x, y)
                        self.board_pieces[y][x] = white_pawn
                    

board = Board(800, 800)
counter = 0
print(board.board_pieces)

for x in board.board_pieces:
    for z in x:
        coordinates = (z.x_coordinates, z.y_coordinates)
        print(coordinates)