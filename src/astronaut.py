import pygame
from utils import Utils
from event import Event
import math

class Astronaut():
    def __init__(self, position_x, position_y, catapult):
        self.image = pygame.image.load('./images/astronaut/Charac_S-S02-idle_0.png')
        self.image_front = pygame.image.load('./images/astronaut/Charac_F-S02-Idle_0.png')
        self.position = (position_x, position_y)
        self.catapult = catapult
        self.scale = 0.1
        self.fly_speed = 30
        self.flying = False
        self.landed = False
        self.angle = 0
        self.initial_boost = 30
        self.boost_decrease = 1
        self.boost = 0
        self.position_linear = self.position
        self.initial_flight_y = -2.5
        self.flight_y = self.initial_flight_y
        self.flight_curve_factor = 0.0
        self.flight_curve_scale = 2.0

        self.spoon_pivot_offset = pygame.math.Vector2(
            self.catapult.spoon_pivot_offset[0] - 38,
            self.catapult.spoon_pivot_offset[1] - 22
        )

    def fire(self, flight_curve_factor):
        self.flying = True
        self.boost = self.initial_boost
        self.flight_y = self.initial_flight_y
        self.flight_curve_factor = flight_curve_factor * self.flight_curve_scale

    def respawn(self):
        self.flying = False
        self.landed = False

    def get_center_position(self):
        return (
            self.position[0] + self.image.get_size()[0] * self.scale / 2,
            self.position[1] + self.image.get_size()[1] * self.scale / 2
        )

    def check_position(self, screen_width, screen_height):
        if not self.flying or self.landed:
            return

        if self.position[0] > screen_width or self.position[1] < 0 - self.image.get_size()[1] * self.scale:
            pygame.event.post(pygame.event.Event(Event.EVENT_LOOSE))

    def land_on_moon(self):
        if not self.landed:
            self.flying = False
            self.landed = True
            pygame.event.post(pygame.event.Event(Event.EVENT_LANDED))

    def update(self, time_delta):
        if self.flying and not self.landed:
            if self.boost > 0:
                self.boost = max(0, self.boost - self.boost_decrease)

            self.flight_y = self.flight_y + (self.flight_curve_factor * time_delta)
            self.position = self.position + pygame.math.Vector2(5, self.flight_y) * (self.fly_speed + self.boost) * time_delta

    def draw(self, screen):
        if self.landed:
            screen.blit(
                pygame.transform.rotozoom(self.image_front, -55, self.scale),
                self.position
            )
            return

        if self.flying:
            screen.blit(
                pygame.transform.rotozoom(self.image, -55, self.scale),
                self.position
            )
            return

        rotated_astronaut, rect = Utils.rotate(
            pygame.transform.rotozoom(self.image, 0, self.scale),
            self.catapult.spoon_angle,
            self.catapult.spoon_pivot,
            self.spoon_pivot_offset
        )
        screen.blit(rotated_astronaut, rect)

        self.position = (rect[0], rect[1])
        self.angle = self.catapult.spoon_angle
