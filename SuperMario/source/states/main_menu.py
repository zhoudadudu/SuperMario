import pygame
from .. import setup
from .. import tools
from .. import constants as C
from .. components import info


class MainMenu:
    def __init__(self):
        self.setup_background()
        self.setup_player()
        self.setup_cursor()
        self.info = info.Info('main_menu')

    def setup_background(self):
        self.background = setup.GRAPHICS['bc1']
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (int(self.background_rect.width * C.BG_MULTI),
                                                                   int(self.background_rect.height * C.BG_MULTI)))
        self.viewport = setup.SCREEN.get_rect()
        self.caption = tools.get_image(setup.GRAPHICS['0'], 0, 0, 79, 79, (0,0,0), C.BG_MULTI)

    def setup_player(self):
        pass

    def setup_cursor(self):
        pass

    def update(self, surface):

        surface.blit(self.background, self.viewport)
        surface.blit(self.caption, (170, 100))

        self.info.update()
        self.info.draw(surface)