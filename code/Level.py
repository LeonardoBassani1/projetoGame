#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import pygame
import sys

from code.Const import MENU_OPTION, EVENT_ENEMY, SPAWN_TIME
from code.EntityFactory import EntityFactory

# Constantes globais (ajusta se necessário)
COLOR_WHITE = (255, 255, 255)
WIN_HEIGHT = 480  # coloca a altura real da tua janela aqui

class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.timeout = 60000  # tempo de exemplo em milissegundos
        self.entity_list = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1],MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)



        MENU_OPTION

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    if event.type == EVENT_ENEMY:
                        choice = random.choice(['Enemy1', 'Enemy2'])
                        self.entity_list.append(EntityFactory.get_entity(choice))
                    self.entity_list.append(EntityFactory.get_entity('Enemy1'))

            # Impressão dos textos na tela
            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s',
                            text_color=COLOR_WHITE, text_pos=(10, 5))
            self.level_text(text_size=14, text=f'FPS: {clock.get_fps():.0f}', text_color=COLOR_WHITE,
                            text_pos=(10, WIN_HEIGHT - 35))
            self.level_text(text_size=14, text=f'Entidades: {len(self.entity_list)}', text_color=COLOR_WHITE,
                            text_pos=(10, WIN_HEIGHT - 20))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
