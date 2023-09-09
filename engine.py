import pygame
from board import Board
from empty import Empty

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
CENTER_X = 20
CENTER_Y = 10
SIZE = 100
ORIGIN = (0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True


white_pawn = pygame.image.load("assets/images/pawnw.png")
white_bishop = pygame.image.load("assets/images/bishopw.png")
white_knight = pygame.image.load("assets/images/knightw.png")
white_rook = pygame.image.load("assets/images/rookw.png")
white_queen = pygame.image.load("assets/images/queenw.png")
white_king = pygame.image.load("assets/images/kingw.png")


black_pawn = pygame.image.load("assets/images/pawnb.png")
black_bishop = pygame.image.load("assets/images/bishopb.png")
black_knight = pygame.image.load("assets/images/knightb.png")
black_rook = pygame.image.load("assets/images/rookb.png")
black_queen = pygame.image.load("assets/images/queenb.png")
black_king = pygame.image.load("assets/images/kingb.png")
board_map = pygame.image.load("assets/images/cb2.png")


board = Board(SCREEN_WIDTH, SCREEN_HEIGHT)

def draw_pieces(current_pieces):
    for i in current_pieces:
        for n in i:
            piece_name = n.name
            match piece_name:
                case "Pawn":
                    if n.color == "White":
                        screen.blit(white_pawn, (n.x_coordinates * SIZE + CENTER_X, n.y_coordinates * SIZE + CENTER_Y))
                    else:
                        screen.blit(black_pawn, (n.x_coordinates * SIZE + CENTER_X, n.y_coordinates * SIZE + CENTER_Y))
                case "Rook":
                    if n.color == "White":
                        screen.blit(white_rook, (n.x_coordinates * SIZE + CENTER_X, n.y_coordinates * SIZE + CENTER_Y))
                    else:
                        screen.blit(black_rook, (n.x_coordinates * SIZE + CENTER_X, n.y_coordinates * SIZE + CENTER_Y))
                case "Knight":
                    if n.color == "White":
                        screen.blit(white_knight, (n.x_coordinates * SIZE + CENTER_X, n.y_coordinates * SIZE + CENTER_Y))
                    else:
                        screen.blit(black_knight, (n.x_coordinates * SIZE + CENTER_X, n.y_coordinates * SIZE + CENTER_Y))
                case "Bishop":
                    if n.color == "White":
                        screen.blit(white_bishop, (n.x_coordinates * SIZE + CENTER_X, n.y_coordinates * SIZE + CENTER_Y))
                    else:
                        screen.blit(black_bishop, (n.x_coordinates * SIZE + CENTER_X, n.y_coordinates * SIZE + CENTER_Y))
                case "King":
                    if n.color == "White":
                        screen.blit(white_king, (n.x_coordinates * SIZE + CENTER_X, n.y_coordinates * SIZE + CENTER_Y))
                    else:
                        screen.blit(black_king, (n.x_coordinates * SIZE + CENTER_X, n.y_coordinates * SIZE + CENTER_Y))
                case "Queen":
                    if n.color == "White":
                        screen.blit(white_queen, (n.x_coordinates * SIZE + CENTER_X, n.y_coordinates * SIZE + CENTER_Y))
                    else:
                        screen.blit(black_queen, (n.x_coordinates * SIZE + CENTER_X, n.y_coordinates * SIZE + CENTER_Y))
                
def get_coordinates():
    coordinates_x = event.pos[0] // SIZE
    coordinates_y = event.pos[1] // SIZE
    return ((coordinates_x, coordinates_y))

def get_selected_piece():
    coordinates_x = event.pos[0] // SIZE
    coordinates_y = event.pos[1] // SIZE
    selected_piece = board.board_pieces[coordinates_y][coordinates_x]
    return selected_piece
    
def get_allowed_moves(piece_name):
    if piece_name.name is not None:
        moveset = piece_name.get_possible_moves(board.board_pieces)
        return moveset
    return None

def draw_moves(moves):
    if moves is not None:
        for m in moves:
            pygame.draw.rect(screen, "green", pygame.Rect(m[0] * SIZE, m[1] * SIZE, SIZE, SIZE), 5)


def game_state():
    all_possible_moves = []
    for row in board.board_pieces:
        for piece in row:
            if piece.name is not None:
                if white_turn:
                    if piece.color == "White":
                        moves = piece.get_possible_moves(board.board_pieces)
                        allow = allowed_moves(piece, moves)
                        all_possible_moves += allow
                else:
                    if piece.color == "Black":
                        moves = piece.get_possible_moves(board.board_pieces)
                        allow = allowed_moves(piece, moves)
                        all_possible_moves += allow
    enemy_moves = acquire_enemy_moveset(white_turn)
    if len(all_possible_moves) == 0 and white_turn:
        if is_check(enemy_moves):
            print("Black wins!")
        else:
            print("Stalemate")
    if len(all_possible_moves) == 0 and not white_turn:
        if is_check(enemy_moves):
            print("White wins!")
        else:
            print("Stalemate")
    


def legal_check(piece_hovered, coordinates_listed):
    y = piece_hovered.y_coordinates
    x = piece_hovered.x_coordinates
    old_y = y
    old_x = x
    new_y = coordinates_listed[1]
    new_x = coordinates_listed[0]
    piece_hovered.x_coordinates = new_x
    piece_hovered.y_coordinates = new_y
    board.board_pieces[y][x], board.board_pieces[new_y][new_x] = board.board_pieces[new_y][new_x], board.board_pieces[y][x]
    if board.board_pieces[y][x].name is not None:
        incorrect_kill = board.board_pieces[y][x]
        board.board_pieces[y][x] = Empty(x, y)
        enemy_moves_2 = acquire_enemy_moveset(white_turn)
        if is_check(enemy_moves_2):
            board.board_pieces[y][x] = incorrect_kill
            board.board_pieces[y][x], board.board_pieces[incorrect_kill.y_coordinates][incorrect_kill.x_coordinates] = board.board_pieces[incorrect_kill.y_coordinates][incorrect_kill.x_coordinates], board.board_pieces[y][x]
            piece_hovered.x_coordinates = old_x
            piece_hovered.y_coordinates = old_y
            return False
        else:
            board.board_pieces[y][x] = incorrect_kill
            board.board_pieces[y][x], board.board_pieces[incorrect_kill.y_coordinates][incorrect_kill.x_coordinates] = board.board_pieces[incorrect_kill.y_coordinates][incorrect_kill.x_coordinates], board.board_pieces[y][x]
            piece_hovered.x_coordinates = old_x
            piece_hovered.y_coordinates = old_y
            return True
    else:
        enemy_moves_1 = acquire_enemy_moveset(white_turn)
        if is_check(enemy_moves_1):
            board.board_pieces[new_y][new_x], board.board_pieces[y][x] = board.board_pieces[y][x], board.board_pieces[new_y][new_x]
            piece_hovered.x_coordinates = x
            piece_hovered.y_coordinates = y
            return False
        else:
            board.board_pieces[new_y][new_x], board.board_pieces[y][x] = board.board_pieces[y][x], board.board_pieces[new_y][new_x]
            piece_hovered.x_coordinates = old_x
            piece_hovered.y_coordinates = old_y
            return True            


def acquire_enemy_moveset(turn):
    enemy_moves = []
    for check in board.board_pieces:
        for enemy in check:
            if enemy.name is not None:
                if turn:
                    if enemy.color == "Black":
                        enemy_possible_moves = enemy.get_possible_moves(board.board_pieces)
                        enemy_moves += enemy_possible_moves
                else:
                    enemy_possible_moves = enemy.get_possible_moves(board.board_pieces)
                    enemy_moves += enemy_possible_moves
    return enemy_moves
        
def is_check(enemy_moves_attack):
    for find_king in board.board_pieces:
        for found in find_king:
            if white_turn:
                if found.name == "King" and found.color == "White":
                    if (found.x_coordinates, found.y_coordinates) in enemy_moves_attack:
                        return True
                    else:
                        return False
            else:
                if found.name == "King" and found.color == "Black":
                    if (found.x_coordinates, found.y_coordinates) in enemy_moves_attack:
                        return True
                    else:
                        return False

    return False


def allowed_moves(piece, moveset):
    allowed_set = []
    for m in moveset:
        if legal_check(piece, m):
            allowed_set.append(m)
    return allowed_set


def update_location(piece_hovered, coordinates_listed):
    y = piece_hovered.y_coordinates
    x = piece_hovered.x_coordinates
    new_y = coordinates_listed[1]
    new_x = coordinates_listed[0]
    piece_hovered.x_coordinates = new_x
    piece_hovered.y_coordinates = new_y
    board.board_pieces[y][x], board.board_pieces[new_y][new_x] = board.board_pieces[new_y][new_x], board.board_pieces[y][x]
    if board.board_pieces[y][x].name is not None:
        board.board_pieces[y][x] = Empty(x, y)

def highlight_selected_piece(coordinates):
    pygame.draw.rect(screen, "yellow", pygame.Rect(coordinates[0] * SIZE, coordinates[1] * SIZE, SIZE, SIZE), 5)


current_moves = []
possible = []
current_enemy_moves = []
white_turn = True
board.board_setup()
highlight = False

while running:
    game_state()
    screen.blit(board_map, ORIGIN)
    draw_pieces(board.board_pieces)
    draw_moves(possible)
    enemy_moves = acquire_enemy_moveset(white_turn)
    current_enemy_moves = enemy_moves
    if highlight:
        highlight_selected_piece(coordinates)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            coordinates = get_coordinates()
            piece_selected = get_selected_piece()
            if piece_selected.name is not None and piece_selected.color == "White" and white_turn:
                highlight = True
                piece_moves = get_allowed_moves(piece_selected)
                current_moves = piece_moves
                piece_name = piece_selected
                possible = allowed_moves(piece_selected, current_moves)
            if coordinates in possible and white_turn:
                update_location(piece_name, coordinates)
                enemy_moves = acquire_enemy_moveset(white_turn)
                current_moves = []
                possible = []
                white_turn = False
                highlight = False
                continue
            if piece_selected.name is not None and piece_selected.color == "Black" and not white_turn:
                highlight = True
                piece_moves = get_allowed_moves(piece_selected)
                current_moves = piece_moves
                piece_name = piece_selected
                possible = allowed_moves(piece_selected, current_moves)
            if coordinates in possible and not white_turn:
                update_location(piece_name, coordinates)
                enemy_moves = acquire_enemy_moveset(white_turn)
                current_moves = []
                possible = []
                white_turn = True
                highlight = False
            





    pygame.display.flip()

    clock.tick(60) 

pygame.quit()