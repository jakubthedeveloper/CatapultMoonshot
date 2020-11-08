import sys
sys.path.insert(0, './src')

import pygame
import pygame_gui
import random
import math
from datetime import datetime
from event import Event
from catapult import Catapult
from moon import Moon
from ground import Ground
from astronaut import Astronaut
from clouds import Clouds
from parameter_bar import ParameterBar

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
(width, height) = (800, 600) # Dimension of the window
screen = pygame.display.set_mode((width, height)) # Making of the screen
pygame.display.set_caption("MoonShoot by JakubTheDeveloper")
background = pygame.image.load('./images/bg.png')

SPEED_EASY = 5
SPEED_HARD = 10
SPEED_EXTREME = 15

ground = Ground()
moon = Moon(630, 20)
catapult = Catapult(50, 480)
astronaut = Astronaut(20, 490, catapult)
clouds = Clouds()
curve_bar = ParameterBar(10, 10, SPEED_EASY)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          is_running = False
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
              is_running = False
          if event.key == pygame.K_SPACE:
              if astronaut.landed:
                  astronaut.respawn()
                  curve_bar.restart()
              else:
                  catapult.shot()
                  curve_bar.freeze()

      if event.type == Event.EVENT_FIRE:
          if not astronaut.flying and not astronaut.landed:
              astronaut.fire(curve_bar.get_value())
      if event.type == Event.EVENT_RESPAWN:
          astronaut.respawn()
          curve_bar.restart()

    astronaut.check_position(width, height)
    catapult.update(time_delta)
    astronaut.update(time_delta)
    clouds.update(time_delta)
    curve_bar.update(time_delta)

    screen.blit(background, (0, 0))
    ground.draw(screen, width)
    moon.draw(screen)
    astronaut.draw(screen)
    catapult.draw(screen)
    clouds.draw(screen)
    curve_bar.draw(screen)

    if moon.center_dist(astronaut.get_center_position()) < 0.8:
        astronaut.land_on_moon()

    pygame.display.update()
