import random
import pygame
import math
from utils import Utils
from event import Event

class CatapultPreview():
    def __init__(self, position_x, position_y):
        self.image = pygame.image.load('./images/catapult-small.png')
        self.spoon_image = pygame.image.load('./images/catapult-spoon-small.png')
        self.position_x = position_x
        self.position_y = position_y
        self.scale = 0.75
        self.spoon_idle_speed = 10

        self.time = 0
        self.spoon_angle = 0

        self.spoon_pivot = [self.position_x + math.ceil(94 * self.scale), self.position_y + math.ceil(18 * self.scale)]
        self.spoon_pivot_offset = pygame.math.Vector2(-70 * self.scale, 5 * self.scale)

    def updateSpoonRotation(self, time_delta):
        self.spoon_angle = math.sin(self.time) * self.spoon_idle_speed

    def update(self, time_delta):
        self.time = self.time + time_delta
        self.updateSpoonRotation(time_delta)

    def draw(self, screen):
        rotated_spoon, rect = Utils.rotate(
            pygame.transform.rotozoom(self.spoon_image, 0, self.scale),
            self.spoon_angle,
            self.spoon_pivot,
            self.spoon_pivot_offset
        )
        screen.blit(rotated_spoon, rect)  # Blit the rotated image.

        screen.blit(
            pygame.transform.rotozoom(self.image, 0, self.scale),
            (self.position_x, self.position_y)
        )
