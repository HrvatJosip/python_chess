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
