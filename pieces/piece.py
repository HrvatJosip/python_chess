from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color, square_coord):
        self.color = color
        self.coord = square_coord

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def is_legal_move(self):
        pass
