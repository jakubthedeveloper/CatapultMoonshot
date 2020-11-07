import pygame
from utils import Utils

class Astronaut():
    def __init__(self, position_x, position_y, catapult):
        self.image = pygame.image.load('./images/astronaut/Charac_S-S02-idle_0.png')
        self.position_x = position_x
        self.position_y = position_y
        self.catapult = catapult
        self.scale = 0.1

        self.spoon_pivot_offset = pygame.math.Vector2(
            self.catapult.spoon_pivot_offset[0] - 38,
            self.catapult.spoon_pivot_offset[1] - 22
        )

    def draw(self, screen):
        #screen.blit(
        #    pygame.transform.rotozoom(self.image, 0, self.scale),
        #    (self.position_x, self.position_y)
        #)

        rotated_astronaut, rect = Utils.rotate(
            pygame.transform.rotozoom(self.image, 0, self.scale),
            self.catapult.spoon_angle,
            self.catapult.spoon_pivot,
            self.spoon_pivot_offset
        )
        screen.blit(rotated_astronaut, rect)  # Blit the rotated image.

        pygame.draw.circle(screen, (30, 250, 70), self.catapult.spoon_pivot, 3)
