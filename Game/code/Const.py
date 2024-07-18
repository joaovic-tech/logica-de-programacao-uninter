# COLORS
import pygame

COLOR_ORANGE = (236, 142, 44)
COLOR_WHITE = (195, 209, 211)
COLOR_SELECTED = (201, 79, 79)
COLOR_FPS = (12, 109, 26)

# MENU
MENU_OPTION = ('NEW GAME 1P', 'NEW GAME 2P - COOPERATIVE', 'NEW GAME 2P - COOPERATIVE', 'EXIT')

# DIMENSIONS
WIN_WIDTH = 576
WIN_HEIGHT = 324

# Evento do inimigo
EVENT_ENEMY = pygame.USEREVENT + 1

# Velocidade das entidades
ENTITY_SPEED = {
    'Level1BG1': 0,
    'Level1BG2': 1,
    'Level1BG3': 2,
    'Level1BG4': 3,
    'Level1BG5': 4,
    'Level1BG6': 5,
    'Level1BG7': 6,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1
}

# Teclas dos jogadores
PLAYER_KEY_UP = {
    'Player1': pygame.K_w,
    'Player2': pygame.K_UP
}

PLAYER_KEY_DOWN = {
    'Player1': pygame.K_s,
    'Player2': pygame.K_DOWN
}

PLAYER_KEY_LEFT = {
    'Player1': pygame.K_a,
    'Player2': pygame.K_LEFT
}

PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_d,
    'Player2': pygame.K_RIGHT
}

# Vida das entidades
ENTITY_HEALTH = {
    'Level1BG1': 999,
    'Level1BG2': 999,
    'Level1BG3': 999,
    'Level1BG4': 999,
    'Level1BG5': 999,
    'Level1BG6': 999,
    'Level1BG7': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 300,
    'Enemy2': 300
}
