import pygame

from pieces.piece import Piece
from pieces.type import Type


class Pawn(Piece):
    """Sets properties for a Pawn

    Args:
        settings(obj): Settings object which contains settings for the game
        screen(obj): Reference to the surface displayed on the monitor
        color(str): Color of piece
        square_coord(int, int): Tuple containing initial location of Pawn

    Attributes:
        has_moved(bool): Flag checking if Pawn has moved previously(en  passant, double step)
        image(obj): Image of Pawn
    """

    def __init__(self, settings, screen, color, square_coord):
        piece_type = Type.PAWN
        super().__init__(settings, screen, color, square_coord, piece_type)
        self.has_moved = False
        self.image = pygame.image.load('images/'+color+'_pawn.png')
        self.image = pygame.transform.scale(self.image, (self.settings.square_size, self.settings.square_size))
