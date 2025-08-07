import pygame

WIN_WIDTH = 576
WIN_HEIGHT = 324
C_ORANGE = (255, 165, 0)
C_YELLOW = (255, 255, 0)
C_WHITE = (255, 255, 255)

EVENT_ENEMY = pygame.USEREVENT +1

ENTITY_SPEED = {
'Player1': 3,
'Player2': 3,
'Enemy': 3,
'Level1Bg0': 0,
'Level1Bg1': 1,
'Level1Bg2': 2,
'Level1Bg3': 3,
'Level1Bg4': 4,
'Level1Bg5': 5,
'Level1Bg6': 6,
'Enemy1': 2,
'Enemy2': 1,
}


PLAYER_KEY_UP = {
    'Player1': pygame.K_UP,
    'Player2': pygame.K_w
}
PLAYER_KEY_DOWN = {
    'Player1': pygame.K_DOWN,
    'Player2': pygame.K_s
}
PLAYER_KEY_LEFT = {
    'Player1': pygame.K_LEFT,
    'Player2': pygame.K_a
}
PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_RIGHT,
    'Player2': pygame.K_d
}
PLAYER_KEY_SHOOT = {
    'Player1': pygame.K_RCTRL,
    'Player2': pygame.K_LCTRL
}

SPAWN_TIME = 4000


MENU_OPTION = ["NEW GAME 1P", "NEW GAME 2P - COOPERATIVE", "NEW GAME 2P - COMPETITIVE", "SCORE", "EXIT"]