import pygame
import sys
from menu_button import MenuButton
from catapult_preview import CatapultPreview

class Menu(object):
    done = False
    screen = None
    level = None
    buttons = []

    def __init__(self, screen, clock):
        pygame.font.init()
        self.screen = screen
        self.clock = clock

        screen_width = screen.get_size()[0]
        self.buttons = [
            MenuButton('Easy', screen_width / 2 - 200, 320, lambda: self.start('easy')),
            MenuButton('Hard', screen_width / 2, 320, lambda: self.start('hard')),
            MenuButton('Extreme', screen_width / 2 + 200, 320, lambda: self.start('extreme')),
            MenuButton('Quit', screen_width / 2, 525, lambda: self.quit())
        ]

        self.title_font = pygame.font.Font('./fonts/upheavtt.ttf', 36)
        self.title = self.title_font.render("Catapult MoonShoot", True, (255, 255, 255))

        self.menu_font = pygame.font.SysFont('Verdana', 26)

        self.label_instructions = [
            self.menu_font.render("Instruction:", True, (255, 255, 255)),
            self.menu_font.render("Press space to shot the astronaut.", True, (255, 255, 255)),
            self.menu_font.render("Try to shot when the indicator is in the middle.", True, (255, 255, 255))
        ]
        self.label_select_difficulty = self.menu_font.render("Select difficulty:", True, (255, 255, 255))

        self.astronaut_image = pygame.image.load('./images/astronaut/Charac_S-S02-idle_0.png')
        self.moon_image = pygame.image.load('./images/moon.png')
        self.catapult_preview = CatapultPreview(330, 420)

    def quit(self):
        self.done = True
        pygame.quit()
        sys.exit(0)

    def start(self, difficulty):
        self.done = True
        self.difficulty = difficulty

    def eventLoop(self):
        self.mouse_released = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                for button in self.buttons:
                    if button.checkMouseOver(pygame.mouse.get_pos()):
                        button.click_callback()

    def draw(self):
        self.screen.fill((0,0,0))

        self.screen.blit(self.title, (100, 40))

        for i in range(len(self.label_instructions)):
            self.screen.blit(self.label_instructions[i], (180, 100 + (i * 40)))

        self.screen.blit(
            pygame.transform.rotozoom(self.astronaut_image, 0, 0.2),
            (100, 100)
        )

        self.screen.blit(
            pygame.transform.rotozoom(self.moon_image, 0, 0.2),
            (620, 30)
        )

        self.screen.blit(self.label_select_difficulty, (100, 240))

        self.catapult_preview.draw(self.screen)

        for button in self.buttons:
            button.draw(self.screen, pygame.mouse.get_pos())

        pygame.display.flip()

    def main_loop(self):
        while not self.done:
            time_delta = self.clock.tick(60)/1000.0
            self.catapult_preview.update(time_delta)
            self.eventLoop()
            self.draw()

    def run(self):
        self.done = False
        self.difficulty = None
        self.main_loop()
        return self.difficulty
