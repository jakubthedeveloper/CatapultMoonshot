import pygame
from utils import Utils
from event import Event

class Astronaut():
    def __init__(self, position_x, position_y, catapult):
        self.image = pygame.image.load('./images/astronaut/Charac_S-S02-idle_0.png')
        self.position = (position_x, position_y)
        self.catapult = catapult
        self.scale = 0.1
        self.fly_speed = 0.5
        self.flying = False
        self.angle = 0

        self.spoon_pivot_offset = pygame.math.Vector2(
            self.catapult.spoon_pivot_offset[0] - 38,
            self.catapult.spoon_pivot_offset[1] - 22
        )

    def fire(self):
        self.flying = True

    def respawn(self):
        self.flying = False

    def check_position(self, screen_width, screen_height):
        if self.position[0] > screen_width or self.position[0] < 0 - self.image.get_size()[1]:
            pygame.event.post(pygame.event.Event(Event.EVENT_RESPAWN))

    def draw(self, screen):
        if self.flying:
            self.position = self.position + pygame.math.Vector2(5 * self.fly_speed, -2.5 * self.fly_speed)

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
        screen.blit(rotated_astronaut, rect)  # Blit the rotated image.

        self.position = (rect[0], rect[1])
        self.angle = self.catapult.spoon_angle

        #pygame.draw.circle(screen, (30, 250, 70), self.catapult.spoon_pivot, 3)
