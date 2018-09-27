import pygame

from pieces.piece import Piece
from pieces.type import Type


class Bishop(Piece):
    """Sets properties for a Bishop

    Args:
        settings(obj): Settings object which contains settings for the game
        color(str): Color of piece
        square_coord(int, int): Tuple containing initial location of Bishop

    Attributes:
        image_string(str): Image of Bishop
    """

    def __init__(self, settings, color, square_coord):
        piece_type = Type.BISHOP
        super().__init__(settings, color, square_coord, piece_type)
        self.image_string = 'images/'+color+'_bishop.png'
