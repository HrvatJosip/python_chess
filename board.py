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

    def get_piece_at_square(self, square_coord):
        """Gets piece at given square

            Args:
                 square_coord(int, int): Tuple containing row and column of given square

            Returns:
                Piece object or None
        """
        return self.get_board_state()[square_coord[0]][square_coord[1]]

    def is_square_empty(self, square_coord):
        """Check if square on board is empty

            Args:
                square_coord(int, int): Tuple containing row and column coordinates of a square

            Returns:
                True if square is empty. False is otherwise
        """
        return True if self.get_board_state()[square_coord[0]][square_coord[1]] is None else True

    def is_clear_path(self, from_tuple, to_tuple):
        """Check is path between 2 squares is clear

            Args:
                from_tuple(int, int): Tuple containing row and column coordinates of piece about to move
                to_tuple(int, int): Tuple containing row and column coordinates of piece destination

            Returns:
                True if path is clear. False if there is another piece between both points
        """
        # Store from_tuple coordinates in separate variables
        (from_square_row, from_square_col) = from_tuple
        # Store to_tuple coordinates in separate varibles
        (to_square_row, to_square_col) = to_tuple

        # Generate list of coordinates between both points
        # Vertical move
        if from_square_col == to_square_col and from_square_row != to_square_row:
            coord_list = [(row, to_square_col) for row in
                          range(min(from_square_row, to_square_row) + 1, max(from_square_row, to_square_row))]
        # Horizontal move
        elif from_square_row == to_square_row and from_square_col != to_square_col:
            coord_list = [(to_square_row, col) for col in
                          range(min(from_square_col, to_square_col) + 1, max(from_square_col, to_square_col))]
        # Diagonal move SE and NW
        elif ((from_square_row < to_square_row and from_square_col < to_square_col) or
              (from_square_row > to_square_row and from_square_col > to_square_col)):
            coord_list = [(min(from_square_row, to_square_row) + i, min(from_square_col, to_square_col) + i)
                          for i in range(1, abs(from_square_row - to_square_row))]
        # Diagonal move SW and NE
        else:
            coord_list = [(min(from_square_row, to_square_row) + i, max(from_square_col, to_square_col) - i)
                          for i in range(1, abs(from_square_row - to_square_row))]
        # Check if path is clear
        for coord in coord_list:
            if not self.is_square_empty(coord):
                return False
        return True
