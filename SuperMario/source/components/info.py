import pygame
from .. import constants as C
pygame.font.init()

class Info:
    def __init__(self, state):
        self.state = state
        self.create_state_labels()
        self.create_info_labels()

    def create_state_labels(self):
        self.state_labels = []
        if self.state == 'main_menu':
            self.state_labels.append((self.create_label('1 PLAYER GAME'), (400, 100)))
            self.state_labels.append((self.create_label('2 PLAYER GAME'), (400, 150)))
            self.state_labels.append((self.create_label('TOP - '), (400, 50)))
            self.state_labels.append((self.create_label('000000'), (500, 50)))

    def create_info_labels(self):
        self.info_labels = []
        self.info_labels.append((self.create_label('LF2'), (100, 50)))

    def create_label(self, label, size=40, width_scale=1.25, height_scale=1):
        font = pygame.font.SysFont(C.FONT, size)
        label_image = font.render(label, 1, (255, 255, 255))
        rect = label_image.get_rect()
        label_image = pygame.transform.scale(label_image, (int(rect.width * width_scale),
                                                           int(rect.height * height_scale)))
        return label_image

    def update(self):
        pass

    def draw(self, surface):
        for label in self.state_labels:
            surface.blit(label[0], label[1])
        for label in self.info_labels:
            surface.blit(label[0], label[1])