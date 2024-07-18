#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image
from pygame import Surface

from code.Const import ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name, position: tuple):
        self.name = name
        self.surf: Surface = pygame.image.load('./asset/' + name + '.png').convert_alpha()

        if (name == 'Player1'):
            self.surf = pygame.transform.scale(self.surf, (58.5, 37.5))

        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move(self, ):
        pass

