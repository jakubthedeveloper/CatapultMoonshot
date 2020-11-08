import os
import pygame
import math

class Moon():
    def __init__(self, position_x, position_y):
        self.image = pygame.image.load(os.path.join("images", "moon.png"))
        self.position_x = position_x
        self.position_y = position_y
        self.scale = 0.3
        self.radius = (self.image.get_size()[0] * self.scale) / 2
        self.center = (
            math.ceil(self.position_x + self.radius),
            math.ceil(self.position_y + self.radius)
        )

    # 0.0 - 1.0 - on moon
    # > 1.0 - outside moon
    def center_dist(self, point):
        dist = math.hypot(point[0] - self.center[0], point[1] - self.center[1])
        return dist / self.radius

    def draw(self, screen):
        screen.blit(
            pygame.transform.rotozoom(self.image, 0, self.scale),
            (self.position_x, self.position_y)
        )

        #pygame.draw.circle(screen, (30, 250, 70), self.center, 3)
