import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import SCORE_POSITION, MENU_OPTION, COLOR_GREEN, COLOR_BLACK, COLOR_SELECTED, COLOR_YELLOW, \
    COLOR_ORANGE, COLOR_WHITE
from code.DBProxy import DBProxy


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f'{current_time} - {current_date}'


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/menu-background.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, menu_option: str, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/menu.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            # Criando títulos
            self.score_text('YOU WIN!!', 48, COLOR_GREEN, SCORE_POSITION['Title'])

            if menu_option == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Player 1 ente with your name (4 caracteres)'

            if menu_option == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter with the name the team (4 caracteres)'

            if menu_option == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Player 1 ente with your name (4 caracteres)'
                else:
                    score = player_score[1]
                    text = 'Player 2 ente with your name (4 caracteres)'

            self.score_text(text, 20, COLOR_BLACK, SCORE_POSITION['EnterName'])

            # CONFERIR EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode

            self.score_text(name, 20, COLOR_SELECTED, SCORE_POSITION['Name'])
            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load(f'./asset/menu.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)

        # Mostrar o título
        self.score_text('TOP 10 SCORE', 48, COLOR_YELLOW, SCORE_POSITION['Title'])

        # Mostrar os nomes do players
        self.score_text('NAME    SCORE        DATE    ', 20, COLOR_WHITE, SCORE_POSITION['Label'])

        # Mostrar os score's
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(f'{name}    {score: 05d}        {date}', 20, COLOR_ORANGE, SCORE_POSITION[list_score.index(player_score)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

            pygame.display.flip()


    def score_text(self, text: str, text_size: int, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
