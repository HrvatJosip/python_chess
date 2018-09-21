from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color, square_coord):
        self.color = color
        self.coord = square_coord
        super().__init__()

    @abstractmethod
    def move(self, coord_to_move):
        pass

    @abstractmethod
    def is_legal_move(self, coord_to_move):
        pass
