import pygame

class Moon():
    def __init__(self, position_x, position_y):
        self.image = pygame.image.load('./images/moon.png')
        self.position_x = position_x
        self.position_y = position_y
        self.scale = 0.3

    def draw(self, screen):
        screen.blit(
            pygame.transform.rotozoom(self.image, 0, self.scale),
            (self.position_x, self.position_y)
        )
