import pygame

from pieces.piece import Piece
from pieces.type import Type


class Bishop(Piece):
    """Sets properties for a Bishop

    Args:
        settings(obj): Settings object which contains settings for the game
        screen(obj): Reference to the surface displayed on the monitor
        color(str): Color of piece
        square_coord(int, int): Tuple containing initial location of Bishop

    Attributes:
        image(obj): Image of Bishop
    """

    def __init__(self, settings, screen, color, square_coord):
        piece_type = Type.BISHOP
        super().__init__(settings, screen, color, square_coord, piece_type)
        self.image = pygame.image.load('images/'+color+'_bishop.png')
        self.image = pygame.transform.scale(self.image, (self.settings.square_size, self.settings.square_size))
