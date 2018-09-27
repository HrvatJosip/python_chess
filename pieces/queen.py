import pygame

from pieces.piece import Piece
from pieces.type import Type


class Queen(Piece):
    """Sets properties for a Queen

    Args:
        settings(obj): Settings object which contains settings for the game
        color(str): Color of piece
        square_coord(int, int): Tuple containing initial location of Queen

    Attributes:
        image_string(str): Image of Queen
    """

    def __init__(self, settings, color, square_coord):
        piece_type = Type.QUEEN
        super().__init__(settings, color, square_coord, piece_type)
        self.image_string = 'images/' + color + '_queen.png'
