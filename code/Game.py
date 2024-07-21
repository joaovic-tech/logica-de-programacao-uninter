#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.display

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in MENU_OPTION[:3]:  # Considerando que MENU_OPTION tem pelo menos 3 elementos
                player_score = [0, 0]
                levels = ['Level1', 'Level2']

                for level_name in levels:
                    level = Level(self.window, level_name, menu_return, player_score)
                    level_return = level.run(player_score)

                    if not level_return:
                        break

            else:
                pygame.quit()
                sys.exit()
