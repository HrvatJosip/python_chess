import sys
import os

import pygame

from settings import Settings


def run_game():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Chess")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(settings.bg_color)
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
