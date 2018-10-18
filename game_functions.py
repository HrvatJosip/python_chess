import sys
import pygame


def convert_algebraic_notation(square_coord):
    """Convert coordinate on chessboard to algebraic notation
    Algebraic notation begins at lower left square 1A (board_squares[7][0])

    Args:
        square_coord (int, int): Tuple containing row and column coordinate of a square

    Returns:
        Corresponding algebraic notation coordinate
    """
    (row, col) = square_coord
    return convert_algebraic_notation_column(col) + convert_algebraic_notation_row(row)


def convert_algebraic_notation_row(row):
    """Convert row number to algebraic notation
    Algebraic notation begins at lower left square 1A (board_squares[7][0])

    Args:
        row(int): row on the chessboard in range 0-7 starting from the top

    Returns:
        Corresponding algebraic notation row number
    """
    number_coord = list(range(1, 9))
    return str(number_coord[(row + 1) * -1])


def convert_algebraic_notation_column(col):
    """Convert column number to algebraic notation
    Algebraic notation begins at lower left square 1A (board_squares[7][0])

    Args:
        col(int): column on the chessboard in range 0-7 starting from left

    Returns:
        Corresponding algebraic notation column letter
    """
    letter_coord = list(map(chr, range(ord('a'), ord('i'))))
    return letter_coord[col]


def opponent_color(player_color):
    if player_color == 'white':
        return 'black'
    else:
        return 'white'


def check_events(board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            square_clicked = board.convert_to_chess_coord((mouse_x, mouse_y))
            if square_clicked[0] < 0 or square_clicked[0] > 7 or square_clicked[1] < 0 or square_clicked[1] > 7:
                square_clicked = []


def update_board(board):
    for piece in board.pieces_on_board:
        board.get_board_state()[piece.get_row()][piece.get_col()] = piece






