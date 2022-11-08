import pygame
from .. import tools, setup
from .. import constants as C

class FlashingCoin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frame = []
        self.frame_index = 0
        frame_rects = [(320, 0, 79, 79), (400, 0, 79, 79), (480, 0, 79, 79), (560, 0, 79, 79), (480, 0, 79, 79), (400, 0, 79, 79)]
        self.load_frames(frame_rects)
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = 280
        self.rect.y = 50
        self.timer = 0

    def load_frames(self, frame_rects):
        sheet = setup.GRAPHICS['0']
        for frame_rect in frame_rects:
            self.frame.append(tools.get_image(sheet, *frame_rect, (0, 0, 0), C.BG_MULTI))

    def update(self):
        self.current_time = pygame.time.get_ticks()
        frame_durations = [125, 125, 125, 125, 125, 125]

        if self.timer == 0:
            self.timer = self.current_time
        elif self.current_time - self.timer > frame_durations[self.frame_index]:
            self.frame_index += 1
            self.frame_index %= 6
            self.timer = self.current_time

        self.image = self.frame[self.frame_index]