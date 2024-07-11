#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display
from pygame import Surface

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1BG'))

    def run(self, ):
        pygame.mixer_music.load('./asset/fase1.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0)

        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass
