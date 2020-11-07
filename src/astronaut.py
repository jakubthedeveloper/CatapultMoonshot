import pygame

class Astronaut():
    def __init__(self, position_x, position_y):
        self.image = pygame.image.load('./images/astronaut/Charac_S-S02-idle_0.png')
        self.position_x = position_x
        self.position_y = position_y
        self.scale = 0.1

    def draw(self, screen):
        screen.blit(
            pygame.transform.rotozoom(self.image, 0, self.scale),
            (self.position_x, self.position_y)
        )
