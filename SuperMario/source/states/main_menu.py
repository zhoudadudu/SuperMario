import pygame
from .. import setup
from .. import tools
from .. import constants as C
from ..components import info


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
        self.cursor = pygame.sprite.Sprite()
        self.cursor.image = tools.get_image(setup.GRAPHICS['weapon5'], 0, 0, 48, 48, (0, 0, 0), C.BG_MULTI)
        rect = self.cursor.image.get_rect()
        rect.x, rect.y = (320, 64)
        self.cursor.rect = rect
        self.cursor.state = '1P'

    def update_cursor(self, keys):
        if keys[pygame.K_UP]:
            self.cursor.state = '1P'
            self.cursor.rect.y = 64
        elif keys[pygame.K_DOWN]:
            self.cursor.state = '2P'
            self.cursor.rect.y = 84
        elif keys[pygame.K_RETURN]:
            if self.state == '1P':
                pass
            elif self.state == '2P':
                pass

    def update(self, surface, keys):

        self.setup_cursor(keys)

        surface.blit(self.background, self.viewport)
        surface.blit(self.caption, (50, 50))
        surface.blit(self.cursor.image, self.cursor.rect)

        self.info.update()
        self.info.draw(surface)