import os
import pygame
import math

class ParameterBar():
    def __init__(self, position_x, position_y, speed):
        self.background_image = pygame.image.load(os.path.join("images", "parameter-bar-bg.png"))
        self.pointer_image  = pygame.image.load(os.path.join("images", "parameter-bar-pointer.png"))
        self.scale = 0.4
        self.position_x = position_x
        self.position_y = position_y
        self.background_width = self.background_image.get_size()[0]
        self.center_x = math.ceil(self.background_width / 2)
        self.pointer_width = math.ceil(self.pointer_image.get_size()[0] / 2)
        self.value = 0 # -1.0 to 1.0
        self.pointer_area_size = 0.9
        self.speed = speed
        self.time = 0
        self.running = True

    def freeze(self):
        self.running = False

    def restart(self):
        self.running = True

    def get_value(self):
        return self.value

    def update(self, time_delta):
        if self.running:
            self.time = self.time + time_delta
            self.value = math.sin(self.time * self.speed)

    def draw(self, screen):
        screen.blit(
            pygame.transform.rotozoom(self.background_image, 0, self.scale),
            (self.position_x, self.position_y)
        )

        screen.blit(
            pygame.transform.rotozoom(self.pointer_image, 0, self.scale),
            (
                self.position_x + self.center_x * self.scale - self.pointer_width / 2 + self.value * self.background_width * self.scale / 2 * self.pointer_area_size,
                self.position_y + 16 * self.scale
            )
        )
