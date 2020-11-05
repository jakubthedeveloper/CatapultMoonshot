import pygame
import math

class Ground():
    def __init__(self):
        self.image = pygame.image.load('./images/ground.png')
        self.scale = 0.3
        self.image_width = self.image.get_size()[0] * self.scale

    def draw(self, screen, screen_width):
        ground_repeats = math.ceil(screen_width / self.image_width)
        for i in range(ground_repeats):
            screen.blit(
                pygame.transform.rotozoom(self.image, 0, self.scale),
                (self.image_width * i, 540)
            )
