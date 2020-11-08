#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.join("src"))

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
from menu import Menu

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

white = (255, 255, 255)
black = (0, 0, 0)
(width, height) = (800, 600) # Dimension of the window
screen = pygame.display.set_mode((width, height)) # Making of the screen
pygame.display.set_caption("MoonShoot by JakubTheDeveloper")
background = pygame.image.load(os.path.join("images", "bg.png"))

you_win_sound = pygame.mixer.Sound(os.path.join("sounds", "you-win.wav"))
you_win_sound.set_volume(1.0)

you_loose_sound = pygame.mixer.Sound(os.path.join("sounds", "you-loose.wav"))
you_loose_sound.set_volume(1.0)

shoot_sound = pygame.mixer.Sound(os.path.join("sounds", "bow.wav"))
shoot_sound.set_volume(1.0)

flight_sound = pygame.mixer.Sound(os.path.join("sounds", "flight.wav"))
flight_sound.set_volume(1.0)

message_font = pygame.font.Font(os.path.join("fonts", "upheavtt.ttf"), 24)
landed_messages = [
    message_font.render("You have successfully landed on the moon", True, (255, 255, 255)),
    message_font.render("Press Space to play again", True, (255, 255, 255)),
    message_font.render("or Esc to return to the main menu.", True, (255, 255, 255)),
]
show_landed_messages = False

SPEED_BABY = 2
SPEED_EASY = 5
SPEED_HARD = 10
SPEED_EXTREME = 15

ground = Ground()
moon = Moon(630, 20)
catapult = Catapult(50, 480)
astronaut = Astronaut(20, 490, catapult)
clouds = Clouds()

clock = pygame.time.Clock()
menu = Menu(screen, clock)

while True:
    show_landed_messages = False
    difficulty = menu.run()

    if difficulty == 'extreme':
        speed = SPEED_EXTREME
    elif difficulty == 'hard':
        speed = SPEED_HARD
    elif difficulty == 'baby':
        speed = SPEED_BABY
    else:
        speed = SPEED_EASY

    curve_bar = ParameterBar(10, 10, speed)
    astronaut.respawn()

    if difficulty:
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
                          show_landed_messages = False
                          astronaut.respawn()
                          curve_bar.restart()
                          you_win_sound.fadeout(500)
                      else:
                          shoot_sound.play(0)
                          catapult.shot()
                          curve_bar.freeze()

              if event.type == Event.EVENT_FIRE:
                  if not astronaut.flying and not astronaut.landed:
                      astronaut.fire(curve_bar.get_value())
                      flight_sound.play(0, 0, 1000)
              if event.type == Event.EVENT_LOOSE:
                  you_loose_sound.play(0)
                  flight_sound.fadeout(100)
                  astronaut.respawn()
                  curve_bar.restart()
              if event.type == Event.EVENT_LANDED:
                  show_landed_messages = True
                  flight_sound.fadeout(100)
                  you_win_sound.play(0)

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

            if show_landed_messages:
                for i in range(len(landed_messages)):
                    screen.blit(landed_messages[i], (140, 180 + (i * 40)))

            if moon.center_dist(astronaut.get_center_position()) < 0.8:
                astronaut.land_on_moon()

            pygame.display.update()

    you_win_sound.fadeout(1000)
    flight_sound.fadeout(500)
pygame.quit()
