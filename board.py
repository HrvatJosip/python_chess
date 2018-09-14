import pygame


class ChessBoard:

    """Draws and maintains the state of the chess board

    Args:
        settings(obj): Settings object which contains settings for the game
        screen(obj): Reference to the surface displayed on the monitor

    Attributes:
        settings(obj): Settings object which contains settings for the game
        screen(obj): Reference to the surface displayed on the monitor
        board_squares(list): A list representation of pieces on the board
        white_square(obj): Image of a white square used for the board
        black_square(obj): Image of a black square used for the board
        square_size(int): Size of the squares sides in pixels
    """

    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.board_squares = [[None for column in range(8)] for row in range(8)]
        self.white_square = pygame.image.load('images/white_square.png')
        self.black_square = pygame.image.load('images/black_square.png')
        self.square_size = self.white_square.get_rect().width

    def get_board_state(self):
        """Return state of board as list"""
        return self.board_squares

    def draw(self):
        """Draws chess board on screen"""
        # Get board size in squares across.
        board_size = len(self.get_board_state())

        # Draw empty board on screen
        current_square = 0
        for row in range(board_size):
            for column in range(board_size):
                (screen_x, screen_y) = self.convert_to_screen_coord((row, column))
                if current_square:
                    self.screen.blit(self.black_square, (screen_x, screen_y))
                    current_square = (current_square + 1) % 2
                else:
                    self.screen.blit(self.white_square, (screen_x, screen_y))
                    current_square = (current_square + 1) % 2
            current_square = (current_square + 1) % 2

    def convert_algebraic_notation(self, square_coord):
        """Convert coordinate on chessboard to algebraic notation
        Algebraic notation begins at lower left square 1A (board_squares[7][0])

        Args:
            square_coord (int, int): Tuple containing row and column coordinate of a square

        Returns:
            Corresponding algebraic notation coordinate
        """
        (row, col) = square_coord
        return self.convert_algebraic_notation_column(col) + self.convert_algebraic_notation_row(row)

    def convert_algebraic_notation_row(self, row):
        """Convert row number to algebraic notation
        Algebraic notation begins at lower left square 1A (board_squares[7][0])

        Args:
            row(int): row on the chessboard in range 0-7 starting from the top

        Returns:
            Corresponding algebraic notation row number
        """
        number_coord = list(range(1, 9))
        return str(number_coord[(row + 1) * -1])

    def convert_algebraic_notation_column(self, col):
        """Convert column number to algebraic notation
        Algebraic notation begins at lower left square 1A (board_squares[7][0])

        Args:
            col(int): column on the chessboard in range 0-7 starting from left

        Returns:
            Corresponding algebraic notation column letter
        """
        letter_coord = list(map(chr, range(ord('a'), ord('i'))))
        return letter_coord[col]

    def convert_to_screen_coord(self, square_coord):
        """Convert chess coordinate into coordinate on screen

        Args:
            square_coord(int, int): Tuple containing row and column coordinates of a square

        Returns:
            Screen coordinate of top left corner of chess square
        """
        (row, col) = square_coord
        screen_x = self.settings.board_start_x + col * self.square_size
        screen_y = self.settings.board_start_y + row * self.square_size
        return screen_x, screen_y

    def convert_to_chess_coord(self, screen_coord):
        """Convert chess coordinate into coordinate on screen

            Args:
                screen_coord(int, int): Tuple containing x and y screen coordinates of a square

            Returns:
                Index of chess square within list board_squares
        """
        (x, y) = screen_coord
        row = int((y - self.settings.board_start_y) / self.square_size)
        col = int((x - self.settings.board_start_x) / self.square_size)
        return row, col
