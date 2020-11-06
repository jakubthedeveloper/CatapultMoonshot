import sys
sys.path.insert(0, './src')

import pygame
import pygame_gui
import random
import math
from datetime import datetime
from catapult import Catapult
from moon import Moon
from ground import Ground

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
(width, height) = (800, 600) # Dimension of the window
screen = pygame.display.set_mode((width, height)) # Making of the screen
pygame.display.set_caption("MoonShoot by JakubTheDeveloper")

background = pygame.Surface((width, height))
background.fill(pygame.Color('#79B2EC'))

catapult = Catapult(50, 480)
moon = Moon(630, 20)
ground = Ground()

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          is_running = False
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
              catapult.shot()

    screen.blit(background, (0, 0))
    catapult.update(time_delta)

    ground.draw(screen, width)
    catapult.draw(screen)
    moon.draw(screen)

    pygame.display.update()
