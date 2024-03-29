import pygame

from . import coin
from .. import constants as C
from .. import setup, tools

pygame.font.init()

class Info:
    def __init__(self, state, game_info):
        self.state = state
        self.game_info = game_info
        self.create_state_labels()
        self.create_info_labels()
        self.flash_coin = coin.FlashingCoin()

    def create_state_labels(self):
        self.state_labels = []
        if self.state == 'main_menu':
            self.state_labels.append((self.create_label('START GAME'), (280, 220)))
            self.state_labels.append((self.create_label('EXIT GAME'), (290, 320)))
            #self.state_labels.append((self.create_label('TOP - '), (400, 50)))
            #self.state_labels.append((self.create_label('000000'), (500, 50)))

        elif self.state == 'load_screen':
            #self.state_labels.append((self.create_label('WORLD'), (400, 100)))
            #self.state_labels.append((self.create_label('1 - 1'), (400, 150)))
            #self.state_labels.append((self.create_label('TOP - '), (400, 50)))
            self.state_labels.append((self.create_label('Lives      {}'.format(self.game_info['lives'])), (300, 300)))
            self.player_image = tools.get_image(setup.GRAPHICS['0'], 0, 0, 0, 0, (0, 0, 0), C.BG_MULTI)

        elif self.state == 'level':
            self.state_labels.append((self.create_label('Lives   {}'.format(self.game_info['lives'])), (290, 50)))

        elif self.state == 'game_over':
            self.state_labels.append((self.create_label('GAME OVER'), (280, 300)))



    def create_info_labels(self):
        self.info_labels = []
        self.info_labels.append((self.create_label('SuperMario'), (290, 80)))

    def create_label(self, label, size=40, width_scale=1.25, height_scale=1):
        font = pygame.font.SysFont(C.FONT, size)
        label_image = font.render(label, 1, (255, 255, 255))
        rect = label_image.get_rect()
        label_image = pygame.transform.scale(label_image, (int(rect.width * width_scale),
                                                           int(rect.height * height_scale)))
        return label_image

    def update(self):
        self.flash_coin.update()

    def draw(self, surface):
        for label in self.state_labels:
            surface.blit(label[0], label[1])
        #for label in self.info_labels:
            #surface.blit(label[0], label[1])

            #surface.blit(self.flash_coin.image, self.flash_coin.rect)

        #if self.state == 'load_screen':
            #surface.blit(self.player_image, (100, 100))

    def draw_loadScreen(self, surface):
        for label in self.state_labels:
            surface.blit(label[0], label[1])
        for label in self.info_labels:
            surface.blit(label[0], label[1])

            surface.blit(self.flash_coin.image, self.flash_coin.rect)

        if self.state == 'load_screen':
            surface.blit(self.player_image, (100, 100))