# COLORS
import pygame

COLOR_ORANGE = (236, 142, 44)
COLOR_WHITE = (195, 209, 211)
COLOR_SELECTED = (201, 79, 79)
COLOR_GREEN = (12, 109, 26)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (255, 255, 128)

# MENU
MENU_OPTION = ('NEW GAME 1P', 'NEW GAME 2P - COOPERATIVE', 'NEW GAME 2P - COOPERATIVE', 'EXIT')

# DIMENSIONS
WIN_WIDTH = 576
WIN_HEIGHT = 324

# Eventos
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# Velocidade das entidades
ENTITY_SPEED = {
    'Level1BG0': 0,
    'Level1BG1': 1,
    'Level1BG2': 2,
    'Level1BG3': 3,
    'Level1BG4': 4,
    'Level2BG0': 0,
    'Level2BG1': 1,
    'Level2BG2': 2,
    'Level2BG3': 3,
    'Level2BG4': 4,
    'Level2BG5': 4,
    'Level2BG6': 4,
    'Player1': 3,
    'Player1Shot': 3,
    'Player2': 3,
    'Player2Shot': 3,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 5,
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

PLAYER_KEY_SHOOT = {
    'Player1': pygame.K_SPACE,
    'Player2': pygame.K_RCTRL
}

# Intervalos de criação de tiros quando a tecla de tiro for pressionada
ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 200,
}

# Vida das entidades
ENTITY_HEALTH = {
    'Level1BG0': 999,
    'Level1BG1': 999,
    'Level1BG2': 999,
    'Level1BG3': 999,
    'Level1BG4': 999,
    'Level2BG0': 999,
    'Level2BG1': 999,
    'Level2BG2': 999,
    'Level2BG3': 999,
    'Level2BG4': 999,
    'Level2BG5': 999,
    'Level2BG6': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 100,
    'Enemy1Shot': 1,
    'Enemy2': 100,
    'Enemy2Shot': 1,
}

# Danos
ENTITY_DAMAGE = {
    'Level1BG0': 0,
    'Level1BG1': 0,
    'Level1BG2': 0,
    'Level1BG3': 0,
    'Level1BG4': 0,
    'Level2BG0': 0,
    'Level2BG1': 0,
    'Level2BG2': 0,
    'Level2BG3': 0,
    'Level2BG4': 0,
    'Level2BG5': 0,
    'Level2BG6': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 25,
    'Enemy1': 5,
    'Enemy1Shot': 20,
    'Enemy2': 5,
    'Enemy2Shot': 25,
}

# Pontos
ENTITY_SCORE = {
    'Level1BG0': 0,
    'Level1BG1': 0,
    'Level1BG2': 0,
    'Level1BG3': 0,
    'Level1BG4': 0,
    'Level2BG0': 0,
    'Level2BG1': 0,
    'Level2BG2': 0,
    'Level2BG3': 0,
    'Level2BG4': 0,
    'Level2BG5': 0,
    'Level2BG6': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
}
