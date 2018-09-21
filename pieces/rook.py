from pieces.piece import Piece


class Rook(Piece):

    def __init__(self, color, square_coord):
        super().__init__(color, square_coord)
        has_moved = False

    def move(self, coord_to_move):
        pass

    def is_legal_move(self, coord_to_move):
        pass
