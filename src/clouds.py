import os
import pygame
import math

class Clouds():
    def __init__(self):
        self.image = pygame.image.load(os.path.join("images", "clouds.png"))
        alpha = 50
        self.image.fill((255, 255, 255, alpha), None, pygame.BLEND_RGBA_MULT)
        self.image_width = self.image.get_size()[0]
        self.offset_x = 0
        self.clouds_speed = 30

    def update(self, time_delta):
        self.offset_x = self.offset_x + self.clouds_speed * time_delta

        if (self.offset_x >= self.image_width):
            self.offset_x = 0

    def draw(self, screen):
        screen.blit(self.image, (0 - self.offset_x, 0))
        screen.blit(self.image, (0 + self.image_width - self.offset_x + 1, 0))
