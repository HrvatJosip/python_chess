from abc import ABC


class Piece(ABC):
    """Abstract class that sets properties for all Pieces

    Args:
        settings(obj): Settings object which contains settings for the game
        screen(obj): Reference to the surface displayed on the monitor
        color(str): Color of piece
        square_coord(int, int): Tuple containing initial location of Piece
        piece_type(Type): The type of piece (i.e. Pawn, Bishop, etc.)

    Attributes:
        settings(obj): Settings object which contains settings for the game
        screen(obj): Reference to the surface displayed on the monitor
        color(str): Color of piece
        square_coord(int, int): Tuple containing initial location of Piece
        self.row(int): Row number
        piece_type(Type): The type of piece (i.e. Pawn, Bishop, etc.)
        image(obj): Image used to display Piece
    """
    def __init__(self, settings, screen, color, square_coord, piece_type):
        self.settings = settings
        self.screen = screen
        self.color = color
        self.square_coord = square_coord
        self.piece_type = piece_type
        self.image = None
        super().__init__()

    def move(self, coord_to_move):
        """Moves Piece to another square

        Args:
            coord_to_move(int, int): Tuple containing row and column coordinates of a square
        """
        self.square_coord = coord_to_move

    def draw(self, screen_x, screen_y):
        """Draws Piece onto screen

            Args:
                screen_x(int): x coordinate where top left of image is displayed
                screen_y(int): y coordinate where top left of image is displayed
        """
        self.screen.blit(self.image, (screen_x, screen_y))

    def get_row(self):
        """Get row Piece is currently on"""
        return self.square_coord[0]

    def get_col(self):
        """Get column Piece is currently on"""
        return self.square_coord[1]
