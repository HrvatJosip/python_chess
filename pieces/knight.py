import pygame

from pieces.piece import Piece
from pieces.type import Type


class Knight(Piece):
    """Sets properties for a Knight

    Args:
        settings(obj): Settings object which contains settings for the game
        screen(obj): Reference to the surface displayed on the monitor
        color(str): Color of piece
        square_coord(int, int): Tuple containing initial location of Knight

    Attributes:
        image(obj): Image of Knight
    """

    def __init__(self, settings, screen, color, square_coord):
        piece_type = Type.KNIGHT
        super().__init__(settings, screen, color, square_coord, piece_type)
        self.image = pygame.image.load('images/'+color+'_knight.png')
        self.image = pygame.transform.scale(self.image, (self.settings.square_size, self.settings.square_size))
