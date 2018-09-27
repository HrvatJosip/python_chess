import pygame

from pieces.piece import Piece
from pieces.type import Type


class Knight(Piece):
    """Sets properties for a Knight

    Args:
        settings(obj): Settings object which contains settings for the game
        color(str): Color of piece
        square_coord(int, int): Tuple containing initial location of Knight

    Attributes:
        image_string(str): Image of Knight
    """

    def __init__(self, settings, color, square_coord):
        piece_type = Type.KNIGHT
        super().__init__(settings, color, square_coord, piece_type)
        self.image_string = 'images/' + color + '_knight.png'
