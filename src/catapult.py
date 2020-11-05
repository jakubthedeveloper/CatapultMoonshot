import random
import pygame
import math
from utils import Utils

class Catapult():
    def __init__(self, position_x, position_y):
        self.image = pygame.image.load('./images/catapult-small.png')
        self.spoon_image = pygame.image.load('./images/catapult-spoon-small.png')
        self.time = 0
        self.position_x = position_x
        self.position_y = position_y
        self.scale = 0.7

        # Store the original center position of the surface.
        self.spoon_pivot = [self.position_x + (94 * self.scale), self.position_y + (18 * self.scale)]
        # This offset vector will be added to the pivot point, so the
        # resulting rect will be blitted at `rect.topleft + offset`.
        self.spoon_pivot_offset = pygame.math.Vector2(-70 * self.scale, 5 * self.scale)

    def update(self, time_delta):
        self.time = self.time + time_delta

    def draw(self, screen):
        rotated_spoon, rect = Utils.rotate(
            pygame.transform.rotozoom(self.spoon_image, 0, self.scale),
            self.spoonRotation(),
            self.spoon_pivot,
            self.spoon_pivot_offset
        )
        screen.blit(rotated_spoon, rect)  # Blit the rotated image.
        #pygame.draw.circle(screen, (30, 250, 70), self.spoon_pivot, 3)  # Pivot point.
        #pygame.draw.rect(screen, (30, 250, 70), rect, 1)  # The rect.

        screen.blit(
            pygame.transform.rotozoom(self.image, 0, self.scale),
            (self.position_x, self.position_y)
        )

    def spoonRotation(self):
        return math.sin(self.time)*10
