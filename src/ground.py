import pygame
import math

class Ground():
    def __init__(self):
        self.image = pygame.image.load('./images/ground.png')
        self.scale = 0.4
        self.image_width = math.ceil(self.image.get_size()[0] * self.scale)
        self.image_height = math.ceil(self.image.get_size()[1] * self.scale)

    def draw(self, screen, screen_width):
        ground_repeats = math.ceil(screen_width / self.image_width)
        for i in range(ground_repeats):
            screen.blit(
                pygame.transform.scale(self.image, (self.image_width, self.image_height)),
                (self.image_width * i, 540)
            )
