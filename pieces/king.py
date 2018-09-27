import pygame

from pieces.piece import Piece
from pieces.type import Type


class King(Piece):
    """Sets properties for a King

    Args:
        settings(obj): Settings object which contains settings for the game
        color(str): Color of piece
        square_coord(int, int): Tuple containing initial location of King

    Attributes:
        has_moved(bool): Flag checking if King has moved previously(for castling)
        image(obj): Image of King
    """

    def __init__(self, settings, color, square_coord):
        piece_type = Type.KING
        super().__init__(settings, color, square_coord, piece_type)
        self.has_moved = False
        self.image_string = 'images/' + color + '_king.png'

    def move(self, coord_to_move):
        """Moves Piece to another square

        Args:
            coord_to_move(int, int): Tuple containing row and column coordinates of a square
        """
        super().move(coord_to_move)
        # Change flag to moved
        if not self.has_moved:
            self.has_moved = True
