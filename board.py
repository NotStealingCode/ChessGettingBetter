from board_pieces import BoardPieces
from chesspieces.pawn import Pawn
from chesspieces.knight import Knight
from chesspieces.bishop import Bishop
from chesspieces.queen import Queen
from chesspieces.rook import Rook

from empty import Empty

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

    def board_setup(self):
        for y, item in enumerate(self.board_pieces):
            for x, piece in enumerate(item):
                match piece.value:
                    case BoardPieces.BLACK_ROOK.value:
                        black_pawn = Rook("Black", x, y)
                        self.board_pieces[y][x] = black_pawn
                    case BoardPieces.BLACK_KNIGHT.value:
                        black_pawn = Knight("Black", x, y)
                        self.board_pieces[y][x] = black_pawn
                    case BoardPieces.BLACK_BISHOP.value:
                        black_pawn = Bishop("Black", x, y)
                        self.board_pieces[y][x] = black_pawn
                    case BoardPieces.BLACK_QUEEN.value:
                        black_pawn = Queen("Black", x, y)
                        self.board_pieces[y][x] = black_pawn
                    case BoardPieces.BLACK_KING.value:
                        black_pawn = Pawn("Black", x, y)
                        self.board_pieces[y][x] = black_pawn
                    case BoardPieces.BLACK_PAWN.value:
                        black_pawn = Pawn("Black", x, y)
                        self.board_pieces[y][x] = black_pawn
                    case BoardPieces.WHITE_ROOK.value:
                        white_pawn = Pawn("White", x, y)
                        self.board_pieces[y][x] = white_pawn
                    case BoardPieces.WHITE_KNIGHT.value:
                        white_pawn = Knight("White", x, y)
                        self.board_pieces[y][x] = white_pawn
                    case BoardPieces.WHITE_BISHOP.value:
                        white_pawn = Bishop("White", x, y)
                        self.board_pieces[y][x] = white_pawn
                    case BoardPieces.WHITE_QUEEN.value:
                        white_pawn = Queen("White", x, y)
                        self.board_pieces[y][x] = white_pawn
                    case BoardPieces.WHITE_KING.value:
                        white_pawn = Pawn("White", x, y)
                        self.board_pieces[y][x] = white_pawn
                    case BoardPieces.WHITE_PAWN.value:
                        white_pawn = Pawn("White", x, y)
                        self.board_pieces[y][x] = white_pawn
                    case BoardPieces.EMPTY.value:
                        white_pawn = Empty(x, y)
                        self.board_pieces[y][x] = white_pawn


board = Board(800, 800)
board.board_setup()
row_index = 1
column_index = 3
specific_piece = board.board_pieces[row_index][column_index]
moveset = specific_piece.get_possible_moves(board.board_pieces)
print(moveset)