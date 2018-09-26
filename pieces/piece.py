from abc import ABC


class Piece(ABC):
    def __init__(self, settings, screen, color, square_coord, piece_type):
        self.settings = settings
        self.screen = screen
        self.color = color
        self.square_coord = square_coord
        self.row = square_coord[0]
        self.col = square_coord[1]
        self.piece_type = piece_type
        self.image = ''
        super().__init__()

    def move(self, coord_to_move):
        pass

    def draw(self, screen_x, screen_y):
        self.screen.blit(self.image, (screen_x, screen_y))
