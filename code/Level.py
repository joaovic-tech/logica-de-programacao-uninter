#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import MENU_OPTION, EVENT_ENEMY, COLOR_GREEN, EVENT_TIMEOUT, ENTITY_SCORE, WIN_WIDTH, COLOR_WHITE
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'BG'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))

        # Caso o usuário escolha dois jogadores irar adicionar mais uma entidade
        # No caso o player2
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        pygame.time.set_timer(EVENT_ENEMY, 2000)

        self.timeout = 20000  # definir tempo de cada level
        pygame.time.set_timer(EVENT_TIMEOUT, 100)

    def run(self, ):
        clock = pygame.time.Clock()

        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)

        while True:
            clock.tick(60)

            # DESENHAR NA TELA
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # aqui é desenhado as entidades
                ent.move()

                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

                # textos a serem exibido na tela
                if ent.name == 'Player1':
                    self.level_text(22, f'Player 01: {ent.health}HP | Score: {ent.score}', COLOR_GREEN, (WIN_WIDTH - 400, 10))
                if ent.name == 'Player2':
                    self.level_text(22, f'Player 02: {ent.health}HP | Score: {ent.score}', COLOR_GREEN, (WIN_WIDTH - 400, 30))
                    self.level_text(22, f'Score: {ent.score}', COLOR_GREEN, (10, 30))

            self.level_text(22, f'{clock.get_fps():.0f} FPS', COLOR_GREEN, (10, 10))

            # Atualizar a tela
            pygame.display.flip()

            # VERIFICAR COLISÕES
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # CONFERIR EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                # Criando um decrementador para o tempo do jogo
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= 100
                    if self.timeout == 0:
                        return True

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
