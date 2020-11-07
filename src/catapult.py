import random
import pygame
import math
from utils import Utils
from event import Event

class Catapult():
    def __init__(self, position_x, position_y):
        self.image = pygame.image.load('./images/catapult-small.png')
        self.spoon_image = pygame.image.load('./images/catapult-spoon-small.png')
        self.position_x = position_x
        self.position_y = position_y
        self.scale = 0.75
        self.shot_target_angle = 60
        self.spoon_idle_speed = 10
        self.spoon_shot_speed = 200
        self.spoon_restart_speed = 70

        self.time = 0
        self.is_shooting = False
        self.is_restarting = False
        self.spoon_angle = 0

        # Store the original center position of the surface.
        self.spoon_pivot = [self.position_x + math.ceil(94 * self.scale), self.position_y + math.ceil(18 * self.scale)]
        # This offset vector will be added to the pivot point, so the
        # resulting rect will be blitted at `rect.topleft + offset`.
        self.spoon_pivot_offset = pygame.math.Vector2(-70 * self.scale, 5 * self.scale)

    def spoon_angle(self):
        return self.spoon_angle

    def spoon_pivot(self):
        return self.spoon_pivot

    def spoon_pivot_offset(self):
        return self.spoon_pivot_offset

    def shot(self):
        self.is_shooting = True

    def updateSpoonRotation(self, time_delta):
        if (self.is_shooting and self.spoon_angle >= self.shot_target_angle):
            pygame.event.post(pygame.event.Event(Event.EVENT_FIRE))
            self.is_shooting = False
            self.is_restarting = True

        if (self.is_restarting and self.spoon_angle <= 0):
            self.is_restarting = False
            self.time = 0

        if (self.is_shooting):
            self.spoon_angle = self.spoon_angle + (self.spoon_shot_speed * time_delta)
            return

        if (self.is_restarting):
            self.spoon_angle = self.spoon_angle - (self.spoon_restart_speed * time_delta)
            return

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

        #pygame.draw.circle(screen, (30, 250, 70), self.spoon_pivot, 3)  # Pivot point.
        #pygame.draw.rect(screen, (30, 250, 70), rect, 1)  # The rect.
