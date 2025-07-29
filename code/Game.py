import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            # se o usuário escolher uma das 3 primeiras opções de novo jogo
            if menu_return in MENU_OPTION[:3]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTION[4]:  # EXIT
                pygame.quit()  # Close Window
                quit()
            else:
                pass
